#!/usr/bin/env python3
import sys
import ast
import os

filename = os.environ.get("map_input_file", "unknown")

code = sys.stdin.read()

try:
    tree = ast.parse(code)
except SyntaxError:
    print(f"{filename}\tSYNTAX_ERROR\t1")
    sys.exit(0)

# Find undefined variable names
defined_names = set()
used_names = []

class NameCollector(ast.NodeVisitor):
    def visit_Assign(self, node):
        # builds list of defined variables
        for target in node.targets:
            if isinstance(target, ast.Name):
                defined_names.add(target.id)
        self.generic_visit(node)

    def visit_Name(self, node):
        # builds list of named variables
        if isinstance(node.ctx, ast.Load):
            used_names.append(node.id)
        self.generic_visit(node)

collector = NameCollector()
collector.visit(tree)

# Check named but undefined variables
for name in used_names:
    if name not in defined_names and not hasattr(__builtins__, name):
        print(f"{filename}\tERROR_NAME_UNDEFINED_{name.upper()}\t1")

# Walk through AST nodes for structural errors
for node in ast.walk(tree):

    # Bare except (handles every possible exception)
    if isinstance(node, ast.ExceptHandler) and node.type is None:
        print(f"{filename}\tERROR_BARE_EXCEPT\t1")

    # Empty except (pass on except)
    if isinstance(node, ast.ExceptHandler) and len(node.body) == 0:
        print(f"{filename}\tERROR_EMPTY_EXCEPT\t1")

    # Dividing by zero
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        if isinstance(node.right, ast.Constant) and node.right.value == 0:
            print(f"{filename}\tERROR_DIV_BY_ZERO\t1")

    # Useless "pass" block
    if isinstance(node, ast.Pass):
        print(f"{filename}\tERROR_USELESS_PASS\t1")

    # Unreachable code after the return statement of a function
    if isinstance(node, ast.FunctionDef):
        found_return = False
        for stmt in node.body:
            if isinstance(stmt, ast.Return):
                found_return = True
                continue
            if found_return:
                print(f"{filename}\tERROR_UNREACHABLE_CODE\t1")
                break

    # print() used for debugging
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        if node.func.id == "print":
            print(f"{filename}\tWARNING_PRINT_USED\t1")
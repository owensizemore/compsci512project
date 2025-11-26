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

# Walk through AST nodes
for node in ast.walk(tree):

    # Imports
    if isinstance(node, ast.Import):
        # import os
        for alias in node.names:
            print(f"{filename}\tIMPORT_{alias.name.upper()}\t1")

    if isinstance(node, ast.ImportFrom):
        # from math import sqrt
        module = node.module if node.module else "UNKNOWN_MODULE"
        for alias in node.names:
            print(f"{filename}\tIMPORT_FROM_{module.upper()}.{alias.name.upper()}\t1")

    # Operators
    if isinstance(node, ast.BinOp):
        # a + b, a - 1, a ** b, etc.
        op_type = type(node.op).__name__.upper()
        print(f"{filename}\tOPERATOR_{op_type}\t1")

    if isinstance(node, ast.BoolOp):
        # a and b, a or b, etc.
        op_type = type(node.op).__name__.upper()
        print(f"{filename}\tBOOLEAN_OP_{op_type}\t1")

    if isinstance(node, ast.UnaryOp):
        # not a, etc.
        op_type = type(node.op).__name__.upper()
        print(f"{filename}\tUNARY_OP_{op_type}\t1")

    if isinstance(node, ast.Compare):
        # ==, !=, >, <, etc.
        for op in node.ops:
            op_type = type(op).__name__.upper()
            print(f"{filename}\tCOMPARE_OP_{op_type}\t1")

    # Control structures
    if isinstance(node, ast.If):
        # if/else
        print(f"{filename}\tCONTROL_IF\t1")
        if node.orelse:
            print(f"{filename}\tCONTROL_ELSE\t1")
    if isinstance(node, ast.For):
        # for loop
        print(f"{filename}\tCONTROL_FOR\t1")
    if isinstance(node, ast.While):
        # while loop
        print(f"{filename}\tCONTROL_WHILE\t1")

    # Functions
    if isinstance(node, ast.FunctionDef):
        print(f"{filename}\tFUNCTION_DEF\t1")

    # Data structures
    if isinstance(node, ast.List):
        print(f"{filename}\tDATA_LIST\t1")
    if isinstance(node, ast.Dict):
        print(f"{filename}\tDATA_DICT\t1")
    if isinstance(node, ast.Set):
        print(f"{filename}\tDATA_SET\t1")

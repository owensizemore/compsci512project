#!/usr/bin/env python3
import sys
import ast
import os

filename = os.environ.get("map_input_file", "unknown")

# Read the entire file from STDIN
code = sys.stdin.read()

# Safely parse with AST
try:
    tree = ast.parse(code)
except SyntaxError:
    print(f"{filename}\tSYNTAX_ERROR\t1")
    sys.exit(0)

# Walk through AST nodes
for node in ast.walk(tree):

    # -------- IMPORTS --------
    if isinstance(node, ast.Import):
        # Each name in the import statement (e.g., import os, sys)
        for alias in node.names:
            print(f"{filename}\tIMPORT\t{alias.name}\t1")

    if isinstance(node, ast.ImportFrom):
        # e.g., from math import sqrt
        module = node.module if node.module else "UNKNOWN_MODULE"
        for alias in node.names:
            print(f"{filename}\tIMPORT_FROM\t{module}.{alias.name}\t1")

    # -------- OPERATORS --------
    if isinstance(node, ast.BinOp):
        op_type = type(node.op).__name__.upper()  # Add → ADD
        print(f"{filename}\tOPERATOR_{op_type}\t1")

    if isinstance(node, ast.BoolOp):
        op_type = type(node.op).__name__.upper()  # And → AND, Or → OR
        print(f"{filename}\tBOOLEAN_OP_{op_type}\t1")

    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op).__name__.upper()  # Not → NOT, UAdd → UADD
        print(f"{filename}\tUNARY_OP_{op_type}\t1")

    if isinstance(node, ast.Compare):
        # Comparison operations (==, !=, <, >, <=, >=, etc.)
        for op in node.ops:
            op_type = type(op).__name__.upper()  # Eq → EQ, Lt → LT, etc.
            print(f"{filename}\tCOMPARE_OP_{op_type}\t1")

    # -------- CONTROL STRUCTURES --------
    if isinstance(node, ast.If):
        print(f"{filename}\tCONTROL_IF\t1")
        if node.orelse:
            print(f"{filename}\tCONTROL_ELSE\t1")
    if isinstance(node, ast.For):
        print(f"{filename}\tCONTROL_FOR\t1")
    if isinstance(node, ast.While):
        print(f"{filename}\tCONTROL_WHILE\t1")

    # -------- FUNCTIONS --------
    if isinstance(node, ast.FunctionDef):
        print(f"{filename}\tFUNCTION_DEF\t1")

    # -------- DATA STRUCTURES --------
    if isinstance(node, ast.List):
        print(f"{filename}\tDATA_LIST\t1")
    if isinstance(node, ast.Dict):
        print(f"{filename}\tDATA_DICT\t1")
    if isinstance(node, ast.Set):
        print(f"{filename}\tDATA_SET\t1")

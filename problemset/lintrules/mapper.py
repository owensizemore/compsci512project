#!/usr/bin/env python3
import sys
import os
import subprocess
import tempfile

filename = os.environ.get("map_input_file", "unknown")

code = sys.stdin.read()

with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
    tmp.write(code)
    tmp_filename = tmp.name

FLAKE8_PATH = "/opt/conda/default/bin/flake8"

try:
    result = subprocess.run(
        [FLAKE8_PATH, tmp_filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
except Exception as e:
    print(f"{filename}\tLINT_ERROR_FLAKE8_FAILED\t{repr(e)}")
    sys.exit(0)

# Extract error code (F401, E302, etc.) from flake8 output
for line in result.stdout.splitlines():
    if not line.strip():
        continue
    try:
        # Split into filename, line, column, and message
        _, _, _, msg = line.split(":", 3)
        # Only the error code is relevant
        error_code = msg.strip().split()[0]
        print(f"{filename}\tLINT_{error_code}\t1")
    except Exception:
        print(f"{filename}\tLINT_UNKNOWN\t1")

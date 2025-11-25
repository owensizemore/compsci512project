import sys
import os

filename = os.environ.get("map_input_file", "unknown")

for _ in sys.stdin:
    print(f"{filename}\t1")



#!/usr/bin/env python3
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) != 3:
        continue

    filename, error_type, count_str = parts

    try:
        count = int(count_str)
    except ValueError:
        continue

    key = (filename, error_type)

    if current_key == key:
        current_count += count
    else:
        if current_key is not None:
            print(f"{current_key[0]}\t{current_key[1]}\t{current_count}")
        current_key = key
        current_count = count

if current_key is not None:
    print(f"{current_key[0]}\t{current_key[1]}\t{current_count}")

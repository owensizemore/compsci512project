import sys

current_file = None
count = 0

for line in sys.stdin:
    file, value = line.strip().split("\t")

    if current_file != file:
        if current_file is not None:
            print(f"{current_file}\t{count}")
        current_file = file
        count = 0

    count += int(value)

if current_file is not None:
    print(f"{current_file}\t{count}")



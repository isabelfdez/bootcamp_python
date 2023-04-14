import sys

kata = (19, 42, 3)

size = len(kata)
if (size == 0):
    print("Tuple is empty")
    sys.exit(0)

print(f"The {size} numbers are:", ", ".join(map(str, kata)))

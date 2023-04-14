import sys

if (len(sys.argv) != 3):
    print("Incorrect number of arguments")
    print("Usage: python operations.py <number1> <number2>")
    print("Example: python operations.py 10 3")
else:
    if (sys.argv[1].isdigit() == 0 or sys.argv[2].isdigit() == 0):
        print("Only integers are accepted as arguments")
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        sum = a + b
        print(f"{'Sum:':<15}{sum:>10}")
        diff = a - b
        print(f"{'Difference:':<15}{diff:>10}")
        prod = a * b
        print(f"{'Product:':<15}{prod:>10}")
        try:
            quot = a / b
            print(f"{'Quotient:':<15}{quot:>10}")
        except:
            print(f"{'Quotient:':<15}{'ERROR (division by zero)':>10}")
        try:
            mod = a % b
            print(f"{'Remainder:':<15}{mod:>10}")
        except:
            print(f"{'Remainder:':<15}{'ERROR (modulo by zero)':>10}")

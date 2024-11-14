# Assume input is x y z
    # x is integer
    # y is + - * or /
    # z is an integer

# Prompt user for input
x = float(input("First integer: "))
y = input("Basic operation: ")
z = float(input("Second integer: "))
    
if y == "+":
    calculator = x + z
elif y == "-":
    calculator = x - z
elif y == "*":
    calculator = x * z
elif y == "/":
    if z == 0:
        print("Error: Cannot divide by zero!")
        calculator = None
    else:
        calculator = x / z
else:
    print("Invalid operation! Please use +, -, *, or /.")
    calculator = None

# Output floating point value, 1 dp
if calculator is not None:
    print(f"{calculator:.1f}")
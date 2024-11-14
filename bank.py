# Prompts user for greeting, case insensitive, whitespace removed
greeting = input("Enter a greeting: ").lower().strip()

# If greeting hello, output 0
if greeting == "hello":
    print("$0")

# If greeting starts with h but not hello output 20
elif greeting.startswith("h"):
    print("$20")

# Otherwise output 100
else:
    print("$100")
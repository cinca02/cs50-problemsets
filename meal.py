import sys

# Prompts user for input if no command line input
def main():
    if len(sys.argv) == 2:
        time = sys.argv[1].strip()
    else:
        time = input("What time is it? ").strip()
    
    convert(time)

# Convert input str to float and determine meal time
def convert(n):

    hours, minutes = map(float, n.split(":"))
    time_in_hours = hours + minutes / 60.0


    if 7.0 <= time_in_hours <= 8.0:
        print("breakfast")
    elif 12.0 <= time_in_hours <= 13.0:
        print("lunch")
    elif 18.0 <= time_in_hours <= 19.0:
        print("dinner")
    else:
        return

# Runs main function
if __name__ == "__main__":
    main()
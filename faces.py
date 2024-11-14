# Takes input and defines smiley variables
def main():
    sentence = input("What do you want to say?")
    convert(sentence)


# Turns faces into correct emoji
def convert(to):
    smiling_face = "\U0001F642"
    frowning_face = "\U0001F641"
    to = to.replace(":)", smiling_face )
    to = to.replace(":(", frowning_face)
    print("Your new sentence is: ''", to, "''")

# Prints output
main()
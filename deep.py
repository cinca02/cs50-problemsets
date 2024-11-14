def main():
    x = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    great_answer(x)

def great_answer(n):
    if n in ("42", "forty-two", "forty two"):
        print ("Yes")
    else:
        print ("No")
    


main()

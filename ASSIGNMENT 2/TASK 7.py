def pal_checker(word):
    new_string = ""

    if " " in word:
        for i in word:
            if i == " ":
                continue
            else:
                new_string += i
    else:

        new_string = word

    reversed_word = new_string[::-1]

    if new_string == reversed_word:
        print("Palindrome")
    else:
        print("Not a palindrome")


pal_checker(input("Sir,Please enter the word: "))

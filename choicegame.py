

from random import choice

word = choice(["code","club"])

guessed = []
while True:

    out =""

    for letter in word:
        if letter in guessed:
            out = out +letter
        else:
            out = out + "_"

    if out == word:
        print ("you guessed",word)
        break

    print ("you guessed",out)
    guess = input()

    if guess in guessed:
        print ("already guessed",word)
    elif guess in word:
        print ("yay")
        guessed.append(guess)

    else:
        print ("no")

    

   
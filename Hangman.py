import random

# choose the random word from the given list
def ChooseRandomWord():
    listOfWords=["APPLE", "BILBO", "CHORUSED", "DISIMAGINE", "ENSURING", "FORMALISING", "GLITCHES", "HARMINE", "INDENTATION", 
                "JACKED", "KALPACS", "LAUNDRY", "MASKED", "NETTED", "OXFORD", "PARODY", "QUOTIENTS", "RACERS", "SADNESS", 
                "THYREOID", "UNDUE", "VENT", "WEDGED", "XERIC", "YOUTHHOOD", "ZIFFS"]

    choice=listOfWords[random.randint(0,len(listOfWords)-1)]
    return choice

print("Welcome to Hangman!")
endGame="yes"
while endGame =="yes":
    secretWord=ChooseRandomWord()           # call the chooseRandomWord() and get a word 
    dashes=list(secretWord)
    displayList=[]
    for i in dashes:
        # add the dash to the display list to show on screen
        displayList.append("_")
    # count the length of secret word 
    count=len(secretWord)
    guesses=0
    letter = 0
    usedList=[]     # list for used words
    
    # continue on loop while secret word guessed completly
    while count != 0 and letter!="exit":
        print(" ".join(displayList))
        letter=input("Guess your letter: ")

        if letter.upper() in usedList:
            print("Oops! Already guessed that letter.")
        else:
            for i in range(0,len(secretWord)):
                if letter.upper() == secretWord[i]:
                    displayList[i]=letter.upper()
                    count -= 1
            guesses +=1
        usedList.append(letter.upper())     # add the letter used for guesing in list
    if letter =="exit":
        print("Thanks!")
    else:
        print(" ".join(displayList))
        print("Good job! You figured that the word is "+secretWord+" after guessing %s letters!" % guesses)
        endGame=str(input("Want to play again? Press 'yes' or 'no' :"))





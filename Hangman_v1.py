from random import choice

def drawMan(num):
    if num == 6:
        print("_______")
        print("|     |")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
    if num == 5:
        print("_______")
        print("|     |")
        print("|     0")
        print("|      ")
        print("|      ")
        print("|      ")
    elif num == 4:
        print("_______")
        print("|     |")
        print("|     0")
        print("|     |")
        print("|      ")
        print("|      ")
    elif num == 3:
        print("_______")
        print("|     |")
        print("|     0")
        print("|    /|")
        print("|      ")
        print("|      ")
    elif num == 2:
        print("_______")
        print("|     |")
        print("|     0")
        print("|    /|\\")
        print("|      ")
        print("|      ")
    elif num == 1:
        print("_______")
        print("|     |")
        print("|     0")
        print("|    /|\\")
        print("|    /")
        print("|      ")
    elif num == 0:
        print("_______")
        print("|     |")
        print("|     0")
        print("|    /|\\")
        print("|    / \\")
        print("|      ")

def setup():
    global word, lives, win, guesses
    win = False
    wordList = []
    guesses = []
    wordsFile = open("Words.txt", "r")
    for line in wordsFile:
        wordList.append(line)
    for i in range(len(wordList)):
        if "\n" in wordList[i]:
            wordList[i] = wordList[i].replace("\n", "")
    word = choice(wordList)
    lives = 6
    wordsFile.close()
    print("Welcome to Hangman v1.0. Your job is to guess the word I choose without losing all your lives and hanging the man.")
    print("The theme of today's words is: Instruments. Good luck!")

def hint():
    hints = {"guitar": "Pretty much every country singer knows how to play this.",
             "piano": "Arguably the most well known classical instrument.",
             "ukelele" : "The guitar's little cousin. It's tropical.",
             "saxophone": "It sounds really saxy.",
             "xylophone": "The toy versions of these usually have colorful keys.",
             "keytar": "This one is a fusion of two other instruments.",
             "banjo": "Think guitar, but circle.",
             "accordian": "If you're a one man band, you probably have this.",
             "drum": "Badum tsssssss.",
             "flute": "A much more elegant recorder.",
             "piccolo": "It's also the name of a character on Dragon Ball Z.",
             "recorder": "A really cheap instrument a lot of elementary school students 'learn' to play.",
             "triangle": "Also a shape.",
             "violin": "You play this with a bow.",
             "harp": "It's pretty huge and has strings.",
             "gong": "Round 1: Fight!"}
    print("\nHint: " + hints[word])


play = True
usedWords = []

while(play):
    setup()
    while(word in usedWords):
        setup()
    usedWords.append(word)
    blanks = ["_" for i in range(len(word))]
    while(lives != 0 and (not win)):
        drawMan(lives)
        for i in range(len(blanks)):
            print(blanks[i], end=" ")
        if lives < 4:
            hint()
        if (guesses):
            print("\nGuesses: ", end="")
            for guess in guesses:
                print(guess + " ", end= "")
            print("\n")
        if word == "".join(blanks):
            print("You win!")
            win = True
            playerGuess = input("Would you like to play again? Enter Y or N: ").lower()
            while((not playerGuess.isalpha()) or (playerGuess != "y" and playerGuess != "n")):
                playerGuess = input("Would you like to play again? Enter Y or N: ").lower()
            if(playerGuess == "n"):
                play = False
            break
        playerGuess = input("Guess a letter please: ").lower()
        while(not playerGuess.isalpha() or playerGuess in guesses):
            playerGuess = input("Your input is invalid. Try again.").lower()
        guesses.append(playerGuess)
        if playerGuess in word:
            print("Nice, you guessed right.")
            for i in range(len(word)):
                if playerGuess == word[i]:
                    blanks[i] = playerGuess
        else:
            print("Sorry, you guessed wrong.")
            lives -= 1
        if lives == 0:
            print("You lost...")
            playerGuess = input("Would you like to play again? Enter Y or N: ").lower()
            while((not playerGuess.isalpha()) or (playerGuess != "y" and playerGuess != "n")):
                playerGuess = input("Would you like to play again? Enter Y or N: ").lower()
            if(playerGuess == "n"):
                play = False
            break
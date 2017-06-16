# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    n = 0
    for i in secretWord:
        if i in lettersGuessed:
            n += 1
    if n == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    res = []
    for i in secretWord:
        if i in lettersGuessed:
            res.append(i)
        else:
            res.append('_')       
    strres = ' '.join(res)
    return strres
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letters = string.ascii_lowercase
    letterlist = []
    for i in letters:
        letterlist.append(i)
    for j in lettersGuessed:
        letterlist.remove(j)
    res = ''.join(letterlist)
    return res
    

def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+ str(len(secretWord)) + " letters long")
    print("-------------")
    n = 8
    lettersGuessed = []
    while n > 0:
        available = []
        available = getAvailableLetters(lettersGuessed)
        print("You have " + str(n) + " guesses left.")
        print("Available letters: "+ available)
        letter = input("Please guess a letter: ")
        lettersGuessed.append(letter)
        output = getGuessedWord(secretWord, lettersGuessed)
        flag = True
        if len(lettersGuessed)>len(letter) and not isWordGuessed(secretWord, lettersGuessed) :
            if letter in lettersGuessed[0:]:
                print("Oops! You've already guessed that letter: " + output)
                flag = False
        if letter in secretWord and flag:
            print("Good guess: " + output) 
        elif letter not in secretWord and flag:
            print("Oops! That letter is not in my word: " + output)
            n -= 1
        print("-------------")
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
    print("Sorry, you ran out of guesses. The word was " + secretWord + ".")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

# Problem Set 2
# Name: Navinder kour
# time spent = 8 hours
# Hangman game
from os import error
import random

WORDLIST_FILENAME = "D:\PythonProblemSolvingCodeSubmission\words.txt"

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
    
    return random.choice(wordlist)


wordlist = loadWords()

def WordGuessed(randomWord, guessedWord):

    a=0
    for i in guessedWord:
        if i in randomWord:
            a+=1
    if a==len(randomWord):
        return True
    else:
        return False


def GuessedTheWord(randomWord, guessedWord):
    
    b=[]
    for i in randomWord:
        if i in guessedWord:
            b.append(i)
    ans=''
    for i in randomWord:
        if i in b:
            ans+=i
        else:
            ans+='_ '
    return ans



def availableword(guessedWord):
    
    import string
    ans=list(string.ascii_lowercase)
    for i in guessedWord:
        ans.remove(i)
    return ''.join(ans)

def hangman(randomWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(randomWord),"letters long.")
    
    global lettersGuessed
    error=0
    guessedWord=[]
    
    while 8 - error > 0:
        
        if WordGuessed(randomWord, guessedWord):
            print("-------------")
            print("Congratulations, you won!")
            break
            
        else:
            print("-------------")
            print("You have",8-error,"guesses left.")
            print("Available letters:",availableword(guessedWord))
            guess=str(input("Please guess a letter: ")).lower()
            
            if guess in guessedWord:
                print("Oops! You've already guessed that letter:",GuessedTheWord(randomWord,guessedWord))
                
            elif guess in randomWord and guess not in guessedWord:
                guessedWord.append(guess)
                print("Good guess:",GuessedTheWord(randomWord,guessedWord))
                
            else:
                guessedWord.append(guess)
                error += 1
                print("Oops! that letter is not in my word:",GuessedTheWord(randomWord,guessedWord))
                
        if 8 - error == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.",randomWord)
            break
        
        else:
            continue


randomWord = chooseWord(wordlist).lower()
hangman(randomWord)
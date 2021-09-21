# Problem Set 2
# Name: Navinder kour
# time spent = 2 days
# Hangman game
import random

WORDLIST_FILENAME = "D:\PythonProblemSolvingCodeSubmission\words.txt"

def loadWords():
    """a
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

# -----------------------------------
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):

    c=0
    for i in lettersGuessed:
        if i in secretWord:
            c+=1
    if c==len(secretWord):
        return True
    else:
        return False


def GuessedLetter(secretWord, lettersGuessed):
    
    s=[]
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans=''
    for i in secretWord:
        if i in s:
            ans+=i
        else:
            ans+='_ '
    return ans



def availableLetters(lettersGuessed):
    
    import string
    ans=list(string.ascii_lowercase)
    for i in lettersGuessed:
        ans.remove(i)
    return ''.join(ans)

def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long.")
    
    global lettersGuessed
    mistakeMade=0
    lettersGuessed=[]
    
    while 8 - mistakeMade > 0:
        
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break
            
        else:
            print("-------------")
            print("You have",8-mistakeMade,"guesses left.")
            print("Available letters:",availableLetters(lettersGuessed))
            guess=str(input("Please guess a letter: ")).lower()
            
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter:",GuessedLetter(secretWord,lettersGuessed))
                
            elif guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Good guess:",GuessedLetter(secretWord,lettersGuessed))
                
            else:
                lettersGuessed.append(guess)
                mistakeMade += 1
                print("Oops! that letter is not in my word:",GuessedLetter(secretWord,lettersGuessed))
                
        if 8 - mistakeMade == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.",secretWord)
            break
        
        else:
            continue


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
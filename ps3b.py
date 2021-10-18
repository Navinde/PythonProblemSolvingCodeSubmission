from ps3a import *
import time
from perm import *

#
#
# Problem #6A: Computer chooses a word
#
#

def comp_get_valid_words_with_scores(hand, word_list):
    """
    Given a hand and a word_list, returns a list of valid words
        sorted in descending order according to their word scores
    
    return list ( tuple (int,string) ) sorted according to int,
        or None if no valid words are found

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...

    length = 0
    for i in hand:
        length += i

    word_choices = []
 
    for perm in word_list:
        word_choices.append(perm)

def comp_choose_word(hand, word_list):
    """
    Given a hand and a word_list, find a valid word, and return it.
    This word should be calculated by considering all possible permutations
    of lengths 1 to hand length.
    
    Hint: First try to make a legal player, and then worry about making
    the computer player better (if you have time). 

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...

    computer_word = ''
    word_choices = []
    length=0
    for i in hand:
            length += i


    for word in word_choices:
        score = get_word_score(word, length)
        if score > get_word_score(computer_word, length):
            computer_word = word

    return computer_word


#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO...
    
    score = 0
    length = calculate_handlen(hand)

    while comp_choose_word(hand, word_list) != '':
        computer_word = comp_choose_word(hand, word_list)
        score_word = get_word_score(computer_word, length)
        score += score_word

        print ('Total Score: %d' % (score))

    print ('Run out of letters. Total score: %s points.' % (score))
    
#
# Problem #6C: Playing a game
#
#

def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...

    n= HAND_SIZE
    hand = {}

    while True: 
        game = input('Enter n to deal a new hand, r to replay the last hand,c to computer,u to use the game or e to end game:')
        if game == 'r':
            play_hand(hand, word_list, n)   
        elif game == 'n':
            hand = deal_hand(n)
            play_hand(hand, word_list, n)
        elif game =='u':
             play_hand(hand, word_list, n)
        elif game =='c':
            comp_play_hand(hand, word_list)
        elif game == 'e':
            break
        else:
            print ('Invalid command.')

            # computer_game = input('Enter u to play a new game, or c to have the computer play a game,or e to end game : ')
            # if computer_game == 'u':
            #     play_hand(hand, word_list, n)
            # elif computer_game == 'c':
            #     comp_play_hand(hand, word_list)
            # elif computer_game =='e':
            #     break
            # else:
            #  print ('Invalid command.')



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

# shows error in c computer play and u use play 
# only n,r and e is working 

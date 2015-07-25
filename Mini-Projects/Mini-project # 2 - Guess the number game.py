# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# set the default range to 0-100
range = 100


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print ""
    
    global secret_number
    global remain_guess
    
    if range == 100:
        secret_number = random.randrange(0,100)
        print "New game! Range is from 0 to 100"
        remain_guess = 7
        
    elif range == 1000:
        secret_number = random.randrange(0,1000)
        print "New game! Range is from 0 to 1000"        
        remain_guess = 10
        
    print "Number of remaining guesses is", remain_guess        
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print ""
    global range
    range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print ""
    global range
    range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    print ""

    guess = int(guess)
    print "Guess was", guess
        
    # the remaining guesses in a game    
    global remain_guess
    remain_guess -= 1
    print "Number of remaining guesses is", remain_guess
    
    # the guess is correct
    if guess == secret_number:
        print "Correct!"
        new_game()
        return

    # run out of guesses
    if remain_guess == 0:
        print "You ran out of guesses.  The number was", secret_number
        new_game()
        return  
    
    # the guess is not correct
    if guess > secret_number:
        print "Lower!"
    else:
        print "Higher!"
    
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range:0-100", range100, 200)
frame.add_button("Range:0-1000", range1000, 200)
frame.add_input("", input_guess, 200)
frame.start()

# call new_game 
new_game()


# CodeSkulptor URL: http://www.codeskulptor.org/#user40_zK8o7hZjMu_1.py
# Template: http://www.codeskulptor.org/#examples-guess_the_number_template.py

# by XingYi Xie (ilquv2@gmail.com), 2015.Jun.13
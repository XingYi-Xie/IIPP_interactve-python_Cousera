# implementation of card game - Memory

import simplegui
import random

CARD_WIDTH = 100
CARD_HEIGHT = 100
CANVAS_WIDTH = CARD_WIDTH * 4
CANVAS_HEIGHT = CARD_HEIGHT * 4
IMAGE_WIDTH = 635 / 4
IMAGE_HEIGHT = 321 / 2

image = simplegui.load_image("http://fc.sharewa.com/upload_file/7/content/dd6c8335-53f3-cd06-7d8a-04eec57cdc49.jpg")
card_num = range(8) * 2

# helper function to initialize globals
def new_game():
    global card_num, exposed, state, turns
    random.shuffle(card_num)
    exposed = [False] * 16
    # "state" is card(s) exposed but not matched or checked, 
    # as suggested in the video   
    state = 0
    turns = 0
    label.set_text("Turns = 0")
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, turns, card1_index, card2_index
    
    selected_index = 4 * (pos[1] // CARD_HEIGHT) + pos[0] // CARD_WIDTH

    if exposed[selected_index] == False:
        exposed[selected_index] = True 

        if state == 0:
            state = 1
            card1_index = selected_index
        elif state == 1:
            state = 2
            card2_index = selected_index
            turns += 1
            label.set_text("Turns =" + str(turns))
        else:
            if card_num[card1_index] != card_num[card2_index]:
                exposed[card1_index] = False            
                exposed[card2_index] = False
            state = 1
            card1_index = selected_index            

# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(16):
        if exposed[card_index]:
             canvas.draw_image(image, [IMAGE_WIDTH * (card_num[card_index] % 4 + 0.5) , IMAGE_HEIGHT * (card_num[card_index] // 4 + 0.5)], [IMAGE_WIDTH, IMAGE_HEIGHT], [CARD_WIDTH * (card_index % 4 + 0.5), CARD_HEIGHT * (card_index // 4 + 0.5)], [CARD_WIDTH, CARD_HEIGHT])
        else:
             canvas.draw_text("?", [CARD_WIDTH * (card_index % 4 + 0.4), CARD_HEIGHT * (card_index // 4 + 0.7)], CARD_WIDTH * 0.6, "White")

    # draw grids (lines)
    for i in range(1,4):
        canvas.draw_line([0, CARD_HEIGHT * i], [CANVAS_WIDTH, CARD_HEIGHT * i], 1, "White")
        canvas.draw_line([CARD_WIDTH * i, 0], [CARD_WIDTH * i, CANVAS_HEIGHT], 1, "White")
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# CodeSkulptor URL: http://www.codeskulptor.org/#user40_iXhMGTh3hW_6.py
# Template: http://www.codeskulptor.org/#examples-memory_template.py

# by XingYi Xie ( ilquv2@gmail.com )
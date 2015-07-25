# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_vel = 0
paddle2_vel = 0
paused = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    ball_vel = [0, 0]
    ball_vel[1] = - random.randrange(60, 180) / 60.0    
    if direction == True:
        ball_vel[0] = random.randrange(120, 240) / 60.0
    else:
        ball_vel[0] = - random.randrange(120, 240) / 60.0        
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    # the center point on the top of each paddle
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT]
    
    score1 = 0
    score2 = 0
    
    spawn_ball(random.choice([LEFT, RIGHT]))
        

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if paused == False:
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
    
    # collision and reflection with top and bottom walls
    if ball_pos[1] <= BALL_RADIUS or  ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if paused == False:
        paddle1_pos[1] += paddle1_vel
        paddle2_pos[1] += paddle2_vel

    # restrict paddles in canvas
    if paddle1_pos[1] < 0:
        paddle1_pos[1] = 0
    if paddle1_pos[1] > HEIGHT - PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - PAD_HEIGHT
    if paddle2_pos[1] < 0:
        paddle2_pos[1] = 0
    if paddle2_pos[1] > HEIGHT - PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - PAD_HEIGHT        
    
    # draw paddles
    canvas.draw_line(paddle1_pos, [paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line(paddle2_pos, [paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT], PAD_WIDTH, "White")
        
    # determine whether paddle and ball collide
        # the left paddle
    if ball_pos[0] - BALL_RADIUS <= paddle1_pos[0]:
        if ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[1] + PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
            
        # the right paddle
    if ball_pos[0] + BALL_RADIUS >= paddle2_pos[0]:
        if ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[1] + PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH * (0.25 - 0.03*len(str(score1))), WIDTH * 0.12], WIDTH * 0.1, "White", "sans-serif")
    canvas.draw_text(str(score2), [WIDTH * (0.76 - 0.03*len(str(score2))), WIDTH * 0.12], WIDTH * 0.1, "White", "sans-serif")
    
    # draw "Game Paused!"
    if paused == True:
        canvas.draw_text("PAUSED!", [WIDTH * 0.3, HEIGHT * 0.5], WIDTH * 0.1, "Silver", "sans-serif")
        canvas.draw_text('Press Space key to resume.', [WIDTH * 0.14, HEIGHT * 0.6], WIDTH * 0.06, "Silver", "sans-serif")


def keydown(key):
    global paddle1_vel, paddle2_vel
    global paused
    
    if key == simplegui.KEY_MAP["space"]:
        paused = not paused
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -7
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 7
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -7
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 7      
        
    
def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["w"] or  key == simplegui.KEY_MAP["s"] :
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)

frame.add_label('Click "Restart" to start a new game and clear scores.', 200)
frame.add_label('Key Controls:', 200)
frame.add_label('Player 1 (Left): W / S', 200)
frame.add_label('Player 2 (Right): Up / Down', 200)
frame.add_label('Pause / Resume: Space', 200)

# start frame
new_game()
frame.start()


# CodeSkulptor URL: http://www.codeskulptor.org/#user40_sLEgbNF61oTBjTq_3.py
# Template: http://www.codeskulptor.org/#examples-pong_template.py

# by XingYi Xie (ilquv2@gmail.com) --2015.Jun.25
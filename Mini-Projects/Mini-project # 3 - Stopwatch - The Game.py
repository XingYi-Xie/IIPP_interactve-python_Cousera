# template for "Stopwatch: The Game"

import simplegui

# define global variables

time_in_tenths_of_seconds = 0
attempts = 0
success = 0
timer_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    minutes = str(t // 600)
    time_left = t % 600

    seconds = time_left // 10
    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)

    tenths_of_seconds = str(time_left % 10)
    return minutes + ":" + seconds + "." + tenths_of_seconds

    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_timer():
    """
    The event handler for Start button
    """
    timer.start()

    global timer_running
    timer_running = True
    

def stop_timer():
    """
    The event handler for Stop button
    It stops the timer and count for the attempts to stop the watch,
    and the number of success in stopping at whole seconds
    """
    
#    if timer.is_running():
# For the accuracy of the game, I'll stop the timer as soon as possible
# So I use a global Boolean variable instead of timer.is_running
    timer.stop()
    
    global attempts
    global success
    global timer_running

# check if the time is running, 
# so it will not increase the point incorrectly
    if timer_running == True:
        attempts += 1
        timer_running = False
        if time_in_tenths_of_seconds % 10 == 0:
             success +=1


def reset_timer():
    """
    The event handler for Reset button
    It stop the timer and reset all global variables to initial states
    """
    global time_in_tenths_of_seconds
    global attempts
    global success
    global timer_running

    timer.stop()

    time_in_tenths_of_seconds = 0
    attempts = 0
    success = 0
    timer_running = False


# define event handler for timer with 0.1 sec interval

def tick():
    global time_in_tenths_of_seconds
    time_in_tenths_of_seconds += 1

# define draw handler

def draw(canvas):
    canvas.draw_text(format(time_in_tenths_of_seconds), (75,130), 64, "White")
    canvas.draw_text(str(success) + " / " + str(attempts), (210,40), 40, "Green")
    
# create frame
frame = simplegui.create_frame("the Stopwatch Game", 300, 200)

# register event handlers
frame.add_button("Start", start_timer, 200)
frame.add_button("Stop", stop_timer, 200)
frame.add_button("Reset", reset_timer, 200)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)

# start frame
frame.start()

# CodeSkulptor URL: http://www.codeskulptor.org/#user40_FJnCfZCCIy_4.py
# Template: http://www.codeskulptor.org/#examples-stopwatch_template.py

# by XingYi Xie (ilquv2@gmail.com) --2015.Jun.19


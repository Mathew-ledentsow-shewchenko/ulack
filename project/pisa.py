from tkinter import *

import random

WIDTH = 900
HEIGHT = 300



PAD_W = 10

PAD_H = 100

BALL_SPEED_UP = 1.05

BALL_MAX_SPEED = 40

BALL_RADIUS = 30

INITIAL_SPEED = 20
BALL_X_SPEED = INITIAL_SPEED
BALL_Y_SPEED = INITIAL_SPEED


PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0



right_line_distance = WIDTH - PAD_W

def update_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
        canvas.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        PLAYER_2_SCORE += 1
        canvas.itemconfig(p_2_text, text=PLAYER_2_SCORE)

def spawn_ball():
    global BALL_X_SPEED

    canvas.coords(BALL, WIDTH/2-BALL_RADIUS/2,
             HEIGHT/2-BALL_RADIUS/2,
             WIDTH/2+BALL_RADIUS/2,
             HEIGHT/2+BALL_RADIUS/2)


    BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED) / abs(BALL_X_SPEED)


def bounce(action):
    global BALL_X_SPEED, BALL_Y_SPEED

    if action == "strike":
        BALL_Y_SPEED = random.randrange(-10, 10)
        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
            BALL_X_SPEED *= -BALL_SPEED_UP
        else:
            BALL_X_SPEED = -BALL_X_SPEED
    else:
        BALL_Y_SPEED = -BALL_Y_SPEED


window = Tk()
window.title("Pong")


canvas = Canvas(window, width=WIDTH, height=HEIGHT, background="black")
canvas.pack()



canvas.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")

canvas.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill="white")

canvas.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill="white")





BALL = canvas.create_oval(WIDTH/2-BALL_RADIUS/2,
                     HEIGHT/2-BALL_RADIUS/2,
                     WIDTH/2+BALL_RADIUS/2,
                     HEIGHT/2+BALL_RADIUS/2, fill="white")


LEFT_PAD = canvas.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill="white")


RIGHT_PAD = canvas.create_line(WIDTH-PAD_W/2, 0, WIDTH-PAD_W/2,
                          PAD_H, width=PAD_W, fill="white")


p_1_text = canvas.create_text(WIDTH-WIDTH/6, PAD_H/4,
                         text=PLAYER_1_SCORE,
                         font="Arial 20",
                         fill="white")

p_2_text = canvas.create_text(WIDTH/6, PAD_H/4,
                          text=PLAYER_2_SCORE,
                          font="Arial 20",
                          fill="white")



BALL_X_CHANGE = 20

BALL_Y_CHANGE = 0

def move_ball():

    ball_left, ball_top, ball_right, ball_bot = canvas.coords(BALL)
    ball_center = (ball_top + ball_bot) / 2



    if ball_right + BALL_X_SPEED < right_line_distance and \
            ball_left + BALL_X_SPEED > PAD_W:
        canvas.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)

    elif ball_right == right_line_distance or ball_left == PAD_W:

        if ball_right > WIDTH / 2:



            if canvas.coords(RIGHT_PAD)[1] < ball_center < canvas.coords(RIGHT_PAD)[3]:
                bounce("strike")
            else:

                update_score("left")
                spawn_ball()
        else:

            if canvas.coords(LEFT_PAD)[1] < ball_center < canvas.coords(LEFT_PAD)[3]:
                bounce("strike")
            else:
                update_score("right")
                spawn_ball()


    else:
        if ball_right > WIDTH / 2:
            canvas.move(BALL, right_line_distance-ball_right, BALL_Y_SPEED)
        else:
            canvas.move(BALL, -ball_left+PAD_W, BALL_Y_SPEED)

    if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
        bounce("ricochet")



PAD_SPEED = 20

LEFT_PAD_SPEED = 0

RIGHT_PAD_SPEED = 0


def move_pads():

    PADS = {LEFT_PAD: LEFT_PAD_SPEED,
            RIGHT_PAD: RIGHT_PAD_SPEED}

    for pad in PADS:

        canvas.move(pad, 0, PADS[pad])

        if canvas.coords(pad)[1] < 0:
            canvas.move(pad, 0, -canvas.coords(pad)[1])
        elif canvas.coords(pad)[3] > HEIGHT:
            canvas.move(pad, 0, HEIGHT - canvas.coords(pad)[3])


def main():
    move_ball()
    move_pads()

    window.after(30, main)


canvas.focus_set()


def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED


canvas.bind("<KeyPress>", movement_handler)


def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0


canvas.bind("<KeyRelease>", stop_pad)


main()


window.mainloop()
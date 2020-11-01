from tkinter import *
from winsound import *
from random import *
window = Tk()
#def func1():
    #PlaySound("papaka/EpicSaxGuy.wav", SND_FILENAME)

#button = Button(window, text="Turn on music", command=func1)

WIDTH = 1000
HEIGHT = 550

PWid = 50
PHei = 50

Ball_Speed_Up = 1.05
Ball_Max_Speed = 40
Ball_Radius = 30

Initial_Speed = 20
Ball_X_Speed = Initial_Speed
Ball_Y_Speed = Initial_Speed

PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

right_line_distance = WIDTH - PWid
def spawn_ball():
    global BALL_X_SPEED

    canvas.coords(BALL, WIDTH/2-Ball_Radius/2,
             HEIGHT/2-Ball_Radius/2,
             WIDTH/2+Ball_Radius/2,
             HEIGHT/2+Ball_Radius/2)
    BALL_X_SPEED = -(BALL_X_SPEED * -Initial_Speed) / abs(BALL_X_SPEED)


canvas = Canvas(window, width=WIDTH, height=HEIGHT, background="white")
canvas.pack()
vertical_up_left_line = canvas.create_rectangle(30,30,20,200, fill = "blue")
vertical_down_left_line = canvas.create_rectangle(30,350,20,520,fill = "blue")
horizotlal_up_line = canvas.create_rectangle(950,20,30,30, fill = "black")
horizotlal_down_line = canvas.create_rectangle(950,520,30,530, fill = "black")
vertical_up_left_line = canvas.create_rectangle(950,30,960,200, fill = "red")
vertical_down_right_line = canvas.create_rectangle(950,520,960,350, fill = "red")

BALL = canvas.create_oval(WIDTH/2-Ball_Radius/2,
                     HEIGHT/2-Ball_Radius/2,
                     WIDTH/2+Ball_Radius/2,
                     HEIGHT/2+Ball_Radius/2, fill="black")
p_1_text = canvas.create_text(WIDTH - WIDTH / 6, PHei / 4,
                         text=PLAYER_1_SCORE,
                         font="Arial 15",
                         fill="black")

p_2_text = canvas.create_text(WIDTH / 6, PHei / 4,
                         text=PLAYER_2_SCORE,
                         font="Arial 15",
                         fill="black")
LEFT_PAD = canvas.create_line(PWid/2, PHei/2, PWid/2,PHei, width=PWid, fill="blue")
RIGHT_PAD = canvas.create_line(WIDTH-PWid/2, PHei/2, WIDTH-PWid/2,
                          PHei, width=PWid, fill="red")




PAD_SPEED = 20

LEFT_PAD_SPEED = 0

RIGHT_PAD_SPEED = 0

canvas.focus_set()







window.mainloop()
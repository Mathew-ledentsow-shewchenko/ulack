from tkinter import Tk, Canvas
import random


WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True

def create_block():
    global BLOCK
    posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE)
    BLOCK = canvas.create_oval(posx, posy,
                          posx+SEG_SIZE, posy+SEG_SIZE,
                          fill="red")


def main():
    global IN_GAME
    if IN_GAME:
        s.move()
        head_coords = canvas.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
        elif head_coords == canvas.coords(BLOCK):
            s.add_segment()
            canvas.delete(BLOCK)
            create_block()
        else:
            for index in range(len(s.segments)-1):
                if head_coords == canvas.coords(s.segments[index].instance):
                    IN_GAME = False
        window.after(100, main)
    else:
        set_state(restart_text, 'normal')
        set_state(game_over_text, 'normal')


class Segment(object):

    def __init__(self, x, y):
        self.instance = canvas.create_rectangle(x, y,
                                           x+SEG_SIZE, y+SEG_SIZE,
                                           fill="black")


class Snake(object):
    """ Simple Snake class """
    def __init__(self, segments):
        self.segments = segments
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        self.vector = self.mapping["Right"]

    def move(self):
        """ Moves the snake with the specified vector"""
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = canvas.coords(self.segments[index+1].instance)
            canvas.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = canvas.coords(self.segments[-2].instance)
        canvas.coords(self.segments[-1].instance,
                 x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
                 x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)

    def add_segment(self):
        """ Adds segment to the snake """
        last_seg = canvas.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
        """ Changes direction of snake """
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

    def reset_snake(self):
        for segment in self.segments:
            canvas.delete(segment.instance)


def set_state(item, state):
    canvas.itemconfigure(item, state=state)


def clicked(event):
    global IN_GAME
    s.reset_snake()
    IN_GAME = True
    canvas.delete(BLOCK)
    canvas.itemconfigure(restart_text, state='hidden')
    canvas.itemconfigure(game_over_text, state='hidden')
    start_game()


def start_game():
    global s
    create_block()
    s = create_snake()
    canvas.bind("<KeyPress>", s.change_direction)
    main()


def create_snake():

    segments = [Segment(SEG_SIZE, SEG_SIZE),
                Segment(SEG_SIZE*2, SEG_SIZE),
                Segment(SEG_SIZE*3, SEG_SIZE)]
    return Snake(segments)



window = Tk()
window.title("Snake")


canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
canvas.grid()
canvas.focus_set()
start_game()
window.mainloop()
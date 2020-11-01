from tkinter import *
from winsound import *
window = Tk()
def func1():
    PlaySound("papaka/anhem_x.wav", SND_FILENAME)

button = Button(window, text="123", command=func1)
button.pack(padx=50, pady=50)
canvas = Canvas(window, width=1000, height=550, bg="white")
canvas.pack()
vertical_up_left_line = canvas.create_rectangle(30,30,20,200, fill = "blue")
vertical_down_left_line = canvas.create_rectangle(30,350,20,520,fill = "blue")
horizotlal_up_line = canvas.create_rectangle(950,20,30,30, fill = "black")
horizotlal_down_line = canvas.create_rectangle(950,520,30,530, fill = "black")
vertical_up_left_line = canvas.create_rectangle(950,30,960,200, fill = "red")
vertical_down_right_line = canvas.create_rectangle(950,520,960,350, fill = "red")
#middle_line = canvas.create_rectangle(450,20,450,350, fill = "black")
window.mainloop()
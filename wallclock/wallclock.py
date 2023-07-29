#
# Author: Alfonso Zepeda
# Created: 28 - July - 2023
#
# Wall Clock GUI
#
# Wall clock created with tkinter, it reads system time and refreshes the gui
#
# (c) GPL-3.0 license
#
# Original code from: https://www.instagram.com/p/Cu80rQlL6TM/
# 

# Import Tkinter library
import tkinter as tk

# Import time to read the system hour
import time

# Import math, to get PI value, SIN and COS operations
import math

# Global variables WIDTH and HEIGHT to create GUI
WIDTH = 400
HEIGHT = 400

# Initialize the window
window = tk.Tk()
# Add Title to window
window.title("Wall Clock")
# Declares size and color for canvas
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
# Add canvas to GUI
canvas.pack()


def update_clock():
    
    canvas.delete("all")
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec

# Draw Clock face
    canvas.create_oval(2, 2, WIDTH, HEIGHT, outline="black", width=2)

# Draw hour numbers
    for i in range(12):
        angle = i * math.pi / 6 - math.pi/2
        x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(angle)
        y = HEIGHT/2 + 0.7 * HEIGHT/2 * math.sin(angle)
        if i == 0:
            canvas.create_text(x, y-10, text=str(i+12), font=("Helvetica",12))
        else:
            canvas.create_text(x,y, text=str(i), font=("helvetica",12))

# Draw minute lines
    for i in range(60):
        angle = i * math.pi/30-math.pi/2
        x1 = WIDTH/2 + 0.8*WIDTH/2*math.cos(angle)
        y1 = HEIGHT/2 + 0.8*HEIGHT/2*math.sin(angle)
        x2 = WIDTH/2 + 0.9*WIDTH/2 * math.cos(angle)
        y2 = HEIGHT/2 + 0.9*HEIGHT/2 * math.sin(angle)

        if i% 5 == 0:
            canvas.create_line(x1,y1,x2,y2, fill="black", width=3)
        else:
            canvas.create_line(x1,y1,x2,y2, fill="black", width=1)

# Draw hour hand
    hour_angle=(hour+minute/60)*math.pi/6-math.pi/2
    hour_x = WIDTH/2 + 0.5*WIDTH/2 * math.cos(hour_angle)
    hour_y = HEIGHT/2 + 0.5*HEIGHT/2 * math.sin(hour_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, hour_x, hour_y, fill="black", width=6)

# Draw minute hand
    minute_angle = (minute+second/60)*math.pi/30-math.pi/2
    minute_x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(minute_angle)
    minute_y = HEIGHT/2 + 0.7 * HEIGHT/2 * math.sin(minute_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, minute_x, minute_y, fill="black", width=4)

# Draw second hand
    second_angle = second * math.pi/30 - math.pi/2
    second_x = WIDTH/2 + 0.6* WIDTH/2 * math.cos(second_angle)
    second_y = HEIGHT/2 + 0.6* HEIGHT/2 * math.sin(second_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, second_x, second_y, fill="red", width=2)

    canvas.after(1000, update_clock)


    
update_clock()
window.mainloop()


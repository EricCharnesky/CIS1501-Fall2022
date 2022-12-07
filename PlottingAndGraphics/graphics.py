# https://www.geeksforgeeks.org/how-do-you-create-a-button-on-a-tkinter-canvas/#:~:text=Steps%20%3A%201%20Import%20tkinter%20from%202%20Then,of%20place%20function%20in%20tkinter%20place%20the%20button.
import random

import tkinter as tk
from tkinter import Canvas, Frame, BOTH

class HistogramViewer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Histogram Viewer')
        self.pack(fill=BOTH, expand=1)
        self.btn = tk.Button(self.master, text='Color!', width=5,
                    height=5, bd='10', command=self.draw_circle)
        self.canvas = Canvas(self)
        self.btn.place(x=65, y=100)

        self.canvas.pack(fill=BOTH, expand=1)
        self.pack()


    def draw_circle(self):
        x1 = random.randint(0, 800)
        x2 = random.randint(0, 800)
        y1 = random.randint(0, 600)
        y2 = random.randint(0, 600)
        self.canvas.create_oval(x1, y1, x2, y2, outline='darkolivegreen4', fill='darkolivegreen4')


app_frame = tk.Tk()
app_frame.geometry('800x600')
histogram_viewer = HistogramViewer(master=app_frame)
histogram_viewer.mainloop()



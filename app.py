import random
import math
import tkinter as tk

class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        left_frame = tk.Frame(frame)
        left_frame.pack(side=tk.LEFT)
        right_frame = tk.Frame(frame)
        right_frame.pack(side=tk.RIGHT)

        top_bar = tk.Frame(left_frame, borderwidth=5)
        top_bar.pack(side=tk.TOP, fill=tk.X)
        tl_text = tk.Label(top_bar, text='Tropical Zodiac\nEqual Houses\nQuadrants')
        tl_text.pack(side=tk.LEFT)
        tr_text = tk.Label(top_bar, text='DRAW  1\nzh 2\nZET9')
        tr_text.pack(side=tk.RIGHT)
        self.canvas = tk.Canvas(left_frame, background="black", width=640, height=480)
        self.canvas.pack(side=tk.TOP)
        bottom_bar = tk.Frame(left_frame, borderwidth=5)
        bottom_bar.pack(side=tk.TOP, fill=tk.X)
        bl_text = tk.Label(bottom_bar, text='2-D Radix\nHorizon view\nOrigo: Tropos')
        bl_text.pack(side=tk.LEFT)
        br_text = tk.Label(bottom_bar, text='MC >> S\nASC > E')
        br_text.pack(side=tk.RIGHT)

        self.button = tk.Button(right_frame, text="Dot", command=self.place_dot)
        self.button.pack(side=tk.TOP)
        self.button2 = tk.Button(right_frame, text="Chart", command=self.draw_chart)
        self.button2.pack(side=tk.TOP)
   
    def place_dot(self):
        x = random.randrange(0, 640)
        y = random.randrange(0, 480)
        self.canvas.create_oval((x, y, x + 5, y + 5), outline='red', fill="black")

    def draw_chart(self):
        canv = self.canvas
        canv.delete(tk.ALL)
        x = 245
        y = 240
        p1 = 180
        p2 = 221
        p3 = 226
        pa = 56
        yz = 92.62923
        canv.create_rectangle((x, y, x + 1, y + 1), fill='white', outline='')
        canv.create_oval(get_bbox(x, y, p2), fill='aquamarine', outline='white')
        canv.create_oval(get_bbox(x, y, p1), fill='black', outline='white')
        canv.create_oval(get_bbox(x, y, p3), fill='', outline='white')
        canv.create_oval(get_bbox(x, y, pa), fill='', outline='white')
        canv.create_oval(get_bbox(x, y, p3 + 12), fill='', outline='dark turquoise')
        canv.create_oval(get_bbox(x, y, 267), fill='', outline='dark turquoise')

        for degrees in range(0, 360, 30):
            r = math.radians(degrees)
            canv.create_line((x + math.cos(r) * 181, y + math.sin(r) * 181,
                              x + math.cos(r) * 221, y + math.sin(r) * 221),
                             fill='white')
        for degrees in range(0, 360, 30):
            r = math.radians(degrees + yz)
            canv.create_line((x + math.cos(r) * (p3 + 12), y + math.sin(r) * (p3 + 12),
                              x + math.cos(r) * (p3 + 45), y + math.sin(r) * (p3 + 45)),
                             fill='dark turquoise')
        
def get_bbox(x, y, radius):
    return (x - radius, y - radius, x + radius, y + radius)    

root = tk.Tk()
root.title('ChartDraw')

app = App(root)

root.mainloop()

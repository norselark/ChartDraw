import tkinter as tk
import random

class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.canvas = tk.Canvas(frame, background="white", width=100, height=100)
        self.canvas.pack(side=tk.TOP)
        self.button = tk.Button(frame, text="Dot", command=self.place_dot)
        self.button.pack(side=tk.TOP)
    
    def place_dot(self):
        x = random.randrange(0, 100)
        y = random.randrange(0, 100)
        self.canvas.create_oval((x, y, x + 5, y + 5), outline='red', fill="black")

root = tk.Tk()

app = App(root)

root.mainloop()
root.destroy()

import random
import tkinter as tk
import numpy as np
from transform_canvas import TransformCanvas

p = ['', '292.24327', '242.66082', '271.75037', '293.01350', '231.33463',
     '228.76548', '272.72153', ' 24.61269', '342.18475', '289.17087', '135.16396']

GLYPHS = {
    'sun': u'\u2609',
    'moon': u'\u263d',
    'mercury': u'\u263f',
    'venus': u'\u2640',
    'earth': u'\u2295',
    'mars': u'\u2642',
    'jupiter': u'\u2643',
    'saturn': u'\u2644',
    'uranus': u'\u2645',
    'neptune': u'\u2646',
    'pluto': u'\u2647',
    'ari': u'\u2648',
    'tau': u'\u2649',
    'gem': u'\u264a',
    'cnc': u'\u264b',
    'leo': u'\u264c',
    'vir': u'\u264d',
    'lib': u'\u264e',
    'sco': u'\u264f',
    'sag': u'\u2650',
    'cap': u'\u2651',
    'aqu': u'\u2652',
    'pis': u'\u2653'
}

ZODIAC = ['ari', 'tau', 'gem', 'cnc', 'leo', 'vir',
          'lib', 'sco', 'sag', 'cap', 'aqu', 'pis']

PLANETS = ['', 'sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter',
           'saturn', 'uranus', 'neptune', 'pluto']

def rotate_coords(coords, degrees):
    r = np.radians(degrees)
    w = np.array([[np.cos(r), -np.sin(r)],
                  [np.sin(r), np.cos(r)]])
    return np.dot(coords, w)

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
        self.canvas = TransformCanvas(left_frame, background="black", width=640, height=480)
        self.canvas.pack(side=tk.TOP)
        bottom_bar = tk.Frame(left_frame, borderwidth=5)
        bottom_bar.pack(side=tk.TOP, fill=tk.X)
        bl_text = tk.Label(bottom_bar, text='2-D Radix\nHorizon view\nOrigo: Tropos')
        bl_text.pack(side=tk.LEFT)
        br_text = tk.Label(bottom_bar, text=u'MC \u25b7 S\nASC \u25b6 E')
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
        origin = np.array([x, y]) 
        canv.set_center(origin)
        p1 = 180
        p2 = 221
        p3 = 226
        pa = 56
        yz = 92.62923
        zy = 267.37077
        canv.circle((0, 0), p2, fill='aquamarine', outline='white')
        canv.circle((0, 0), p1, fill='black', outline='white')
        canv.circle((0, 0), p3, fill='', outline='white')
        canv.circle((0, 0), pa, fill='', outline='white')
        canv.circle((0, 0), p3 + 12, fill='', outline='dark turquoise')
        canv.circle((0, 0), 267, fill='', outline='dark turquoise')

        # White sector lines
        coords = [[181, 0], [221, 0]]
        for degrees in range(0, 360, 30):
            canv.set_rotation(degrees)
            canv.line(coords, fill='white')

        # Delineating the regions of the zodiac
        coords = [[p3 + 12, 0], [p3 + 45, 0]]
        for degrees in range(0, 360, 30):
            canv.set_rotation(degrees + yz)
            canv.line(coords, fill='dark turquoise')

        # Zodiac symbols
        coords = [p3 + 26, 0]
        for sign, degrees in zip(ZODIAC, range(0, 360, 30)):
            canv.set_rotation(degrees + 15 + yz)
            canv.text(coords, text=GLYPHS[sign], fill='dark turquoise', font=(None, 18))

        # Sectors of 5 degrees along the rim
        coords = [[p2, 0], [p3, 0]]
        for degrees in range(0, 360, 5):
            canv.set_rotation(degrees)
            canv.line(coords, fill='white')

        # Planet symbols with circle markers
        for angle, planet in zip(p[1:], PLANETS[1:]):
            canv.set_rotation(float(angle) - zy)

            coords = [p1 - 5, 0]
            canv.circle(coords, 3, fill='', outline='white')

            coords = [p1 + 51, 0]
            for r in [1, 2, 3]:
                canv.circle(coords, r, fill='', outline='white')
                                 
            glyph = GLYPHS[planet]
            coords = [p1 + 21, 0]
            new_coords = origin + rotate_coords(coords, degrees)
            canv.text(coords, text=glyph, fill='black', font=(None, 18))


def get_bbox(x, y, radius, matrix=False):
    if matrix:
        return np.array([[x - radius, y - radius], [x + radius, y + radius]])
    else:
        return [x - radius, y - radius, x + radius, y + radius]

root = tk.Tk()
root.title('ChartDraw')

app = App(root)

root.mainloop()

from pathlib import Path
import tkinter as tk
import numpy as np
from transform_canvas import TransformCanvas
from treeview_panel import TreeviewPanel, ChartSelection
from aq_functions import coordinates, truncate_rounding


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
    'Ari': u'\u2648',
    'Tau': u'\u2649',
    'Gem': u'\u264a',
    'Can': u'\u264b',
    'Leo': u'\u264c',
    'Vir': u'\u264d',
    'Lib': u'\u264e',
    'Sco': u'\u264f',
    'Sag': u'\u2650',
    'Cap': u'\u2651',
    'Aqu': u'\u2652',
    'Psc': u'\u2653'
}

ZODIAC = ['Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir',
          'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Psc']

PLANETS = ['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter',
           'saturn', 'uranus', 'neptune', 'pluto']


def load_data():
    data_dir = Path('aqCHARTS/aq_temp')
    angles = [None] * 13
    truncated_angles = [None] * 13
    with (data_dir / 'PDAT.DAT').open() as infile:
        # Discard first 10 lines for now
        for _ in range(10):
            infile.readline()
        for idx in range(11):
            line = infile.readline().rstrip('\n')
            angles[idx] = float(line)
            truncated_angles[idx] = truncate_rounding(line)

    with (data_dir / 'ANGDAT.DAT').open() as infile:
        for idx in range(11, 13):
            line = infile.readline().rstrip('\n')
            angles[idx] = float(line)
            truncated_angles[idx] = truncate_rounding(line)

    return {"letters": ['S', 'L', 'H', 'V', 'M', 'J', 'D', 'U', 'N', 'P', 'X', 'C', 'A'],
            "angles": angles,
            "truncated_angles": truncated_angles}


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('ChartDraw')
        frame = tk.Frame(self)
        frame.pack()
        left_frame = tk.Frame(frame)
        left_frame.pack(side=tk.LEFT)
        right_frame = tk.Frame(frame)
        right_frame.pack(side=tk.RIGHT)

        self.data = load_data()

        top_bar = tk.Frame(left_frame, borderwidth=5)
        top_bar.pack(side=tk.TOP, fill=tk.X)
        tl_text = tk.Label(top_bar,
                           text='Tropical Zodiac\nEqual Houses\nQuadrants')
        tl_text.pack(side=tk.LEFT)
        tr_text = tk.Label(top_bar, text='DRAW\nzh 2\nZET9')
        self.type_string = tk.StringVar(self, value='1')
        self.chart_type = tk.Label(top_bar, textvariable=self.type_string)
        self.chart_type.pack(side=tk.RIGHT)
        tr_text.pack(side=tk.RIGHT)

        self.canvas = TransformCanvas(left_frame, background="black",
                                      width=512, height=512)
        self.canvas.pack(side=tk.TOP)
        bottom_bar = tk.Frame(left_frame, borderwidth=5)
        bottom_bar.pack(side=tk.TOP, fill=tk.X)
        bl_text = tk.Label(bottom_bar,
                           text='2-D Radix\nHorizon view\nOrigo: Tropos')
        bl_text.pack(side=tk.LEFT)
        br_text = tk.Label(bottom_bar, text=u'MC \u25b7 S\nASC \u25b6 E')
        br_text.pack(side=tk.RIGHT)

        redraw_button = tk.Button(bottom_bar, text="Redraw chart",
                                  command=self.redraw_chart)
        redraw_button.pack(side=tk.TOP)
        self.tv = TreeviewPanel(right_frame, self.data)
        self.tv.pack(side=tk.TOP)

        self.focus_set()
        self.bind('<Key>', self.dispatch)

        self.draw_chart()

    def dispatch(self, event):
        if event.type == tk.EventType.KeyPress and event.char == '=':
            self.tv.toggle_column()
        if event.type == tk.EventType.KeyPress and event.char == '+':
            self.tv.scroll_up()

    def redraw_chart(self):
        sel = ChartSelection(self)
        self.type_string.set(str(sel.result))
        self.draw_chart()

    def draw_chart(self):
        yy, yz, zy = coordinates(self.data['angles'][-1])
        canv = self.canvas
        canv.delete(tk.ALL)
        x = 256
        y = 256
        origin = np.array([x, y])
        canv.set_center(origin)
        p1 = 180
        p2 = 221
        p3 = 226
        pa = 56
        canv.circle((0, 0), p2, fill='#55ffff', outline='white')
        canv.circle((0, 0), p1, fill='#5555ff', outline='white')
        canv.create_arc([x - p1, y - p1, x + p1, y + p1], fill='#0000aa',
                        outline='white', start=180, extent=180)
        canv.circle((0, 0), p3, fill='', outline='white')
        canv.circle((0, 0), pa, fill='#55ffff', outline='black')
        canv.circle((0, 0), 1, fill='black', outline='')
        canv.circle((0, 0), p3 + 12, fill='', outline='#00aaaa')
        canv.circle((0, 0), 267, fill='', outline='#00aaaa')

        # White sector lines
        coords = [[181, 0], [221, 0]]
        for degrees in range(0, 360, 30):
            canv.set_rotation(degrees)
            canv.line(coords, fill='white')

        # Delineating the regions of the zodiac
        coords = [[p3 + 12, 0], [p3 + 45, 0]]
        for degrees in range(0, 360, 30):
            canv.set_rotation(degrees + yz)
            canv.line(coords, fill='#00aaaa')

        # Zodiac symbols
        coords = [p3 + 26, 0]
        for sign, degrees in zip(ZODIAC, range(0, 360, 30)):
            canv.set_rotation(degrees + 15 + yz)
            glyph = GLYPHS[sign]
            canv.text(coords, text=glyph, fill='#00aaaa', font=(None, 18))

        # Sectors of 5 degrees along the rim
        coords = [[p2, 0], [p3, 0]]
        for degrees in range(0, 360, 5):
            canv.set_rotation(degrees + yz)
            canv.line(coords, fill='white')

        # Planet symbols with circle markers
        for angle, planet in zip(self.data['angles'], PLANETS):
            canv.set_rotation(float(angle) - zy)

            coords = [p1 - 5, 0]
            canv.circle(coords, 3, fill='', outline='white')

            coords = [p1 + 51, 0]
            for r in [1, 2, 3]:
                canv.circle(coords, r, fill='', outline='white')

            glyph = GLYPHS[planet]
            coords = [p1 + 21, 0]
            canv.text(coords, text=glyph, fill='black', font=(None, 18))

        self.draw_asc(self.data['angles'][-1] - zy)
        self.draw_mc(self.data['angles'][-2] - zy)

    def draw_asc(self, angle):
        canv = self.canvas

        # depends on sv$
        i, il, l = 1, 9, 3

        canv.set_rotation(angle)
        canv.line([[-57, 0], [-179, 0]], fill='white')
        canv.line([[57, 0], [179, 0]], fill='white')
        canv.line([[179 + 41, 0], [179 + 50, 0]], fill='white')
        canv.polygon((229, 0), [[0, -3], [5, -3],
                                [15, 0], [5, 3], [0, 3]], fill='white')

    def draw_mc(self, angle):
        canv = self.canvas

        # depends on sv$
        i, il, l = 1, 9, 3

        canv.set_rotation(angle)
        canv.line([[-57, 0], [-179, 0]], fill='white')
        canv.line([[57, 0], [179, 0]], fill='white')
        canv.line([[179 + 41, 0], [179 + 50, 0]], fill='white')
        canv.polygon((229, 0), [[0, -3], [5, -3], [15, 0], [5, 3], [0, 3]],
                     outline='white', fill='black')


if __name__ == '__main__':
    app = App()
    app.mainloop()

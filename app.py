from pathlib import Path
import tkinter as tk
import numpy as np
from transform_canvas import TransformCanvas
import widgets
from aq_functions import coordinates, truncate_rounding

ARROW_COORDS = [[0, -3], [5, -3], [15, 0], [5, 3], [0, 3]]

GLYPHS = {
    'Sun': u'\u2609',
    'Moon': u'\u263d',
    'Mercury': u'\u263f',
    'Venus': u'\u2640',
    'Earth': u'\u2295',
    'Mars': u'\u2642',
    'Jupiter': u'\u2643',
    'Saturn': u'\u2644',
    'Uranus': u'\u2645',
    'Neptune': u'\u2646',
    'Pluto': u'\u2647',
    'Node': u'\u260a',
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

PLANETS = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter',
           'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Node']


def load_data():
    data_dir = Path('aqCHARTS/aq_temp')
    angles = [None] * 13
    truncated_angles = [None] * 13
    with (data_dir / 'PDAT.DAT').open() as infile: #pylint: disable=E1101
        # Discard first 10 lines for now
        for _ in range(10):
            infile.readline()
        for idx in range(11):
            line = infile.readline().rstrip('\n')
            angles[idx] = float(line)
            truncated_angles[idx] = truncate_rounding(line)

    with (data_dir / 'ANGDAT.DAT').open() as infile: #pylint: disable=E1101
        for idx in range(11, 13):
            line = infile.readline().rstrip('\n')
            angles[idx] = float(line)
            truncated_angles[idx] = truncate_rounding(line)

    return {"letters": [GLYPHS[p] for p in PLANETS] + ['MC', 'ASC'],
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

        reset_button = tk.Button(bottom_bar, text="Reset chart",
                                 command=self.reset_chart)
        reset_button.pack(side=tk.TOP)

        harmonic_button = tk.Button(right_frame, text='Harmonics', command=self.harmonic)
        harmonic_button.pack(side=tk.TOP)
        turned_axes_button = tk.Button(right_frame, text='Turned axes', command=self.turned)
        turned_axes_button.pack(side=tk.TOP)
        self.tv = widgets.TreeviewPanel(right_frame, self.data)
        self.tv.pack(side=tk.TOP)

        self.focus_set()
        self.bind('<Key>', self.dispatch)

        self.draw_chart(self.data['angles'])

    def dispatch(self, event):
        if event.char == '=':
            self.tv.toggle_column()
        elif event.char == '+':
            self.tv.scroll_up()

    def reset_chart(self):
        self.draw_chart(self.data['angles'])
    
    def draw_chart(self, angles, superimposed=None, cycle=1):
        yz, zy = coordinates(angles[-1])
        cycleoffset = 30 * (cycle - 1)
        if cycle != 1:
            yz -= cycleoffset
            zy += cycleoffset
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
                        outline='white', start=180 - cycleoffset, extent=180)
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
        for angle, planet in zip(angles, PLANETS):
            canv.set_rotation(float(angle) - zy)

            coords = [p1 - 5, 0]
            canv.circle(coords, 3, fill='', outline='white')

            coords = [p1 + 51, 0]
            for r in [1, 2, 3]:
                canv.circle(coords, r, fill='', outline='white')

            glyph = GLYPHS[planet]
            coords = [p1 + 21, 0]
            canv.text(coords, text=glyph, fill='black', font=(None, 18))
        
        if superimposed:
            for angle, planet in zip(superimposed, PLANETS):
                canv.set_rotation(float(angle) - zy)

                coords = [p1 - 5, 0]
                canv.circle(coords, 3, fill='', outline='red')

                coords = [p1 + 51, 0]
                for r in [1, 2, 3]:
                    canv.circle(coords, r, fill='', outline='red')

                glyph = GLYPHS[planet]
                coords = [p1 + 21, 0]
                canv.text(coords, text=glyph, fill='red', font=(None, 18))

        self.draw_asc(angles[-1] - zy, cycle)
        self.draw_mc(angles[-2] - zy, cycle)

        if cycle != 1:
            canv.circle((0, 0), pa, fill='#5555ff', outline='white')
            canv.create_arc([x - pa, y - pa, x + pa, y + pa], fill='#0000aa',
                            outline='white', start=180, extent=180)
            canv.set_rotation(angles[-1] - zy + cycleoffset)
            canv.line([[-pa, 0], [pa, 0]], fill='white')
            canv.polygon([pa, 0], ARROW_COORDS, fill='white')
            canv.set_rotation(angles[-2] - zy + cycleoffset)
            canv.line([[-pa, 0], [pa, 0]], fill='white')
            canv.polygon([pa, 0], ARROW_COORDS, fill='', outline='white')
            canv.set_rotation(angles[0] - zy + cycleoffset)
            canv.circle([pa - 8, 0], 2.5, fill='yellow', outline='black')
            canv.set_rotation(angles[1] - zy + cycleoffset)
            canv.circle([pa - 8, 0], 2.5, fill='grey', outline='black')
            canv.circle((0, 0), 5, fill='#55ffff', outline='black')
            canv.circle((0, 0), 1, fill='black')
            
            

    def draw_asc(self, angle, cycle):
        canv = self.canvas

        # depends on sv$
        i, il, l = 1, 9, 3

        canv.set_rotation(angle)
        canv.line([[-57, 0], [-179, 0]], fill='white')
        canv.line([[57, 0], [179, 0]], fill='white')
        canv.line([[179 + 41, 0], [179 + 50, 0]], fill='white')
        canv.polygon((229, 0), ARROW_COORDS, fill='white')
        if cycle != 1:
            canv.circle([234, 0], 3, fill='#5555ff', outline='')

    def draw_mc(self, angle, cycle):
        canv = self.canvas

        # depends on sv$
        i, il, l = 1, 9, 3
        fill = 'black' if cycle == 1 else '#5555ff'

        canv.set_rotation(angle)
        canv.line([[-57, 0], [-179, 0]], fill='white')
        canv.line([[57, 0], [179, 0]], fill='white')
        canv.line([[179 + 41, 0], [179 + 50, 0]], fill='white')
        canv.polygon((229, 0), ARROW_COORDS,
                     outline='white', fill=fill)
        
    def harmonic(self):
        result = widgets.HarmonicSelection(self).result
        if not result:
            return
        har = result['harmonic']
        harmonic_angles = [(har * ang) % 360 for ang in self.data['angles']]
        if result['superimposed']:
            self.draw_chart(self.data['angles'], superimposed=harmonic_angles)
        else:
            self.draw_chart(harmonic_angles)

    def turned(self):
        result = widgets.CycleSelection(self).result
        self.draw_chart(self.data['angles'], cycle=result)




if __name__ == '__main__':
    app = App()
    app.mainloop()

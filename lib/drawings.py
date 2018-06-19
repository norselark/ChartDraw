from itertools import combinations
from .utils import mirror_angle, asp
from .constants import GLYPHS, PLANETS, ZODIAC
from .constants import white, black, blue, lightblue, teal, lightteal, red, green
from .optimizer import optimize

ARROW_COORDS = [[0, -3], [5, -3], [15, 0], [5, 3], [0, 3]]

class Chart():
    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw_chart(self, angles, superimposed=None,
                   cycle=1, axes_text=['S', 'E']):
        start_of_zodiac = mirror_angle(angles[-1])
        cycleoffset = 30 * (cycle - 1)
        if cycle != 1:
            start_of_zodiac -= cycleoffset
        canv = self.canvas
        canv.delete('all')
        x = 256
        y = 256
        canv.set_center(complex(x, y))
        p1 = 180
        p2 = 221
        p3 = 226
        pa = 56
        canv.circle((0, 0), p2, fill=lightteal, outline=white)
        canv.circle((0, 0), p1, fill=lightblue, outline=white)
        canv.create_arc([x - p1, y - p1, x + p1, y + p1], fill=blue,
                        outline=white, start=180 - cycleoffset, extent=180)
        canv.circle((0, 0), p3, fill='', outline=white)
        canv.circle((0, 0), pa, fill=lightteal, outline=black)
        canv.circle((0, 0), 1, fill=black, outline='')
        canv.circle((0, 0), p3 + 12, fill='', outline=teal)
        canv.circle((0, 0), 267, fill='', outline=teal)

        # White sector lines
        coords = [[181, 0], [221, 0]]
        for degrees in range(0, 360, 30):
            canv.set_rotation(degrees)
            canv.line(coords, fill=white)

        # Delineating the regions of the zodiac
        coords = [[p3 + 12, 0], [p3 + 45, 0]]
        for degrees in range(0, 360, 30):
            canv.set_rotation(start_of_zodiac + degrees)
            canv.line(coords, fill=teal)
        
        # Zodiac symbols
        coords = [p3 + 26, 0]
        for sign, degrees in zip(ZODIAC, range(0, 360, 30)):
            canv.set_rotation(degrees + 15 + start_of_zodiac)
            glyph = GLYPHS[sign]
            canv.text(coords, text=glyph, fill=teal, font=(None, 18))

        # Sectors of 5 degrees along the rim
        coords = [[p2, 0], [p3, 0]]
        for degrees in range(0, 360, 5):
            canv.set_rotation(degrees + start_of_zodiac)
            canv.line(coords, fill=white)

        # Planet circle markers
        for angle, planet in zip(angles, PLANETS):
            canv.set_rotation(float(angle) + start_of_zodiac)

            coords = [p1 - 5, 0]
            canv.circle(coords, 3, fill='', outline=white)

            coords = [p1 + 51, 0]
            for r in [1, 2, 3]:
                canv.circle(coords, r, fill='', outline=white)

        # Planet symbols
        for angle, planet in zip(optimize(angles[:len(PLANETS)]), PLANETS):
            canv.set_rotation(float(angle) + start_of_zodiac)

            glyph = GLYPHS[planet]
            coords = [p1 + 21, 0]
            canv.text(coords, text=glyph, fill=black, font=(None, 18))

        if superimposed:
            for angle, planet in zip(superimposed, PLANETS):
                canv.set_rotation(float(angle) + start_of_zodiac)

                coords = [p1 - 5, 0]
                canv.circle(coords, 3, fill='', outline=red)

                coords = [p1 + 51, 0]
                for r in [1, 2, 3]:
                    canv.circle(coords, r, fill='', outline=red)

                glyph = GLYPHS[planet]
                coords = [p1 + 21, 0]
                canv.text(coords, text=glyph, fill=red, font=(None, 18))

        self.draw_asc(angles[-1] + start_of_zodiac, cycle)
        self.draw_mc(angles[-2] + start_of_zodiac, cycle)
        self.axes_legend(cycle, text=axes_text)

        if cycle != 1:
            self._minichart(angles, start_of_zodiac, cycleoffset)

    def draw_asc(self, angle, cycle):
        canv = self.canvas

        canv.set_rotation(angle)
        canv.line([[-57, 0], [-179, 0]], fill=white)
        canv.line([[57, 0], [179, 0]], fill=white)
        canv.line([[179 + 41, 0], [179 + 50, 0]], fill=white)
        canv.polygon((229, 0), ARROW_COORDS, fill=white, outline=white)
        if cycle != 1:
            canv.circle([234, 0], 3, fill=lightblue, outline='')

    def draw_mc(self, angle, cycle):
        canv = self.canvas

        fill = black if cycle == 1 else lightblue

        canv.set_rotation(angle)
        canv.line([[-57, 0], [-179, 0]], fill=white)
        canv.line([[57, 0], [179, 0]], fill=white)
        canv.line([[179 + 41, 0], [179 + 50, 0]], fill=white)
        canv.polygon((229, 0), ARROW_COORDS,
                     outline=white, fill=fill)

    def axes_legend(self, cycle, text=['S', 'E']):
        canv = self.canvas
        
        canv.create_text([416, 483], text='MC', fill=white, anchor='nw')
        canv.create_text([416, 498], text='ASC', fill=white, anchor='nw')
        if cycle == 1:
            canv.create_polygon([[x + 445, y + 489] for x, y in ARROW_COORDS],
                                outline=white, fill=black)
            canv.create_polygon([[x + 445, y + 506] for x, y in ARROW_COORDS],
                                outline=white, fill=white)
        else:
            canv.create_polygon([[x + 445, y + 489] for x, y in ARROW_COORDS],
                                outline=white, fill=lightblue)
            canv.create_polygon([[x + 445, y + 506] for x, y in ARROW_COORDS],
                                outline=white, fill=white)
            canv.create_oval([448, 503, 454, 509], fill=lightblue, outline='')
        canv.create_text([470, 483], text=text[0], fill=white, anchor='nw')
        canv.create_text([470, 498], text=text[1], fill=white, anchor='nw')

    def aspects(self, angles, cycle=1):
        r = 168
        xx = 256
        y = 256
        self.canvas.circle((0, 0), r, fill=white, outline='', tags='asp')
        zy = -mirror_angle(angles[-1]) + 30 * (cycle - 1)
        for a, b in combinations(angles[:-3], 2):
            v = (a - zy) % 360
            self.canvas.set_rotation(v)
            aspect, degree = asp(a, b, orbis=8)
            if aspect is None or aspect in [0, 30]:
                continue
            col = green
            if aspect in [90, 180]:
                col = red
            v2 = (b - zy) % 360
            extent = (v2 - v) % 360

            width = 1
            dash = None
            if degree <= 1 / 3:
                dash = [2, 2]
            elif degree >= 2 / 3:
                width = 2.2

            self.canvas.create_arc([xx - r, y - r, xx + r, y + r],
                                   style='chord', fill='',
                                   dash=dash, width=width,
                                   outline=col, start=v, extent=extent,
                                   tags='asp')
        pa = 10
        self.canvas.circle((0, 0), pa, fill=lightblue, outline='', tags='asp')
        self.canvas.create_arc([xx - pa, y - pa, xx + pa, y + pa],
                               fill=blue,
                               outline='', start=180, extent=180, tags='asp')
        self.canvas.circle((0, 0), pa, fill='', outline=black, tags='asp')
        self.canvas.set_rotation(angles[-1] - zy)
        self.canvas.line([[-pa, 0], [pa, 0]], fill=white, tags='asp')
        self.canvas.set_rotation(angles[-2] - zy)
        self.canvas.line([[-pa, 0], [pa, 0]], fill=white, tags='asp')
        self.canvas.circle((0, 0), 3, fill=lightteal, outline='', tags='asp')
        self.canvas.circle((0, 0), 1, fill=black, tags='asp')


    def _minichart(self, angles, start_of_zodiac, cycleoffset):
        "Draw miniature chart in the center"
        canv = self.canvas
        x = 256
        y = 256
        radius = 56
        canv.circle((0, 0), radius, fill=lightblue, outline=white)
        canv.create_arc([x - radius, y - radius, x + radius, y + radius],
                        fill=blue, outline=white, start=180, extent=180)
        # ASC
        canv.set_rotation(angles[-1] + start_of_zodiac + cycleoffset)
        canv.line([[-radius, 0], [radius, 0]], fill=white)
        canv.polygon([radius, 0], ARROW_COORDS, fill=white)
        # MC
        canv.set_rotation(angles[-2] + start_of_zodiac + cycleoffset)
        canv.line([[-radius, 0], [radius, 0]], fill=white)
        canv.polygon([radius, 0], ARROW_COORDS, fill='', outline=white)
        # Miniature sun
        canv.set_rotation(angles[0] + start_of_zodiac + cycleoffset)
        canv.circle([radius - 8, 0], 2.5, fill='yellow', outline=black)
        # Miniature moon
        canv.set_rotation(angles[1] + start_of_zodiac + cycleoffset)
        canv.circle([radius - 8, 0], 2.5, fill='grey', outline=black)
        # Tiny hub
        canv.circle((0, 0), 5, fill=lightteal, outline=black)
        canv.circle((0, 0), 1, fill=black)



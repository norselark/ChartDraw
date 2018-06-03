from itertools import combinations
from lib.utils import coordinates, asp
from lib.constants import GLYPHS, PLANETS, ZODIAC
from lib.constants import white, black, blue, lightblue, teal, lightteal, red, green

ARROW_COORDS = [[0, -3], [5, -3], [15, 0], [5, 3], [0, 3]]

class Chart():
    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw_chart(self, angles, superimposed=None,
                   cycle=1, axes_text=['S', 'E']):
        yz = coordinates(angles[-1])
        cycleoffset = 30 * (cycle - 1)
        if cycle != 1:
            yz -= cycleoffset
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
            canv.set_rotation(degrees + yz)
            canv.line(coords, fill=teal)

        # Zodiac symbols
        coords = [p3 + 26, 0]
        for sign, degrees in zip(ZODIAC, range(0, 360, 30)):
            canv.set_rotation(degrees + 15 + yz)
            glyph = GLYPHS[sign]
            canv.text(coords, text=glyph, fill=teal, font=(None, 18))

        # Sectors of 5 degrees along the rim
        coords = [[p2, 0], [p3, 0]]
        for degrees in range(0, 360, 5):
            canv.set_rotation(degrees + yz)
            canv.line(coords, fill=white)

        # Planet symbols with circle markers
        for angle, planet in zip(angles, PLANETS):
            canv.set_rotation(float(angle) + yz)

            coords = [p1 - 5, 0]
            canv.circle(coords, 3, fill='', outline=white)

            coords = [p1 + 51, 0]
            for r in [1, 2, 3]:
                canv.circle(coords, r, fill='', outline=white)

            glyph = GLYPHS[planet]
            coords = [p1 + 21, 0]
            canv.text(coords, text=glyph, fill=black, font=(None, 18))

        if superimposed:
            for angle, planet in zip(superimposed, PLANETS):
                canv.set_rotation(float(angle) + yz)

                coords = [p1 - 5, 0]
                canv.circle(coords, 3, fill='', outline=red)

                coords = [p1 + 51, 0]
                for r in [1, 2, 3]:
                    canv.circle(coords, r, fill='', outline=red)

                glyph = GLYPHS[planet]
                coords = [p1 + 21, 0]
                canv.text(coords, text=glyph, fill=red, font=(None, 18))

        self.draw_asc(angles[-1] + yz, cycle)
        self.draw_mc(angles[-2] + yz, cycle)
        self.axes_legend(cycle, text=axes_text)

        if cycle != 1:
            # Draw miniature chart in the center
            canv.circle((0, 0), pa, fill=lightblue, outline=white)
            canv.create_arc([x - pa, y - pa, x + pa, y + pa], fill=blue,
                            outline=white, start=180, extent=180)
            canv.set_rotation(angles[-1] + yz + cycleoffset)
            canv.line([[-pa, 0], [pa, 0]], fill=white)
            canv.polygon([pa, 0], ARROW_COORDS, fill=white)
            canv.set_rotation(angles[-2] + yz + cycleoffset)
            canv.line([[-pa, 0], [pa, 0]], fill=white)
            canv.polygon([pa, 0], ARROW_COORDS, fill='', outline=white)
            canv.set_rotation(angles[0] + yz + cycleoffset)
            canv.circle([pa - 8, 0], 2.5, fill='yellow', outline=black)
            canv.set_rotation(angles[1] + yz + cycleoffset)
            canv.circle([pa - 8, 0], 2.5, fill='grey', outline=black)
            canv.circle((0, 0), 5, fill=lightteal, outline=black)
            canv.circle((0, 0), 1, fill=black)

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

    def aspects(self, angles):
        r = 168
        xx = 256
        y = 256
        self.canvas.circle((0, 0), r, fill=white, outline='')
        zy = -coordinates(angles[-1])
        for a, b in combinations(angles[:-3], 2):
            v = (a - zy) % 360
            self.canvas.set_rotation(v)
            dr = asp(a, b, orbis=8)
            if dr is None or dr in [0, 30]:
                continue
            col = green
            if dr in [90, 180]:
                col = red
            v2 = (b - zy) % 360
            extent = (v2 - v) % 360
            self.canvas.create_arc([xx - r, y - r, xx + r, y + r],
                                    style='chord', fill='',
                                    outline=col, start=v, extent=extent)
        pa = 10
        self.canvas.circle((0, 0), pa, fill=lightblue, outline='')
        self.canvas.create_arc([xx - pa, y - pa, xx + pa, y + pa],
                               fill=blue,
                               outline='', start=180, extent=180)
        self.canvas.circle((0, 0), pa, fill='', outline=black)
        self.canvas.set_rotation(angles[-1] - zy)
        self.canvas.line([[-pa, 0], [pa, 0]], fill=white)
        self.canvas.set_rotation(angles[-2] - zy)
        self.canvas.line([[-pa, 0], [pa, 0]], fill=white)
        self.canvas.circle((0, 0), 3, fill=lightteal, outline='')
        self.canvas.circle((0, 0), 1, fill=black)


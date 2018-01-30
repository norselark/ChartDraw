from aq_functions import coordinates, aspectCalc, asp

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
            canv.set_rotation(float(angle) + yz)

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
                canv.set_rotation(float(angle) + yz)

                coords = [p1 - 5, 0]
                canv.circle(coords, 3, fill='', outline='red')

                coords = [p1 + 51, 0]
                for r in [1, 2, 3]:
                    canv.circle(coords, r, fill='', outline='red')

                glyph = GLYPHS[planet]
                coords = [p1 + 21, 0]
                canv.text(coords, text=glyph, fill='red', font=(None, 18))

        self.draw_asc(angles[-1] + yz, cycle)
        self.draw_mc(angles[-2] + yz, cycle)
        self.axes_legend(cycle, text=axes_text)

        if cycle != 1:
            # Draw miniature chart in the center
            canv.circle((0, 0), pa, fill='#5555ff', outline='white')
            canv.create_arc([x - pa, y - pa, x + pa, y + pa], fill='#0000aa',
                            outline='white', start=180, extent=180)
            canv.set_rotation(angles[-1] + yz + cycleoffset)
            canv.line([[-pa, 0], [pa, 0]], fill='white')
            canv.polygon([pa, 0], ARROW_COORDS, fill='white')
            canv.set_rotation(angles[-2] + yz + cycleoffset)
            canv.line([[-pa, 0], [pa, 0]], fill='white')
            canv.polygon([pa, 0], ARROW_COORDS, fill='', outline='white')
            canv.set_rotation(angles[0] + yz + cycleoffset)
            canv.circle([pa - 8, 0], 2.5, fill='yellow', outline='black')
            canv.set_rotation(angles[1] + yz + cycleoffset)
            canv.circle([pa - 8, 0], 2.5, fill='grey', outline='black')
            canv.circle((0, 0), 5, fill='#55ffff', outline='black')
            canv.circle((0, 0), 1, fill='black')

    def draw_asc(self, angle, cycle):
        canv = self.canvas

        canv.set_rotation(angle)
        canv.line([[-57, 0], [-179, 0]], fill='white')
        canv.line([[57, 0], [179, 0]], fill='white')
        canv.line([[179 + 41, 0], [179 + 50, 0]], fill='white')
        canv.polygon((229, 0), ARROW_COORDS, fill='white', outline='white')
        if cycle != 1:
            canv.circle([234, 0], 3, fill='#5555ff', outline='')

    def draw_mc(self, angle, cycle):
        canv = self.canvas

        fill = 'black' if cycle == 1 else '#5555ff'

        canv.set_rotation(angle)
        canv.line([[-57, 0], [-179, 0]], fill='white')
        canv.line([[57, 0], [179, 0]], fill='white')
        canv.line([[179 + 41, 0], [179 + 50, 0]], fill='white')
        canv.polygon((229, 0), ARROW_COORDS,
                     outline='white', fill=fill)

    def axes_legend(self, cycle, text=['S', 'E']):
        canv = self.canvas
        
        canv.create_text([416, 483], text='MC', fill='white', anchor='nw')
        canv.create_text([416, 498], text='ASC', fill='white', anchor='nw')
        if cycle == 1:
            canv.create_polygon([[x + 445, y + 489] for x, y in ARROW_COORDS], outline='white', fill='black')
            canv.create_polygon([[x + 445, y + 506] for x, y in ARROW_COORDS], outline='white', fill='white')
        else:
            canv.create_polygon([[x + 445, y + 489] for x, y in ARROW_COORDS], outline='white', fill='#5555ff')
            canv.create_polygon([[x + 445, y + 506] for x, y in ARROW_COORDS], outline='white', fill='white')
            canv.create_oval([448, 503, 454, 509], fill='#5555ff', outline='')
        canv.create_text([470, 483], text=text[0], fill='white', anchor='nw')
        canv.create_text([470, 498], text=text[1], fill='white', anchor='nw')

    def aspects(self, angles):
        print(angles)
        w = aspectCalc(angles)
        print(len(w))
        r = 168
        xx = 256
        y = 256
        self.canvas.circle((0, 0), r, fill='white', outline='')
        zy = -coordinates(angles[-1])
        for z in range(len(angles) - 3):
            v = (angles[z] - zy) % 360
            for x in range(len(angles) - 3):
                ww = w[z][x]
                dr = asp(ww, 8)
                if dr == '':
                    continue
                if dr in ':-':
                    continue
                self.canvas.set_rotation(v)
                col = '#00aa00'
                if dr in 'ko':
                    col = '#aa0000'
                v2 = (angles[x] - zy) % 360
                self.canvas.create_arc([xx - r, y - r, xx + r, y + r], style='chord', fill='',
                                       outline=col, start=v, extent=v2 - v)
        pa = 10
        self.canvas.circle((0, 0), pa, fill='#5555ff', outline='')
        self.canvas.create_arc([xx - pa, y - pa, xx + pa, y + pa], fill='#0000aa',
                               outline='', start=180, extent=180)
        self.canvas.circle((0, 0), pa, fill='', outline='black')
        self.canvas.set_rotation(angles[-1] - zy)
        self.canvas.line([[-pa, 0], [pa, 0]], fill='white')
        self.canvas.set_rotation(angles[-2] - zy)
        self.canvas.line([[-pa, 0], [pa, 0]], fill='white')
        self.canvas.circle((0, 0), 3, fill='#55ffff', outline='')
        self.canvas.circle((0, 0), 1, fill='black')


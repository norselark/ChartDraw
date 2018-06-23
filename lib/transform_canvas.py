"""A subclass of Canvas to make it easier to work with polar coordinates"""

from tkinter import Canvas
from math import cos, sin, radians
from .utils import complex_to_coords

class TransformCanvas(Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rotation = 1 + 0j
        self.center = 0 + 0j

    def set_center(self, new_center: complex):
        self.center = new_center

    def set_rotation(self, angle, mode='degrees'):
        if mode == 'degrees':
            angle = radians(angle)
        self.rotation = complex(cos(angle), -sin(angle))

    def apply_transform(self, coords):
        return [self.center + self.rotation * complex(x, y) for x, y in coords]

    def line(self, coords, **kwargs):
        new_coords = self.apply_transform(coords)
        new_coords = complex_to_coords(new_coords)
        self.create_line(new_coords, **kwargs)

    def circle(self, center, radius, **kwargs):
        center = self.apply_transform([center])[0]
        x, y = center.real, center.imag
        coords = (x - radius, y - radius, x + radius, y + radius)
        self.create_oval(coords, **kwargs)

    def text(self, coords, **kwargs):
        new_coords = self.apply_transform([coords])
        new_coords = complex_to_coords(new_coords)
        self.create_text(new_coords, **kwargs)

    def polygon(self, origin, coords, **kwargs):
        transposed = [[x + origin[0], y + origin[1]] for x, y in coords]
        new_coords = self.apply_transform(transposed)
        new_coords = complex_to_coords(new_coords)
        self.create_polygon(new_coords, **kwargs)

    def chord(self, radius, start_angle, end_angle, **kwargs):
        self.set_rotation(0)
        start_angle = radians(start_angle)
        end_angle = radians(end_angle)
        coords = [[radius * cos(start_angle), -radius * sin(start_angle)],
                  [radius * cos(end_angle), -radius * sin(end_angle)]]
        new_coords = self.apply_transform(coords)
        self.create_line(complex_to_coords(new_coords), **kwargs)

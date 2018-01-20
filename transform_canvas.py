from tkinter import Canvas
import numpy as np


class TransformCanvas(Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rotation_matrix = np.identity(2)
        self.center = np.array([0, 0])

    def set_center(self, new_center):
        self.center = new_center

    def set_rotation(self, angle, mode='degrees'):
        if mode == 'degrees':
            angle = np.radians(angle)
        self.rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                         [np.sin(angle), np.cos(angle)]])

    def line(self, coords, **kwargs):
        coords = np.array(coords).reshape((2, 2))
        new_coords = np.dot(coords, self.rotation_matrix) + self.center
        new_coords = list(new_coords.flatten())
        self.create_line(new_coords, **kwargs)

    def circle(self, center, radius, **kwargs):
        x, y = np.dot(center, self.rotation_matrix) + self.center
        coords = (x - radius, y - radius, x + radius, y + radius)
        self.create_oval(coords, **kwargs)

    def text(self, coords, **kwargs):
        new_coords = np.dot(coords, self.rotation_matrix) + self.center
        new_coords = list(new_coords.flatten())
        self.create_text(new_coords, **kwargs)

    def polygon(self, origin, coords, **kwargs):
        transposed = origin + np.array(coords)
        new_coords = np.dot(transposed, self.rotation_matrix) + self.center
        new_coords = list(new_coords.flatten())
        self.create_polygon(new_coords, **kwargs)

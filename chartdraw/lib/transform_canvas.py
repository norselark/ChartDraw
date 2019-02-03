"""A subclass of Canvas to make it easier to work with polar coordinates."""

from math import cos, radians, sin
from tkinter import Canvas
from typing import Iterable, List, Tuple

from .utils import complex_to_coords

Vec2D = Tuple[float, float]
CoordList = Iterable[Vec2D]


class TransformCanvas(Canvas):
    """A canvas adapted to work with polar coordinates.

    Any arguments are passed to :ref:`tkinter.Canvas`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rotation = 1 + 0j
        self.center = 0 + 0j

    def set_center(self, new_center: Vec2D) -> None:
        """Set a new center for polar coordinates.

        Args:
            new_center: A pair of values corresponding to x, y coordinates
                in the underlying Cartesian canvas
        """
        self.center = complex(new_center[0], new_center[1])

    def set_rotation(self, angle: float, mode: str = 'degrees') -> None:
        """Set an angle relative to the origin.

        Args:
            angle: Angle, anticlockwise with 0 to the right
            mode: Defaults to 'degrees'.
        """
        if mode == 'degrees':
            angle = radians(angle)
        self.rotation = complex(cos(angle), -sin(angle))

    def apply_transform(self, coords: CoordList) -> List[complex]:
        """Transform a sequence of polar coodinates to Cartesian.

        Args:
            coords: Raw coordinates

        Returns:
            A list of new coordinates as complex numbers
        """
        return [self.center + self.rotation * complex(x, y) for x, y in coords]

    def line(self, coords: CoordList, **kwargs) -> None:
        complex_coords = self.apply_transform(coords)
        new_coords = complex_to_coords(complex_coords)
        self.create_line(new_coords, **kwargs)

    def circle(self, center: Vec2D, radius: float, **kwargs) -> None:
        """Draw a circle centered according to polar coords.

        Args:
            center: location of circle's center
            radius: radius of drawn circle, in pixels
        """

        center_p = self.apply_transform([center])[0]
        x, y = center_p.real, center_p.imag
        coords = [x - radius, y - radius, x + radius, y + radius]
        self.create_oval(coords, **kwargs)

    def text(self, coords: Tuple[float, float], **kwargs) -> None:
        complex_coords = self.apply_transform([coords])
        new_coords = complex_to_coords(complex_coords)
        self.create_text(new_coords, **kwargs)

    def polygon(self, origin: Vec2D, coords: CoordList, **kwargs) -> None:
        transposed = [(x + origin[0], y + origin[1]) for x, y in coords]
        complex_coords = self.apply_transform(transposed)
        new_coords = complex_to_coords(complex_coords)
        self.create_polygon(new_coords, **kwargs)

    def chord(self, radius: float,
              start_angle: float, end_angle: float, **kwargs) -> None:
        self.set_rotation(0)
        start_angle = radians(start_angle)
        end_angle = radians(end_angle)
        coords = [(radius * cos(start_angle), -radius * sin(start_angle)),
                  (radius * cos(end_angle), -radius * sin(end_angle))]
        new_coords = self.apply_transform(coords)
        self.create_line(complex_to_coords(new_coords), **kwargs)

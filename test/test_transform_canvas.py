from unittest import TestCase
from unittest.mock import Mock

from lib.transform_canvas import TransformCanvas


class TestTransformCanvas(TestCase):
    def setUp(self):
        self.tc = TransformCanvas()

    def test_circle(self):
        self.tc.create_oval = Mock()
        self.tc.set_center(10 + 10j)
        self.tc.circle([0, 0], 2)
        self.tc.create_oval.assert_called_with([8, 8, 12, 12])

    def test_line(self):
        self.tc.create_line = Mock()
        self.tc.set_center(10 + 10j)
        self.tc.line([[0, 0], [2, 2]])
        self.tc.create_line.assert_called_with([10, 10, 12, 12])

        self.tc.set_rotation(90)
        self.tc.line([[0, 0], [2, 2]])
        self.tc.create_line.assert_called_with([10, 10, 12, 8])

    def test_chord(self):
        self.tc.create_line = Mock()
        self.tc.set_center(10 + 10j)
        self.tc.chord(radius=5, start_angle=90, end_angle=180)
        self.tc.create_line.assert_called_with([10, 5, 5, 10])

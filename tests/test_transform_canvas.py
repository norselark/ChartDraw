from unittest.mock import Mock

from chartdraw.lib.transform_canvas import TransformCanvas


tc = TransformCanvas()


def test_circle():
    tc.create_oval = Mock()
    tc.set_center((10, 10))
    tc.circle([0, 0], 2)
    tc.create_oval.assert_called_with([8, 8, 12, 12])


def test_line():
    tc.create_line = Mock()
    tc.set_center((10, 10))
    tc.line([[0, 0], [2, 2]])
    tc.create_line.assert_called_with([10, 10, 12, 12])

    tc.set_rotation(90)
    tc.line([[0, 0], [2, 2]])
    tc.create_line.assert_called_with([10, 10, 12, 8])


def test_chord():
    tc.create_line = Mock()
    tc.set_center((10, 10))
    tc.chord(radius=5, start_angle=90, end_angle=180)
    tc.create_line.assert_called_with([10, 5, 5, 10])

"""Testing for Chua system.
"""

import pytest
from src.attractors.attractor import BaseAttractor


@pytest.mark.parametrize("num_points, length", [(-10, 0), (0, 0), (10, 10)])
def test_initialized_coordinates(num_points, length):
    model = BaseAttractor(num_points=num_points)
    model.process_in_time()
    assert len(model) == length, f"[FAIL]: Expected len is {length} for positive integers only!"


def test_check_reset_coordinates():
    model = BaseAttractor(num_points=100)
    assert model.coordinates is None, f"[FAIL]: Coordinates should be None!"
    model.process_in_time()
    assert len(model) == 100, f"[FAIL]: Expected len is {model.num_points} for positive integers only!"
    model.reset_coordinates()
    assert len(model) == 0, f"[FAIL]: Len should be 0!"
    assert model.coordinates is None, f"[FAIL]: Coordinates should be None!"

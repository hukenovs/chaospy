"""Testing for Chua system.
"""

import pytest
from src.attractors.attractor import BaseAttractor


@pytest.fixture
def chaotic_system():
    return BaseAttractor


@pytest.mark.parametrize("num_points, length", [(-10, 0), (0, 0), (10, 10)])
def test_initialized_coordinates(num_points, length):
    model = BaseAttractor(num_points=num_points)
    assert len(model) == length, f"[FAIL]: Expected len is {length} for positive integers only!"


def test_check_reset_coordinates():
    model = BaseAttractor(num_points=100)
    assert model._coordinates is None, f"[FAIL]: Coordinates should be None!"
    assert len(model) == 100, f"[FAIL]: Expected len is {model.num_points} for positive integers only!"
    del model.coordinates
    assert model._coordinates is None, f"[FAIL]: Coordinates should be None!"


@pytest.mark.parametrize(
    "num_points, initial_points, result", [(1, (0, 0, 0), None), (1, (0, 0, 0), None),],
)
def test_math_moments(num_points, initial_points, result, assert_moments):
    assert_moments(num_points, initial_points, result)

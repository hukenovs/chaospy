"""Testing for Drawer
"""

import matplotlib.pyplot as plt
import numpy as np
import pytest
from src.utils.drawer import PlotDrawer


@pytest.fixture(name="drawer")
def drawer():
    """Return PlotDrawer object with default parameters."""
    return PlotDrawer(save_plots=False, show_plots=False)


@pytest.mark.parametrize(
    "coordinates",
    [
        np.random.randn(10, 3),
        np.zeros(15).reshape(5, 3),
        np.ones((3, 7)).T,
        np.array([[0, 1, 2], [3, 4, 5], [0, 0, 0], [7, 7, 7]]),
        np.array([ii for ii in range(30)]).reshape(-1, 3),
        np.array([[0, 1, 2]] * 10),
    ],
)
def test_shapes_of_coordinates(drawer, coordinates):
    """Test input coordinates from iterable sources. Shape[1] shoud be 3"""
    drawer.show_time_plots(coordinates)
    plt.close()  # disable matplotlib warnings
    drawer.show_3d_plots(coordinates)
    plt.close()  # disable matplotlib warnings
    assert coordinates.shape[1] == 3, f"[FAIL]: Expected shape of vector coordinates is 3!"

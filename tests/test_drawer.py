"""Testing for Drawer
"""

import matplotlib.pyplot as plt
import numpy as np
import pytest
from src.utils.drawer import PlotDrawer


@pytest.fixture(name="drawer")
def drawer():
    return PlotDrawer(save_plots=False, show_plots=False)


@pytest.mark.parametrize(
    "coordinates",
    [
        np.random.randn(10, 3),
        np.zeros(15).reshape(-1, 3),
        np.ones((3, 7)).T,
        np.array([[0, 1, 2], [3, 4, 5], [0, 0, 0], [7, 7, 7]]),
    ],
)
def test_shapes_of_coordinates(drawer, coordinates):
    drawer.show_time_plots(coordinates)
    plt.close()  # disable matplotlib warnings
    drawer.show_3d_plots(coordinates)
    plt.close()  # disable matplotlib warnings
    assert coordinates.shape[1] == 3, f"[FAIL]: Expected shape of vector coordinates is 3!"

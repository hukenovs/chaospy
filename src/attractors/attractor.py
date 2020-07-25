"""Main attractor

Description   :
    Attractor base class.
    It implements abstract method (Chua, Lorenz, Duffing system).
    Can check some parameters for each chaotic system.

------------------------------------------------------------------------

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (c) 2019 Kapitanov Alexander

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT
WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT
NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND
PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE
DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
OR CORRECTION.

------------------------------------------------------------------------
"""

# Authors       : Alexander Kapitanov
# ...
# Contacts      : <empty>
# ...
# Release Date  : 2020/07/16
# License       : GNU GENERAL PUBLIC LICENSE

from abc import abstractmethod
from typing import Tuple

import numpy as np
from scipy.stats import kurtosis, skew
from src.utils.drawer import PlotDrawer

CHARGS = {
    "chua": {"alpha": 0.1, "beta": 28, "mu0": -1.143, "mu1": -0.714},
    "duffing": {"a": 0.1, "b": 11},
    "lorenz": {"sigma": 10, "beta": 8 / 3, "rho": 28},
    "rikitake": {"a": 1, "mu": 1},
    "rossler": {"a": 0.2, "b": 0.2, "c": 5.7},
}


class BaseAttractor:
    """Base class for 3D chaotic system.

    Warning: Do not use this class directly. Use derived classes instead.

    Parameters
    ----------
    num_points: int
        Number of points for X, Y, Z coordinates.

    init_point: tuple
        Initial point [x0, y0, z0] for chaotic attractor system.
        Do not use zeros or very big values because of unstable behavior of dynamic system.
        Default: x, y, z == 1e-4.

    step: float / int
        Step for the next coordinate of dynamic system. Default: 1.0.

    nfft: int
        Number of points for Fast Fourier transform. Default: 1024.

    Examples
    --------
    >>> from src.attractors.attractor import BaseAttractor
    >>> coordinates = (0, 1, -1)
    >>> model = BaseAttractor(num_points=10, init_point=(0.1, 2, -0.5), step=10)
    >>> print(model.coordinates)
    [[ 0.1         2.         -0.5       ]
     [ 0.11        2.2        -0.55      ]
     [ 0.121       2.42       -0.605     ]
     [ 0.1331      2.662      -0.6655    ]
     [ 0.14641     2.9282     -0.73205   ]
     [ 0.161051    3.22102    -0.805255  ]
     [ 0.1771561   3.543122   -0.8857805 ]
     [ 0.19487171  3.8974342  -0.97435855]
     [ 0.21435888  4.28717762 -1.07179441]
     [ 0.23579477  4.71589538 -1.17897385]]
    >>> model.check_moments(is_global=True)
    Mean      : 0.84999
    Variance  : 3.15038
    Skewness  : 0.78675
    Kurtosis  : -0.7909
    Median    : 0.15373

    See Also:
    -----
    Chaotic theory:
    https://en.wikipedia.org/wiki/Chaos_theory
    Attractors (dynamical systems):
    https://en.wikipedia.org/wiki/Attractor
    """

    def __init__(
        self,
        num_points: int,
        init_point: Tuple[float, float, float] = (1e-4, 1e-4, 1e-4),
        step: float = 1.0,
        nfft: int = 1024,
        show_log: bool = False,
        save_plots: bool = False,
    ):
        if show_log:
            print(f"[INFO]: Initialize chaotic system: {self.__class__.__name__}")
        self.num_points = num_points
        self.init_point = init_point
        self.step = step
        self.nfft = nfft
        self.show_log = show_log
        # Internal attributes
        self._coordinates = None
        # Plot drawer
        self.drawer = PlotDrawer(self.__class__.__name__, self.coordinates, self.num_points, save_plots,)

    @property
    def coordinates(self):
        if self._coordinates is None:
            self._coordinates = np.array(list(next(self)))
        return self._coordinates

    @coordinates.deleter
    def coordinates(self):
        self._coordinates = None

    def __len__(self):
        return len(self.coordinates)

    def __iter__(self):
        return self

    def __next__(self):
        coordinates = self.init_point
        for _ in range(self.num_points):
            yield coordinates
            next_coordinates = self.attractor(*coordinates)
            coordinates = tuple(prev + curr / self.step for prev, curr in zip(coordinates, next_coordinates))

    # def __next__(self):
    #     if self.coordinates is None:
    #         self.coordinates = self.init_point
    #         return self.coordinates
    #
    #     next_coordinates = self.attractor(*self.coordinates, **self.kwargs)
    #     self.coordinates = tuple(prev + curr / self.step for prev, curr in zip(self.coordinates,
    #     next_coordinates))
    #     return self.coordinates

    @abstractmethod
    def attractor(self, x: float, y: float, z: float, **kwargs) -> Tuple[float, float, float]:
        """Calculate the next coordinate X, Y, Z for chaotic system.
        Do not use this method for parent BaseAttractor class.

        Parameters
        ----------
        x, y, z : float
            Input coordinates: X, Y, Z respectively

        Returns
        -------
        result: tuple
            The next coordinates: X, Y, Z respectively
        """
        # raise NotImplementedError
        return x, y, z

    def check_min_max(self) -> Tuple[float, float]:
        """Calculate minimum and maximum for X, Y, Z coordinates.
        """
        return np.min(self.coordinates, axis=0), np.max(self.coordinates, axis=0)

    def check_moments(self, is_global: bool = False) -> dict:
        """Calculate stochastic parameters: mean, variance, skewness, kurtosis etc.

        Parameters
        ----------
        is_global : bool
            If is_global is False: return moments for each coordinate. Otherwise
            return moments over all ndarray. Similar for axis or axes along which the moments are computed.
            The default is to compute the moments for each coordinate.

        """
        axis = None if is_global else 0
        return {
            "Mean": np.mean(self.coordinates, axis=axis),
            "Variance": np.var(self.coordinates, axis=axis),
            "Skewness": skew(self.coordinates, axis=axis),
            "Kurtosis": kurtosis(self.coordinates, axis=axis),
            "Median": np.median(self.coordinates, axis=axis),
        }

    def check_probability(self):
        pass
        # TODO: Implement this method!

    def __call__(self, save_plots: bool = False):
        if self.show_log:
            print("\n[INFO]: Calculate mean, variance, skewness, kurtosis and median for chaotic system:")
        _moments = self.check_moments()
        for _key in _moments:
            print(f"{_key:<10}: {_moments[_key]}")

        if self.show_log:
            print("\n[INFO]: Calculate moments:")
        _global_moments = self.check_moments(is_global=True)
        for _key in _global_moments:
            print(f"{_key:<10}: {_global_moments[_key]}")

        self.drawer.show_3d_plots()


if __name__ == "__main__":

    model = BaseAttractor(num_points=10, init_point=(0.1, 2, -0.5), step=10, nfft=32)
    print(model.coordinates)
    model()

"""Main attractor

Description   :
    Attractor base class. It implements abstract method (Chua, Lorenz, Duffing system).
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

import numpy as np
from scipy.stats import kurtosis, skew
from typing import Tuple
from abc import abstractmethod


class BaseAttractor:
    """Base class for chaotic system.

    Warning: Do not use this class directly. Use derived classes instead.

    """
    def __init__(
            self,
            num_points: int,
            init_point: Tuple[float, float, float] = (0, 0, 0),
            step: int = 1,
            nfft: int = 1024,
            **kwargs
    ):
        self.num_points = num_points
        self.init_point = init_point
        self.step = step
        self.nfft = nfft
        self.kwargs = kwargs
        self.coordinates = None

    @abstractmethod
    def attractor(self, x: float, y: float, z: float) -> Tuple[float, float, float]:
        """Calculate the next coordinate X, Y, Z for chaotic system.

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

    def reset_coordinates(self):
        """Reset coordinates to zeros: X, Y, Z = 0"""
        self.coordinates = np.zeros(shape=(self.num_points, 3), dtype=float)

    def _step_coordinates(self, coordinates: Tuple[float, float, float]):
        """Make generator for coordinates.
        """
        for i in range(self.num_points):
            yield coordinates
            next_coordinates = self.attractor(*coordinates, **self.kwargs)
            coordinates = tuple(prev + curr / self.step for prev, curr in zip(coordinates, next_coordinates))

    def process_in_time(self):
        """Collect coordinates from time with time step and initial point.
        """
        self.coordinates = np.array(list(self._step_coordinates(self.init_point)), dtype=float)

    @staticmethod
    def check_min_max(coordinates: np.array) -> Tuple[float, float]:
        """Calculate minimum and maximum for X, Y, Z coordinates.
        """
        return np.min(coordinates, axis=0), np.max(coordinates, axis=0)

    @staticmethod
    def check_moments(coorditanes: np.array) -> dict:
        """Calculate stochastic parameters: mean, variance, skewness, kurtosis etc.

        """
        return {"Mean": np.mean(coorditanes, axis=0),
                "Variance": np.var(coorditanes, axis=0),
                "Skewness": skew(coorditanes, axis=0),
                "Kurtosis": kurtosis(coorditanes, axis=0),
                "Median": np.median(coorditanes, axis=0)}


if __name__ == '__main__':
    chaotic_attractor = BaseAttractor(num_points=10, init_point=(1, 2, 3), step=10, nfft=1024)
    print(f"Start analyzing {chaotic_attractor.__class__.__name__} chaotic system: \n")
    chaotic_attractor.process_in_time()
    xyz = chaotic_attractor.coordinates
    print("Calculate mean, variance, skewness, kurtosis and median for each " "coordinate of chaotic system:")

    moments = chaotic_attractor.check_moments(xyz)
    for key in moments:
        print(f"{key:<10}: {moments[key]}")

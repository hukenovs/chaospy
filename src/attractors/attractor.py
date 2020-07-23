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

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis, skew

CHARGS = {
    "chua": {"alpha": 0.1, "beta": 28, "mu0": -1.143, "mu1": -0.714},
    "duffing": {"a": 0.1, "b": 11},
    "lorenz": {"sigma": 10, "beta": 8 / 3, "rho": 28},
    "rikitake": {"a": 1, "mu": 1},
    "rossler": {"a": 0.2, "b": 0.2, "c": 5.7},
}


class BaseAttractor:
    """Base class for chaotic system.

    Warning: Do not use this class directly. Use derived classes instead.

    """

    def __init__(
        self,
        num_points: int,
        init_point: Tuple[float, float, float] = (1e-4, 1e-4, 1e-4),
        step: int = 1,
        nfft: int = 1024,
    ):
        self.num_points = num_points
        self.init_point = init_point
        self.step = step
        self.nfft = nfft
        self.coordinates = None

    def __len__(self):
        if self.coordinates is not None:
            return len(self.coordinates)
        return 0
        # raise TypeError("[FAIL]: Initialize coordinates for chaotic attractor!")

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
        self.coordinates = None

    def process_in_time(self):
        """Collect coordinates from time with time step and initial point.
        """
        # self.coordinates =  np.array([self.__next__() for _ in range(self.num_points)])
        if self.coordinates is None:
            self.coordinates = np.array(list(next(self)))

    @staticmethod
    def check_min_max(coordinates: np.array) -> Tuple[float, float]:
        """Calculate minimum and maximum for X, Y, Z coordinates.
        """
        return np.min(coordinates, axis=0), np.max(coordinates, axis=0)

    @staticmethod
    def check_moments(coorditanes: np.array) -> dict:
        """Calculate stochastic parameters: mean, variance, skewness, kurtosis etc.
        """
        return {
            "Mean": np.mean(coorditanes, axis=0),
            "Variance": np.var(coorditanes, axis=0),
            "Skewness": skew(coorditanes, axis=0),
            "Kurtosis": kurtosis(coorditanes, axis=0),
            "Median": np.median(coorditanes, axis=0),
        }

    def check_probability(self):
        pass
        # TODO: Implement this method!

    def show_time_plots(self, save_plots: bool = False):
        """Plot 3D coordinates as time series."""
        plt.figure("Coordinates evolution in time", figsize=(8, 6), dpi=100)
        for ii, axis in enumerate(["X", "Y", "Z"]):
            plt.subplot(3, 1, ii + 1)
            plt.plot(self.coordinates[:, ii], linewidth=0.75)
            plt.grid(True)
            if axis == "Z":
                plt.xlabel("Time")
            plt.ylabel(axis)
            plt.xlim([0, self.num_points - 1])
        plt.tight_layout()
        if save_plots:
            plt.savefig(f"{self.__class__.__name__}_coordinates.png")
        plt.show()

    def __call__(self, save_plots: bool = False):
        # Collect coordinates
        self.process_in_time()
        _xyz = self.coordinates
        print("\n[INFO]: Calculate mean, variance, skewness, kurtosis and median for chaotic system:")
        _moments = self.check_moments(_xyz)
        for _key in _moments:
            print(f"{_key:<10}: {_moments[_key]}")
        self.show_time_plots(save_plots=save_plots)


if __name__ == "__main__":
    chaotic_attractor = BaseAttractor(num_points=10, init_point=(1, 5, -0.1), step=100, nfft=1024)
    print(f"\n[INFO]: Start analyzing {chaotic_attractor.__class__.__name__} chaotic system: \n")
    chaotic_attractor.process_in_time()
    print(chaotic_attractor.coordinates)

    xyz = chaotic_attractor.coordinates
    print("\n[INFO]: Calculate mean, variance, skewness, kurtosis and median for each " "coordinate of chaotic system:")
    moments = chaotic_attractor.check_moments(xyz)
    for key in moments:
        print(f"{key:<10}: {moments[key]}")

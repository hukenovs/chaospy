"""Chaotic system calculator.

Description:
    Useful component for calculate some parameters:
       math moments, FFTs, min and max values etc.

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
# Release Date  : 2020/07/25
# License       : GNU GENERAL PUBLIC LICENSE

from typing import Tuple

import numpy as np
from scipy.stats import gaussian_kde, kurtosis, skew


class Calculator:
    """Main class for calculate math parameters.

    See Also:
    -----

    """

    def __init__(self, kde_dots: int = 1000):
        self.kde_dots = kde_dots
        self._coordinates = None

    def __len__(self):
        return len(self.coordinates)

    @property
    def coordinates(self) -> np.ndarray:
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value: np.ndarray):
        """3D coordinates.

        Parameters
        ----------
        value : np.ndarray
            Numpy 3D array of dynamic system coordinates.

        """
        self._coordinates = value

    def check_min_max(self) -> Tuple[np.ndarray, np.ndarray]:
        """Calculate minimum and maximum for X, Y, Z coordinates.
        """
        return np.min(self.coordinates, axis=0), np.max(self.coordinates, axis=0)

    def check_moments(self, is_common: bool = False) -> dict:
        """Calculate stochastic parameters: mean, variance, skewness, kurtosis etc.

        Parameters
        ----------
        is_common : bool
            If False - method returns moments for each coordinate. Otherwise
            returns moments over all ndarray. Similar for axis or axes along
            which the moments are computed.
            The default is to compute the moments for each coordinate.
        """
        axis = None if is_common else 0
        return {
            "Mean": np.mean(self.coordinates, axis=axis),
            "Variance": np.var(self.coordinates, axis=axis),
            "Skewness": skew(self.coordinates, axis=axis),
            "Kurtosis": kurtosis(self.coordinates, axis=axis),
            "Median": np.median(self.coordinates, axis=axis),
        }

    def check_probability(self):
        p_axi = np.zeros([3, self.kde_dots])
        d_kde = np.zeros([3, self.kde_dots])
        for ii in range(3):
            p_axi[ii] = np.linspace(self.coordinates[ii, :].min(), self.coordinates[ii, :].max(), self.kde_dots)
            d_kde[ii] = gaussian_kde(self.coordinates[ii, :]).evaluate(p_axi[ii, :])
            d_kde[ii] /= d_kde[ii].max()
        return d_kde

    def calculate_fft(self):
        pass
        # TODO: Implement this method!


if __name__ == "__main__":
    calc = Calculator()

    num_dots = 10000
    np.random.seed(42)
    calc.coordinates = np.random.randn(num_dots, 3)

    dd_kde = calc.check_probability()
    import matplotlib.pyplot as plt

    print(dd_kde.shape)
    plt.figure("Probability density function")
    for ii in range(dd_kde.shape[0]):
        plt.plot(dd_kde[ii], ".")
        # plt.xlim([0, dd_kde.shape[1] - 1])
        plt.grid()
    plt.tight_layout()
    plt.show()

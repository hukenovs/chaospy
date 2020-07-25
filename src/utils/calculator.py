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
from scipy.stats import kurtosis, skew


class Calculator:
    """Main class for calculate math parameters.

    See Also:
    -----

    """

    def __init__(self):
        pass

    @staticmethod
    def check_min_max(coordinates: np.array) -> Tuple[float, float]:
        """Calculate minimum and maximum for X, Y, Z coordinates.

        Parameters
        ----------
        coordinates: np.array
            Numpy 3D array of dynamic system coordinates.
        """
        return np.min(coordinates, axis=0), np.max(coordinates, axis=0)

    @staticmethod
    def check_moments(coordinates: np.array, is_common: bool = False) -> dict:
        """Calculate stochastic parameters: mean, variance, skewness, kurtosis etc.

        Parameters
        ----------
        coordinates: np.array
            Numpy 3D array of dynamic system coordinates.

        is_common : bool
            If False method returns moments for each coordinate. Otherwise
            returns moments over all ndarray. Similar for axis or axes along
            which the moments are computed.
            The default is to compute the moments for each coordinate.

        """
        axis = None if is_common else 0
        return {
            "Mean": np.mean(coordinates, axis=axis),
            "Variance": np.var(coordinates, axis=axis),
            "Skewness": skew(coordinates, axis=axis),
            "Kurtosis": kurtosis(coordinates, axis=axis),
            "Median": np.median(coordinates, axis=axis),
        }

    def check_probability(self):
        pass
        # TODO: Implement this method!

    def calculate_fft(self):
        pass
        # TODO: Implement this method!


if __name__ == "__main__":
    pass

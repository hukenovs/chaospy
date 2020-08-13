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

    Examples
    --------
    >>> from src.attractors.attractor import BaseAttractor
    >>> coordinates = (0, 1, -1)
    >>> model = BaseAttractor(num_points=10, init_point=(0.1, 2, -0.5), step=10)
    >>> print(model.get_coordinates())
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
    >>> print(len(model))
    10
    >>> model.update_attributes(num_points=1, init_point=(0, 1, 2), nfft=8)
    >>> model.__dict__
    {'num_points': 1, 'init_point': (0, 1, 2), 'step': 10, 'nfft': 8, '_coordinates': None}
    >>> len(model)
    1

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
        show_log: bool = False,
        **kwargs: dict,
    ):
        if show_log:
            print(f"[INFO]: Initialize chaotic system: {self.__class__.__name__}\n")
        self.num_points = num_points
        self.init_point = init_point
        self.step = step
        self.kwargs = kwargs

    def get_coordinates(self):
        return np.array(list(next(self)))

    def __len__(self):
        return self.num_points

    def __iter__(self):
        return self

    def __next__(self):
        points = self.init_point
        for _ in range(self.num_points):
            yield points
            next_points = self.attractor(*points, **self.kwargs)
            points = tuple(prev + curr / self.step for prev, curr in zip(points, next_points))

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
        return x + y + z, y - z, x ** 2 - z ** 2

    def update_attributes(self, **kwargs):
        """Update chaotic system parameters."""
        for key in kwargs:
            if key in self.__dict__ and not key.startswith("_"):
                self.__dict__[key] = kwargs.get(key)


if __name__ == "__main__":

    base_model = BaseAttractor(num_points=10, init_point=(-0.01, 0.5, 2), step=100)
    print(f"Model attributes: {base_model.__dict__}")
    print(f"Model length: {len(base_model)}")
    xyz = base_model.get_coordinates()
    print(xyz)

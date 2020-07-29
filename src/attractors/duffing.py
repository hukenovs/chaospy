"""Duffing map.

Description:
    Duffing map. It is a discrete-time dynamical system (2nd order)
    The map depends on the two constants: a and b.
    Z coordinate is a linear function.

    Duffing equations are:
    Eq. 1:
        dx/dt = y
        dy/dt = -a*y - x**3 + b * cos(z)
        dz/dt = 1
    where a = 0.1 and b = 11 (default parameters)

    Eq. 2:
        dx/dt = y
        dy/dt = a*y - y**3 - b*x
        dz/dt = 1
    where a = 2.75 and b = 0.2 (default parameters)

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
# Release Date  : 2019/05/31
# License       : GNU GENERAL PUBLIC LICENSE

from math import cos
from typing import Tuple

from src.attractors.attractor import BaseAttractor


class Duffing(BaseAttractor):
    """Duffing attractor."""

    def attractor(
        self, x: float, y: float, z: float, alpha: float = 0.1, beta: float = 11
    ) -> Tuple[float, float, float]:
        """Calculate the next coordinate X, Y, Z for 3rd-order Duffing map.
        It is 2nd order attractor (Z coordinate = 1)

        Parameters
        ----------
        x, y, z : float
            Input coordinates X, Y, Z respectively
        alpha, beta: float
            Duffing map parameters. Default:
                - alpha = 0.1,
                - beta = 11,

        Examples
        --------
        >>> from src.attractors.duffing import Duffing
        >>> coordinates = (0, 1, -1)
        >>> model = Duffing(num_points=1)
        >>> output = model.attractor(*coordinates)
        >>> print(output)
        (1, 5.843325364549537, 1)
        >>> model = Duffing(num_points=10, init_point=(0.1, 0, -0.1), step=100)
        >>> print(model.get_coordinates())
        [[ 0.1         0.         -0.1       ]
         [ 0.1         0.10944046 -0.09      ]
         [ 0.1010944   0.21887582 -0.08      ]
         [ 0.10328316  0.3282948  -0.07      ]
         [ 0.10656611  0.4376861  -0.06      ]
         [ 0.11094297  0.54703837 -0.05      ]
         [ 0.11641336  0.6563402  -0.04      ]
         [ 0.12297676  0.7655801  -0.03      ]
         [ 0.13063256  0.87474642 -0.02      ]
         [ 0.13938002  0.98382738 -0.01      ]]

        See Also
        -----
        Duffing map (attractor):
        https://en.wikipedia.org/wiki/Duffing_map
        Duffing equation:
        https://en.wikipedia.org/wiki/Duffing_equation

        """
        x_out = y
        y_out = -alpha * y - x ** 3 + beta * cos(z)
        z_out = 1
        return x_out, y_out, z_out


class DuffingMap(BaseAttractor):
    """Duffing attractor."""

    def attractor(
        self, x: float, y: float, z: float, alpha: float = 2.75, beta: float = 0.2
    ) -> Tuple[float, float, float]:
        """Calculate the next coordinate X, Y, Z for 3rd-order Duffing map.
        It is 2nd order attractor (Z coordinate = 1)

        Parameters
        ----------
        x, y, z : float
            Input coordinates X, Y, Z respectively
        alpha, beta: float
            Duffing map parameters. Default:
                - alpha = 2.75,
                - beta = 0.2,

        Examples
        --------
        >>> from src.attractors.duffing import Duffing
        >>> coordinates = (0, 0.5, -1)
        >>> model = Duffing(num_points=1)
        >>> output = model.attractor(*coordinates)
        >>> print(output)
        (0.5, 5.893325364549537, 1)
        >>> model = Duffing(num_points=10, init_point=(0, 4, -0.1), step=100)
        >>> print(model.get_coordinates())
        [[ 0.          4.         -0.1       ]
         [ 0.04        4.10545046 -0.09      ]
         [ 0.0810545   4.21089917 -0.08      ]
         [ 0.1231635   4.31633113 -0.07      ]
         [ 0.16632681  4.42172673 -0.06      ]
         [ 0.21054407  4.52706105 -0.05      ]
         [ 0.25581469  4.63230318 -0.04      ]
         [ 0.30213772  4.73741548 -0.03      ]
         [ 0.34951187  4.84235276 -0.02      ]
         [ 0.3979354   4.94706145 -0.01      ]]

        See Also
        -----
        Duffing map (attractor):
        https://en.wikipedia.org/wiki/Duffing_map
        Duffing equation:
        https://en.wikipedia.org/wiki/Duffing_equation

        """
        x_out = y
        y_out = alpha * y - y ** 3 - beta * x
        z_out = 1
        return x_out, y_out, z_out


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=1)

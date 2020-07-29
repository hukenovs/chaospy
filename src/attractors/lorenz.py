"""Lorenz Attractor

Description:
    Lorenz attractor is ordinary differential equation (ODE) of 3rd order system.
    In 1963, E. Lorenz developed a simplified mathematical model for
    atmospheric convection.

    Lorenz equations are:
        dx/dt = sigma * (y - x)
        dy/dt = rho * x - y - x * z
        dz/dt = x * y - beta * z

    where:
        beta, rho and sigma - are Lorenz system parameters. Default
    default values for parameters are:
        beta = 8/3,
        rho = 28,
        sigma = 10.

    If rho < 1  then there is only one equilibrium point,
    which is at the origin. This point corresponds to no convection.

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

from typing import Tuple

from src.attractors.attractor import BaseAttractor


class Lorenz(BaseAttractor):
    """Lorenz attractor."""

    def attractor(
        self, x: float, y: float, z: float, sigma: float = 10, beta: float = 8 / 3, rho: float = 28,
    ) -> Tuple[float, float, float]:
        """Calculate the next coordinate X, Y, Z for 3rd-order Lorenz system

        Parameters
        ----------
        x, y, z : float
            Input coordinates X, Y, Z respectively.
        sigma, beta, rho : float
            Lorenz system parameters. Default:
                - sigma = 10,
                - beta = 8/3,
                - rho = 28,

        Examples
        --------
        >>> from src.attractors.lorenz import Lorenz
        >>> coordinates = (0, 1, -1)
        >>> model = Lorenz(num_points=1)
        >>> output = model.attractor(*coordinates)
        >>> print(output)
        (10, -1, 2.6666666666666665)
        >>> model = Lorenz(num_points=10, init_point=(0.1, 0, -0.1), step=100)
        >>> print(model.get_coordinates())
        [[ 0.1         0.         -0.1       ]
         [ 0.09        0.0281     -0.09733333]
         [ 0.08381     0.0531066  -0.09471249]
         [ 0.08073966  0.07612171 -0.09214231]
         [ 0.08027787  0.098042   -0.08962372]
         [ 0.08205428  0.11961133 -0.08715505]
         [ 0.08580998  0.14146193 -0.08473277]
         [ 0.09137518  0.16414681 -0.08235184]
         [ 0.09865234  0.18816564 -0.0800058 ]
         [ 0.10760367  0.21398557 -0.07768669]]

        See Also
        -----
        https://en.wikipedia.org/wiki/Lorenz_system
        """
        x_out = sigma * (y - x)
        y_out = rho * x - y - x * z
        z_out = x * y - beta * z
        return x_out, y_out, z_out


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=1)

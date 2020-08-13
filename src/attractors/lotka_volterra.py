r"""Lotka Volterra attractor.

Description   :
    The Lotka–Volterra equations, also known as the predator–prey equations,
    are a pair of first-order nonlinear differential equations,
    frequently used to describe the dynamics of biological systems in
    which two species interact, one as a predator and the other as prey.

    Chaotic Lotka-Volterra model require a careful tuning of
    parameters and are even less likely to exhibit chaos as the number
    of species increases.

    Lotka–Volterra equations are:
    Eq. 1:
        dx/dt = x * (1 - x - 9*y)
        dy/dt = -y * (1 - 6*x - y + 9*z)
        dz/dt = z * (1 - 3*x - z)

    Be careful! Init parameters of x, y, z should be set right!

    For example, [x, y, z] = [0.6, 0.2, 0.01]

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


class LotkaVolterra(BaseAttractor):
    """Lotka-Volterra attractor."""

    def attractor(self, x: float, y: float, z: float, **kwargs) -> Tuple[float, float, float]:
        r"""Calculate the next coordinate X, Y, Z for 3rd-order Lotka-Volterra system

        Parameters
        ----------
        x, y, z : float
            Input coordinates X, Y, Z respectively.

        Lotka-Volterra does not have initial parameters.

        Examples
        --------
        >>> from src.attractors.lotka_volterra import LotkaVolterra
        >>> coordinates = (0, 1, -1)
        >>> model = LotkaVolterra(num_points=1)
        >>> output = model.attractor(*coordinates)
        >>> print(output)
        (0, 9, -2)
        >>> model = LotkaVolterra(num_points=10, init_point=(0.1, 0.5, -0.1), step=100)
        >>> print(model.get_coordinates())
        [[ 0.1         0.5        -0.1       ]
         [ 0.0964      0.505      -0.1008    ]
         [ 0.09288969  0.51000253 -0.10161809]
         [ 0.08946864  0.51501026 -0.10245436]
         [ 0.08613633  0.52002601 -0.10330888]
         [ 0.08289212  0.5250527  -0.10418173]
         [ 0.07973528  0.53009342 -0.10507301]
         [ 0.07666501  0.53515137 -0.10598281]
         [ 0.07368042  0.54022989 -0.1069112 ]
         [ 0.07078055  0.54533243 -0.1078583 ]]

        See Also
        -----
        https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations
        """
        x_out = x * (1 - x - 9 * y)
        y_out = -y * (1 - 6 * x - y + 9 * z)
        z_out = z * (1 - 3 * x - z)
        return x_out, y_out, z_out


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

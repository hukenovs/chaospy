r"""Rikitake chaotic system.

Description :
    Rikitake system is ordinary differential equation (ODE) of
    3rd order system.
    Rikitake system attempts to explain the reversal of the Earth’s
    magnetic field.

    Rikitake equations are:
        dx/dt = -mu * x + z * y
        dy/dt = -mu * y + x * (z - a)
        dz/dt = 1 - x * y

    where a, mu - are Rikitake system parameters.
    Default values are
        - a = 5,
        - mu = 2
        or

        - a = mu = 1.

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
# Release Date  : 2019/05/30
# License       : GNU GENERAL PUBLIC LICENSE

from typing import Tuple

from src.attractors.attractor import BaseAttractor


class Rikitake(BaseAttractor):
    """Rikitake attractor."""

    def attractor(self, x: float, y: float, z: float, a: float = 5, mu: float = 2) -> Tuple[float, float, float]:
        r"""Calculate the next coordinate X, Y, Z for 3rd-order Rikitake system

        Parameters
        ----------
        x, y, z : float
            Input coordinates X, Y, Z respectively.
        a, mu : float
            Rikitake system parameters. Default:
                - a = 5,
                - mu = 2
            or
                - a = mu = 1.

        Examples
        --------
        >>> from src.attractors.rikitake import Rikitake
        >>> coordinates = (0, 1, -1)
        >>> model = Rikitake(num_points=1)
        >>> output = model.attractor(*coordinates)
        >>> print(output)
        (-1, -2, 1)
        >>> model = Rikitake(num_points=10, init_point=(0.1, 0, -0.1), step=100)
        >>> print(model.get_coordinates())
        [[ 0.1         0.         -0.1       ]
         [ 0.098      -0.0051     -0.09      ]
         [ 0.09604459 -0.0099862  -0.079995  ]
         [ 0.09413169 -0.01466554 -0.06998541]
         [ 0.09225932 -0.01914469 -0.05997161]
         [ 0.09042561 -0.02343009 -0.04995394]
         [ 0.0886288  -0.02752794 -0.03993276]
         [ 0.08686722 -0.03144421 -0.02990836]
         [ 0.08513928 -0.03518467 -0.01988104]
         [ 0.08344349 -0.03875487 -0.00985109]]

        See Also
        -----
        Cannot add wiki link ;(
        """
        x_out = -mu * x + z * y
        y_out = -mu * y + x * (z - a)
        z_out = 1 - x * y

        return x_out, y_out, z_out


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=1)

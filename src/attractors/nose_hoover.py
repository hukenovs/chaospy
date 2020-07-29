r"""Nose-Hoover attractor system.

Description:
    The Nose–Hoover thermostat is a deterministic algorithm for
    constant-temperature molecular dynamics simulations. It was originally
    developed by Nose and was improved further by Hoover.

    Nose–Hoover oscillator is ordinary differential equation (ODE) of
    3rd order system.
    Nose–Hoover system has only five terms and two quadratic
    nonlinearities.

    Nose–Hoover equations are:
        dx/dt = y
        dy/dt = y * z - x
        dz/dt = 1 - y * y

    Nose–Hoover system doesn't have any system parameters.

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
# Release Date  : 2020/07/29
# License       : GNU GENERAL PUBLIC LICENSE

from typing import Tuple

from src.attractors.attractor import BaseAttractor


class NoseHoover(BaseAttractor):
    """Nose Hoover attractor."""

    def attractor(self, x: float, y: float, z: float) -> Tuple[float, float, float]:
        r"""Calculate the next coordinate X, Y, Z for 3rd-order Nose Hoover system

        Parameters
        ----------
        x, y, z : float
            Input coordinates X, Y, Z respectively.

        Examples
        --------
        >>> from src.attractors.nose_hoover import NoseHoover
        >>> coordinates = (0, 1, -1)
        >>> model = NoseHoover(num_points=1)
        >>> output = model.attractor(*coordinates)
        >>> print(output)
        (1, -1, 0)
        >>> model = NoseHoover(num_points=10, init_point=(0.1, 0, -0.1), step=100)
        >>> print(model.get_coordinates())
        [[ 0.1         0.         -0.1       ]
         [ 0.1        -0.001      -0.09      ]
         [ 0.09999    -0.0019991  -0.08000001]
         [ 0.09997001 -0.0029974  -0.07000005]
         [ 0.09994003 -0.003995   -0.06000014]
         [ 0.09990008 -0.00499201 -0.0500003 ]
         [ 0.09985016 -0.00598851 -0.04000055]
         [ 0.09979028 -0.00698462 -0.03000091]
         [ 0.09972043 -0.00798042 -0.0200014 ]
         [ 0.09964063 -0.00897603 -0.01000203]]

        See Also
        -----
        https://en.wikipedia.org/wiki/Nos%C3%A9%E2%80%93Hoover_thermostat

        """
        x_out = y
        y_out = y * z - x
        z_out = 1 - y * y
        return x_out, y_out, z_out


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=1)

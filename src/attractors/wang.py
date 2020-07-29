r"""Wang 3D attractor system. It also has 4D realization.

Description   :
    Wang system (improved Lorenz model) as classic chaotic attractor

    Wang equations are:
        dx/dt = x - y*z
        dy/dt = x - y + x*z
        dz/dt = -3*z + x*y

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


class Wang(BaseAttractor):
    """Wang attractor (it is improved version of Lorenz model)."""

    def attractor(self, x: float, y: float, z: float) -> Tuple[float, float, float]:
        r"""Calculate the next coordinate X, Y, Z for 3rd-order Wang system

        Parameters
        ----------
        x, y, z : float
            Input coordinates X, Y, Z respectively.

        Examples
        --------
        >>> from src.attractors.wang import Wang
        >>> coordinates = (0, 1, -1)
        >>> model = Wang(num_points=1)
        >>> output = model.attractor(*coordinates)
        >>> print(output)
        (1, -1, 3)
        >>> model = Wang(num_points=10, init_point=(0.1, 0, -0.1), step=100)
        >>> print(model.get_coordinates())
        [[ 0.1         0.         -0.1       ]
         [ 0.101       0.0009     -0.097     ]
         [ 0.10201087  0.00180303 -0.09408909]
         [ 0.10303268  0.00270913 -0.09126458]
         [ 0.10406548  0.00361833 -0.08852385]
         [ 0.10510934  0.00453068 -0.08586437]
         [ 0.10616432  0.00544621 -0.08328368]
         [ 0.1072305   0.00636498 -0.08077938]
         [ 0.10830794  0.00728701 -0.07834918]
         [ 0.10939673  0.00821236 -0.07599081]]

        See Also
        -----
        No links.
        """
        x_out = x - y * z
        y_out = x - y + x * z
        z_out = -3 * z + x * y
        return x_out, y_out, z_out


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=1)

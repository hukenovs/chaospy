"""Lottka Volterra attractor.

Description   :
    The Lotka–Volterra equations, also known as the predator–prey
    equations.

    Chaotic Lotka-Volterra model require a careful tuning of
    parameters and are even less likely to exhibit chaos as the number
    of species increases.

    Lotka–Volterra equations are:
    Eq. 1:
        dx/dt = x * (1 - x - 9*y)
        dy/dt = -y * (1 - 6*x - y + 9*z)
        dz/dt = z * (1 - 3*x - z)

    Be careful! Init parameters of x, y, z should be set right.

    For example, [x, y, z] = [0.6; 0.2; 0.01]

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


def lotka_volterra(x: int = 0, y: int = 0, z: int = 1) -> Tuple[int, int, int]:
    """Calculate the next coordinate X, Y, Z for Lotka–Volterra

    Parameters
    ----------
    x, y, z : float
        Input coordinates X, Y, Z respectively
    """

    # Next step coordinates:
    x_out = x * (1 - x - 9 * y)
    y_out = -y * (1 - 6 * x - y + 9 * z)
    z_out = z * (1 - 3 * x - z)

    return x_out, y_out, z_out

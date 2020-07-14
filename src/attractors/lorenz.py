"""Lorenz Attractor

Description   :
    Lorenz attractor is ordinary differential equation (ODE) of
    3rd order system.
    In 1963, E. Lorenz developed a simplified mathematical model for
    atmospheric convection.

    Lorenz equations are:
        dx/dt = sigma * (y - x)
        dy/dt = rho * x - y - x * z
        dz/dt = x * y - beta * z

    where beta, rho and sigma - are Lorenz system parameters. Default
    values are: beta = 8/3, rho = 28 and sigma = 10.

    Wiki: If rho < 1 then there is only one equilibrium point.

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


def lorenz(x: float = 0, y: float = 0, z: float = 1, **kwargs) -> Tuple[float, float, float]:
    """Calculate the next coordinate X, Y, Z for 3rd-order Lorenz system

    Parameters
    ----------
    x, y, z : float
        Input coordinates X, Y, Z respectively
    kwargs : dict
        beta, rho and sigma - are floating point Lorenz system parameters

    """

    # Default Lorenz parameters:
    sigma = kwargs.get("sigma", 10)
    beta = kwargs.get("beta", 8 / 3)
    rho = kwargs.get("rho", 28)

    # Next step coordinates:
    x_out = sigma * (y - x)
    y_out = rho * x - y - x * z
    z_out = x * y - beta * z

    return x_out, y_out, z_out

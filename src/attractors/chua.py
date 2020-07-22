"""Chua attractor

Description   :
    Chua circuit. This is a simple electronic circuit that exhibits
    classic chaotic behavior.

    Chua equations are:
    Eq. 1:
        dx/dt = alpha * (y - x - ht)
        dy/dt = x - y + z
        dz/dt = -beta * y

    where ht = mu1*x + 0.5*(mu0 - mu1)*(np.abs(x + 1) - np.abs(x - 1))
    and alpha, beta, mu0 and mu1 - are Chua system parameters.

    Default values are:
    alpha = 15.6
    beta = 28
    mu0 = -1.143
    mu1 = -0.714

    Eq. 2:
        dx/dt = 0.3*y + x - x**3
        dy/dt = x + z
        dz/dt = y

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

from math import fabs
from typing import Tuple

from src.attractors.attractor import BaseAttractor


class Chua(BaseAttractor):
    """Chua attractor.

    """

    def attractor(
        self,
        x: float,
        y: float,
        z: float,
        alpha: float = 15.6,
        beta: float = 28,
        mu0: float = -1.143,
        mu1: float = -0.714,
    ) -> Tuple[float, float, float]:
        """Calculate the next coordinate X, Y, Z for Chua system.

        Parameters
        ----------
        x, y, z : float
            Input coordinates X, Y, Z respectively

        alpha, beta, mu0, mu1 : float
            Chua initial parameters
        """

        ht = mu1 * x + 0.5 * (mu0 - mu1) * (fabs(x + 1) - fabs(x - 1))
        # Next step coordinates:
        # Eq. 1:
        x_out = alpha * (y - x - ht)
        y_out = x - y + z
        z_out = -beta * y
        return x_out, y_out, z_out


if __name__ == "__main__":
    # chua_defaults = {"alpha": 0.1, "beta": 28, "mu0": -1.143, "mu1": -0.714}
    chua = Chua(num_points=2 ** 10, init_point=(0.0, -0.1, -0.05), step=100, nfft=128)
    chua()

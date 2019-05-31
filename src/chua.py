"""
------------------------------------------------------------------------

Title         : chua.py
Author        : Alexander Kapitanov
E-mail        : sallador@bk.ru
Lang.         : python
Company       :
Release Date  : 2019/05/31

------------------------------------------------------------------------

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
import numpy as np


def chua(x=0, y=0, z=1, **kwargs):
    """
    Calculate the next coordinate X, Y, Z for Chua system.

    Parameters
    ----------
    x, y, z : float
        Input coordinates Z, Y, Z respectively
    kwargs : float
        alpha, beta, mu0, mu1 - are Chua system parameters
    """
    # Default parameters:
    alpha = kwargs.get('alpha', 15.6)
    beta = kwargs.get('beta', 28)
    mu0 = kwargs.get('mu0', -1.143)
    mu1 = kwargs.get('mu1', -0.714)

    ht = mu1*x + 0.5*(mu0 - mu1)*(np.abs(x + 1) - np.abs(x - 1))
    # Next step coordinates:
    # Eq. 1:
    x_out = alpha*(y - x - ht)
    y_out = x - y + z
    z_out = -beta*y
    # Eq. 2:
    # x_out = 0.3*y + x - x**3
    # y_out = x + z
    # z_out = y

    return x_out, y_out, z_out

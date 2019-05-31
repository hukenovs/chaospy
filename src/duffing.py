"""
------------------------------------------------------------------------

Title         : duffing.py
Author        : Alexander Kapitanov
E-mail        : sallador@bk.ru
Lang.         : python
Company       :
Release Date  : 2019/05/31

------------------------------------------------------------------------

Description   :
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
import numpy as np


def duffing(x=0, y=0, z=0, **kwargs):
    """
    Calculate the next coordinate X, Y, Z for Duffing map.
    It is 2nd order attractor (Z coordinate = 1)

    Duffing map:
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

    Parameters
    ----------
    x, y, z : float
        Input coordinates Z, Y, Z respectively
    kwargs : float
        a and b - are Duffing system parameters
    """
    # Default parameters:
    # a = kwargs.get('a', 2.75)
    # b = kwargs.get('b', 0.2)
    a = kwargs.get('a', 0.1)
    b = kwargs.get('b', 11)

    # Next step coordinates:
    x_out = y
    y_out = -a*y - x**3 + b*np.cos(z)
    # y_out = a*y - y**3 - b*x
    z_out = 1
    return x_out, y_out, z_out

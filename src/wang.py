"""
------------------------------------------------------------------------

Title         : wang.py
Author        : Alexander Kapitanov
E-mail        : sallador@bk.ru
Lang.         : python
Company       :
Release Date  : 2019/05/31

------------------------------------------------------------------------

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


def wang(x=0, y=0, z=0):
    """
    Calculate the next coordinate X, Y, Z for 3rd-order Wang Attractor

    Parameters
    ----------
    x, y, z : float
        Input coordinates Z, Y, Z respectively
    """
    # Next step coordinates:
    x_out = x - y*z
    y_out = x - y + x*z
    z_out = -3*z + x*y
    return x_out, y_out, z_out

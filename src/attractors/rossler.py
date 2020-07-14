"""Rossler attractor (see 'Strange attractors' book).

Description   :
    Rossler attractor is the attractor for the Rössler system. Rossler
    attractor is a system of three non-linear ordinary differential
    equations.

    Rossler equations are:
        dx/dt = -(y + z)
        dy/dt = x + a * y
        dz/dt = b + z * (x - c)

    where a, b and sigma - are Rossler system parameters. Default
    values are: a = 0.2, b = 0.2 and c = 5.7.

    1) a = 0.2, b = 0.2 and c = 5.7 (Standard model)
    2) a = 0.1, b = 0.1 and c = 14 (another useful parameters)
    3) a = 0.5, b = 1.0 and c = 3 (J. C. Sprott)

    Wiki (Varying parameters);

    Varying a:
    b = 0.2 and c = 5.7 are fixed. Change a:

    a <= 0	    : Converges to the centrally located fixed point
    a = 0.1	    : Unit cycle of period 1
    a = 0.2	    : Standard parameter value selected by Rössler, chaotic
    a = 0.3     : Chaotic attractor, significantly more Möbius strip-like
                (folding over itself).
    a = 0.35    : Similar to .3, but increasingly chaotic
    a = 0.38    : Similar to .35, but increasingly chaotic

    Varying b:
    a = 0.2 and c = 5.7 are fixed. Change b:

    If b approaches 0 the attractor approaches infinity, but if b would
    be more than a and c, system becomes not a chaotic.

    Varying c:
    a = b = 0.1 are fixed. Change c:

    c = 4       : period-1 orbit,
    c = 6       : period-2 orbit,
    c = 8.5     : period-4 orbit,
    c = 8.7     : period-8 orbit,
    c = 9       : sparse chaotic attractor,
    c = 12      : period-3 orbit,
    c = 12.6    : period-6 orbit,
    c = 13      : sparse chaotic attractor,
    c = 18      : filled-in chaotic attractor.

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


def rossler(x: float = 0, y: float = 0, z: float = 1, **kwargs) -> Tuple[float, float, float]:
    """Calculate the next coordinate X, Y, Z for 3rd-order Rossler system

    Parameters
    ----------
    x, y, z : float
        Input coordinates X, Y, Z respectively
    kwargs : dict
        a, b and c - are Rossler system parameters

    """

    # Default Rossler parameters:
    a = kwargs.get("a", 0.2)
    b = kwargs.get("b", 0.2)
    c = kwargs.get("c", 5.7)

    # Next step coordinates:
    x_out = -(y + z)
    y_out = x + a * y
    z_out = b + z * (x - c)

    return x_out, y_out, z_out

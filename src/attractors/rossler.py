r"""Rossler attractor (see 'Strange attractors' book).

Description :
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

    a <= 0      : Converges to the centrally located fixed point
    a = 0.1     : Unit cycle of period 1
    a = 0.2     : Standard parameter value selected by Rössler, chaotic
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

from src.attractors.attractor import BaseAttractor


class Rossler(BaseAttractor):
    """Rossler attractor."""

    def attractor(
        self, x: float, y: float, z: float, a: float = 0.2, b: float = 0.2, c: float = 5.7,
    ) -> Tuple[float, float, float]:
        r"""Calculate the next coordinate X, Y, Z for 3rd-order Rossler system

        Parameters
        ----------
        x, y, z : float
            Input coordinates X, Y, Z respectively.
        a, b, c : float
            Rossler system parameters. Default:
            1) a = 0.2, b = 0.2 and c = 5.7 (Standard model)
            2) a = 0.1, b = 0.1 and c = 14 (another useful parameters)
            3) a = 0.5, b = 1.0 and c = 3 (J. C. Sprott)

        Examples
        --------
        >>> from src.attractors.rossler import Rossler
        >>> coordinates = (0, 1, -1)
        >>> model = Rossler(num_points=1)
        >>> output = model.attractor(*coordinates)
        >>> print(output)
        (0, 0.2, 5.9)
        >>> model = Rossler(num_points=10, init_point=(0.1, 0, -0.1), step=100)
        >>> print(model.get_coordinates())
        [[ 0.1         0.         -0.1       ]
         [ 0.101       0.001      -0.0924    ]
         [ 0.101914    0.002012   -0.08522652]
         [ 0.10274615  0.00303516 -0.07845547]
         [ 0.10350035  0.0040687  -0.07206412]
         [ 0.1041803   0.00511184 -0.06603105]
         [ 0.10478949  0.00616386 -0.06033607]
         [ 0.10533122  0.00722409 -0.05496014]
         [ 0.10580858  0.00829185 -0.0498853 ]
         [ 0.10622451  0.00936652 -0.04509462]]

        See Also
        -----
        https://en.wikipedia.org/wiki/R%C3%B6ssler_attractor
        """
        x_out = -(y + z)
        y_out = x + a * y
        z_out = b + z * (x - c)

        return x_out, y_out, z_out


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

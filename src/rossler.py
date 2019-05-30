"""
------------------------------------------------------------------------

Title         : rossler.py
Author        : Alexander Kapitanov
E-mail        : sallador@bk.ru
Lang.         : python
Company       :
Release Date  : 2019/05/30

------------------------------------------------------------------------

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

    Also you can set: a = 0.1, b = 0.1 and c = 14.

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

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  # noqa: F401 unused import

# #####################################################################
# Function declaration
# #####################################################################


def rossler(x=0, y=0, z=0, **kwargs):
    """
    Calculate the next coordinate X, Y, Z for 3rd-order Rossler system

    Parameters
    ----------
    x, y, z : float
        Input coordinates Z, Y, Z respectively
    kwargs : float
        a, b and c - are Rossler system parameters

    """
    # Default Rossler parameters:
    aa = kwargs.get('a', 0.2)
    bb = kwargs.get('b', 0.2)
    cc = kwargs.get('c', 5.7)

    # Next step coordinates:
    x_out = -(y + z)
    y_out = x + aa * y
    z_out = bb + z * (x - cc)
    return x_out, y_out, z_out


# #####################################################################
# Calculate attractor
# #####################################################################

NW = 20000              # Number of points
dt = 100                # Step for equations (leave default as 100)

# Create zero arrays for coordinates
xt = np.zeros(NW)
yt = np.zeros(NW)
zt = np.zeros(NW)

# Set initial values for [X, Y, Z]
xt[0], yt[0], zt[0] = 1.0, 1.0, 0.0

# Set system parameters
params = {
    'a': 0.2,
    'b': 0.2,
    'c': 5.7
}

# Calculate the next coordinates of system
for i in range(NW-1):
    x_next, y_next, z_next = rossler(xt[i], yt[i], zt[i], **params)
    xt[i+1] = xt[i] + (x_next / dt)
    yt[i+1] = yt[i] + (y_next / dt)
    zt[i+1] = zt[i] + (z_next / dt)

# #####################################################################
# Plot results
# #####################################################################

# Plot 3D model
fig = plt.figure('3D model of chaotic system')

ax = fig.gca(projection='3d')
ax.plot(xt, yt, zt, 'o-', linewidth=0.2, markersize=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Rossler Attractor")

# Plot 2D coordinates in time axis
lin = plt.figure('Coordinates evolution in time')

plt.subplot(3, 1, 1)
plt.plot(xt)
plt.grid()
plt.ylabel('X')

plt.subplot(3, 1, 2)
plt.plot(yt)
plt.grid()
plt.ylabel('Y')

plt.subplot(3, 1, 3)
plt.plot(zt)
plt.grid()
plt.ylabel('Z')

plt.tight_layout()
plt.xlabel('time')

plt.show()

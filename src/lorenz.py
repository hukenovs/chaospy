"""
------------------------------------------------------------------------

Title         : lorenz.py
Author        : Alexander Kapitanov
E-mail        : sallador@bk.ru
Lang.         : python
Company       :
Release Date  : 2019/05/30

------------------------------------------------------------------------

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

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  # noqa: F401 unused import

# #####################################################################
# Function declaration
# #####################################################################


def lorenz(x=0, y=0, z=0, **kwargs):
    """
    Calculate the next coordinate X, Y, Z for 3rd-order Lorenz system

    Parameters
    ----------
    x, y, z : float
        Input coordinates Z, Y, Z respectively
    kwargs : float
        beta, rho and sigma - are Lorenz system parameters

    """
    # Default Lorenz parameters:
    sigma = kwargs.get('sigma', 10)
    beta = kwargs.get('beta', 8/3)
    rho = kwargs.get('rho', 28)

    # Next step coordinates:
    x_out = sigma * (y - x)
    y_out = rho*x - y - x*z
    z_out = x*y - beta*z
    return x_out, y_out, z_out


# #####################################################################
# Calculate attractor
# #####################################################################

NW = 10000              # Number of points
dt = 100                # Step for equations (leave default as 100)

# Create zero arrays for coordinates
xt = np.zeros(NW)
yt = np.zeros(NW)
zt = np.zeros(NW)

# Set initial values for [X, Y, Z]
xt[0], yt[0], zt[0] = 0.0, 1.0, 0.0

# Set system parameters
params = {
    'sigma': 10,
    'beta': 8/3,
    'rho': 28
}

# Calculate the next coordinates of system
for i in range(NW-1):
    x_next, y_next, z_next = lorenz(xt[i], yt[i], zt[i], **params)
    xt[i+1] = xt[i] + (x_next / dt)
    yt[i+1] = yt[i] + (y_next / dt)
    zt[i+1] = zt[i] + (z_next / dt)

# #####################################################################
# Plot results
# #####################################################################

# Plot 3D model
fig = plt.figure('3D model of chaotic system')

ax = fig.gca(projection='3d')
ax.plot(xt, yt, zt, 'o-', linewidth=0.1, markersize=0.3)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenz Attractor")

# Plot 2D coordinates in time axis
lin = plt.figure('Coordinates evolution in time')

plt.subplot(3, 1, 1)
plt.plot(xt, linewidth=0.75)
plt.grid()
plt.ylabel('X')

plt.subplot(3, 1, 2)
plt.plot(yt, linewidth=0.75)
plt.grid()
plt.ylabel('Y')

plt.subplot(3, 1, 3)
plt.plot(zt, linewidth=0.75)
plt.grid()
plt.ylabel('Z')

plt.tight_layout()
plt.xlabel('time')

plt.show()

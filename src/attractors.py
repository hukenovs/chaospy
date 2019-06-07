"""
------------------------------------------------------------------------

Title         : attractors.py
Author        : Alexander Kapitanov
E-mail        : sallador@bk.ru
Lang.         : python
Company       :
Release Date  : 2019/05/30

------------------------------------------------------------------------

Description   : This is the main module which collects attractors
                together. You can choose: Lorenz, Rossler, Rikitake,
                Nose-Hoover, Chua, Lottki, Duffing, Wang etc.

    Attention!
    You should set correct initial values of coordinates [Xo, Yo, Zo]
    because of some attractors has an overflow effect.

    ----------
    Lorenz:
    ----------
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

    ----------
    Rikitake:
    ----------
    Rikitake system is ordinary differential equation (ODE) of
    3rd order system.
    Rikitake system attempts to explain the reversal of the Earth’s
    magnetic field.

    Rikitake equations are:
        dx/dt = -mu * x + z * y
        dy/dt = -mu * y + x * (z - a)
        dz/dt = 1 - x * y

    where a, mu - are Rikitake system parameters. Default values are
    a = 5, mu = 2 or a = mu = 1.

    ----------
    Rossler:
    ----------
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

    ----------
    Nose–Hoover:
    ----------
    Nose–Hoover oscillator is ordinary differential equation (ODE) of
    3rd order system.
    Nose–Hoover system has only five terms and two quadratic
    nonlinearities.

    Nose–Hoover equations are:
        dx/dt = y
        dy/dt = y * z - x
        dz/dt = 1 - y * y

    Nose–Hoover system doesn't have any system parameters.

    ----------
    Wang attractor:
    ----------
    Wang system (improved Lorenz model) as classic chaotic attractor

    Wang equations are:
        dx/dt = x - y*z
        dy/dt = x - y + x*z
        dz/dt = -3*z + x*y

    ----------
    Duffing map:
    ----------
    It is a discrete-time dynamical system (2nd order)
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

    ----------
    Chua circuit:
    ----------
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

    ----------
    Lotka–Volterra:
    ----------
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
    For example, [x, y, z] = [0.6; 0.2; 0.01].

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
from scipy.stats import kurtosis, skew, gaussian_kde
from scipy.fftpack import fft, fftshift
from scipy.signal import correlate

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  # noqa # pylint: disable=unused-import

from src.chua import chua
from src.wang import wang
from src.lorenz import lorenz
from src.rossler import rossler
from src.duffing import duffing
from src.rikitake import rikitake
from src.nose_hoover import nose_hoover
from src.lotka_volterra import lotka_volterra

# #####################################################################
# Input parameters
# #####################################################################

CHTYPE = 'Lorenz'       # Lorenz, Rossler, Rikitake, Nose-Hoover, etc.
NW = 5000               # Number of ODE's dots
dt = 100                # Step for equations

NFFT = 2**12            # Number of FFT dots

# Create zero arrays for coordinates
xt = np.zeros(NW)
yt = np.zeros(NW)
zt = np.zeros(NW)

# Set initial values for [X, Y, Z]
xt[0], yt[0], zt[0] = 1.0, 0.5, 1.0

# Set system parameters: Lorenz, Rossler, Rikitake

CHUA_ARGS = {'alpha': 0.1, 'beta': 28, 'mu0': -1.143, 'mu1': -0.714}
LORENZ_ARGS = {'sigma': 10, 'beta': 8/3, 'rho': 28}
ROSSLER_ARGS = {'a': 0.2, 'b': 0.2, 'c': 5.7}
DUFFING_ARGS = {'a': 0.1, 'b': 11}
RIKITAKE_ARGS = {'a': 1, 'mu': 1}

# #####################################################################
# Calculate attractor
# #####################################################################

print('Start analyzing the next chaotic system: [%s]\n' % CHTYPE)
for i in range(NW-1):
    ch_type = CHTYPE.casefold()
    if ch_type == 'wang':
        x_next, y_next, z_next = wang(xt[i], yt[i], zt[i])
    elif ch_type == 'nose-hoover':
        x_next, y_next, z_next = nose_hoover(xt[i], yt[i], zt[i])
    elif ch_type == 'lotka':
        x_next, y_next, z_next = lotka_volterra(xt[i], yt[i], zt[i])
    elif ch_type == 'chua':
        x_next, y_next, z_next = chua(xt[i], yt[i], zt[i], **CHUA_ARGS)
    elif ch_type == 'lorenz':
        x_next, y_next, z_next = lorenz(xt[i], yt[i], zt[i], **LORENZ_ARGS)
    elif ch_type == 'rossler':
        x_next, y_next, z_next = rossler(xt[i], yt[i], zt[i], **ROSSLER_ARGS)
    elif ch_type == 'duffing':
        x_next, y_next, z_next = duffing(xt[i], yt[i], zt[i], **DUFFING_ARGS)
    elif ch_type == 'rikitake':
        x_next, y_next, z_next = rikitake(xt[i], yt[i], zt[i], **RIKITAKE_ARGS)
    else:
        raise Exception('Error: you should set the correct chaotic system')

    xt[i+1] = xt[i] + (x_next / dt)
    yt[i+1] = yt[i] + (y_next / dt)
    zt[i+1] = zt[i] + (z_next / dt)

# #####################################################################
# Calculate standardized moments
# #####################################################################

D3 = ['X', 'Y', 'Z']
ch_3d = np.stack((xt, yt, zt))

Nn, Mm = ch_3d.shape[0], ch_3d.shape[1]
print('Calculate mean, variance, skewness, kurtosis and median for each '
      'coordinate of chaotic system:')

M15 = np.zeros([Nn, Mm])
for i in range(Nn):
    M15[i, 0] = np.mean(ch_3d[i, :])      # Mean
    M15[i, 1] = np.var(ch_3d[i, :])       # Variance
    M15[i, 2] = skew(ch_3d[i, :])         # Skewness
    M15[i, 3] = kurtosis(ch_3d[i, :])     # Kurtosis
    M15[i, 4] = np.median(ch_3d[i, :])    # Median

    print('%s axis: ' % D3[i], end='')
    print('M[t]:  {:+.4f},  '.format(M15[i, 0]), end='')
    print('D[t]:  {:+.4f},  '.format(M15[i, 1]), end='')
    print('A[t]:  {:+.4f},  '.format(M15[i, 2]), end='')
    print('E[t]:  {:+.4f},  '.format(M15[i, 3]), end='')
    print('Md[t]: {:+.4f}.  '.format(M15[i, 4]))

# Find Probability density function
N = 1000
p_axi = np.zeros([Nn, N])
d_kde = np.zeros([Nn, N])
for i in range(Nn):
    p_axi[i] = np.linspace(ch_3d[i, :].min(), ch_3d[i, :].max(), N)
    d_kde[i] = gaussian_kde(ch_3d[i, :]).evaluate(p_axi[i, :])
    d_kde[i] /= d_kde[i].max()

# #####################################################################
# Calculate Autocorrelation (Cross-correlation) and FFT
# #####################################################################

# TODO implement FFT and autocorrelation
d_acf = np.zeros([Nn, Mm])
d_fft = np.zeros([Nn, NFFT], dtype=np.complex)
for i in range(Nn):
    d_acf[i] = np.correlate(ch_3d[i, :], ch_3d[i, :], 'same')
    d_acf[i] /= d_acf[i].max()
    d_fft[i] = fft(ch_3d[i, 1:NFFT], NFFT)

d_fft = np.abs(fftshift(d_fft, axes=1))
d_fft /= np.max(d_fft)
d_fft = 20*np.log10(d_fft)

# Plot 2D coordinates in time axis
fig5 = plt.figure('Coordinates evolution in time')
for i in range(Nn):
    plt.subplot(2, 3, i+1)
    plt.plot(d_acf[i], linewidth=0.75)
    plt.grid()
    plt.subplot(2, 3, i+1+3)
    plt.plot(d_fft[i], linewidth=0.75)
    plt.grid()
plt.tight_layout()
plt.show()

# #####################################################################
# Plot results
# #####################################################################

if 0:
    SMALL_SIZE = 8
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 16

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=MEDIUM_SIZE)    # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize

    minmax_x = [np.min(xt), np.max(xt)]
    minmax_y = [np.min(yt), np.max(yt)]
    minmax_z = [np.min(zt), np.max(zt)]

    # Plot 3D model
    fig1 = plt.figure('3D model of chaotic system')

    ax = fig1.gca(projection='3d')
    ax.plot(xt, yt, zt, 'o-', linewidth=0.1, markersize=0.3)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xlim(minmax_x)
    ax.set_ylim(minmax_y)
    ax.set_zlim(minmax_z)
    ax.set_title("3D Chaotic Attractor")
    plt.tight_layout()

    # Plot 2D coordinates of 3D model
    fig2 = plt.figure('2D Coordinates')
    plt.subplot(2, 2, 1)
    plt.plot(yt, xt, linewidth=0.75)
    plt.grid()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(minmax_y)
    plt.ylim(minmax_x)

    plt.subplot(2, 2, 2)
    plt.plot(yt, zt, linewidth=0.75)
    plt.grid()
    plt.xlabel('Z')
    plt.ylabel('Y')
    plt.xlim(minmax_y)
    plt.ylim(minmax_z)

    plt.subplot(2, 2, 3)
    plt.plot(zt, xt, linewidth=0.75)
    plt.grid()
    plt.xlabel('X')
    plt.ylabel('Z')
    plt.xlim(minmax_z)
    plt.ylim(minmax_x)

    ax = fig2.add_subplot(2, 2, 4, projection='3d')
    ax.plot(xt, yt, zt, linewidth=0.7)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.tight_layout()

    # Plot 2D coordinates in time axis
    fig3 = plt.figure('Coordinates evolution in time')
    plt.subplot(2, 2, 1)
    plt.plot(xt, linewidth=0.75)
    plt.grid()
    plt.ylabel('X')
    plt.xlim([0, NW-1])
    plt.ylim(minmax_x)

    plt.subplot(2, 2, 2)
    plt.plot(yt, linewidth=0.75)
    plt.grid()
    plt.ylabel('Y')

    plt.xlim([0, NW-1])
    plt.ylim(minmax_y)

    plt.subplot(2, 2, 3)
    plt.plot(zt, linewidth=0.75)
    plt.grid()
    plt.ylabel('Z')
    plt.xlim([0, NW-1])
    plt.ylim(minmax_z)
    plt.tight_layout()

    # Plot Probability density function
    fig4 = plt.figure('Probability density function')
    for i in range(Nn):
        plt.plot(d_kde[i], '.')
    plt.xlim([0, N-1])
    plt.grid()
    plt.tight_layout()

    # Plot 2D coordinates in time axis
    fig5 = plt.figure('Coordinates evolution in time')
    plt.subplot(2, 2, 1)
    plt.plot(xt, linewidth=0.75)
    plt.grid()
    plt.ylabel('X')
    plt.xlim([0, NW-1])
    plt.ylim(minmax_x)

    plt.subplot(2, 2, 2)
    plt.plot(yt, linewidth=0.75)
    plt.grid()
    plt.ylabel('Y')

    plt.xlim([0, NW-1])
    plt.ylim(minmax_y)

    plt.subplot(2, 2, 3)
    plt.plot(zt, linewidth=0.75)
    plt.grid()
    plt.ylabel('Z')
    plt.xlim([0, NW-1])
    plt.ylim(minmax_z)
    plt.tight_layout()
    plt.show()

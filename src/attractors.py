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

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d  # noqa # pylint: disable=unused-import
from scipy.fftpack import fft, fftshift
from scipy.stats import gaussian_kde, kurtosis, skew
from src.chua import chua
from src.duffing import duffing
from src.lorenz import lorenz
from src.lotka_volterra import lotka_volterra
from src.nose_hoover import nose_hoover
from src.rikitake import rikitake
from src.rossler import rossler
from src.wang import wang

# #####################################################################
# Functions
# #####################################################################


def sel_chaos(chtype=None, xt=0, yt=0, zt=0, **kwargs):
    """
    Select chaotic system function by name

    Parameters
    ----------
    chtype : str
        Select function
    xt, yt, zt : float
        Input coordinates Z, Y, Z respectively
    kwargs : float
        Chaotic system parameters

    """
    ch_case = chtype.casefold()
    if ch_case == "wang":
        return wang(xt, yt, zt)
    elif ch_case == "nose-hoover":
        return nose_hoover(xt, yt, zt)
    elif ch_case == "lotka":
        return lotka_volterra(xt, yt, zt)
    elif ch_case == "chua":
        return chua(xt, yt, zt, **kwargs)
    elif ch_case == "lorenz":
        return lorenz(xt, yt, zt, **kwargs)
    elif ch_case == "rossler":
        return rossler(xt, yt, zt, **kwargs)
    elif ch_case == "duffing":
        return duffing(xt, yt, zt, **kwargs)
    elif ch_case == "rikitake":
        return rikitake(xt, yt, zt, **kwargs)
    else:
        raise Exception("Error: you should set the correct chaotic system")


def sel_args(chtype=None, args=None):
    """
    Select arguments for chaotic system

    Parameters
    ----------
    chtype : str
        Select function
    args : dict
        Chaotic system arguments (as a dict)
    """
    ch_case = chtype.casefold()
    if ch_case in ("lorenz", "rossler", "duffing", "chua", "rikitake"):
        return args[ch_case]
    return {}


# #####################################################################
# Input parameters
# #####################################################################

CHTYPE = "Wang"  # Chaotic system name
CHARGS = {
    "rikitake": {"a": 1, "mu": 1},
    "duffing": {"a": 0.1, "b": 11},
    "rossler": {"a": 0.2, "b": 0.2, "c": 5.7},
    "lorenz": {"sigma": 10, "beta": 8 / 3, "rho": 28},
    "chua": {"alpha": 0.1, "beta": 28, "mu0": -1.143, "mu1": -0.714},
}  # Set arguments

NW = 5000  # Number of ODE's dots
DT = 100  # Step for equations
NFFT = 2 ** 12  # Number of FFT dots


# #####################################################################
# Calculate attractor
# #####################################################################
def calc_chaos():
    print("Start analyzing the next chaotic system: [%s]\n" % CHTYPE)

    # Create zero arrays for coordinates
    xt, yt, zt = np.zeros(NW), np.zeros(NW), np.zeros(NW)
    # Set initial values for [X, Y, Z]
    xt[0], yt[0], zt[0] = 1.0, 0.5, 1.0

    for ii in range(NW - 1):
        x_nt, y_nt, z_nt = sel_chaos(chtype=CHTYPE, xt=xt[ii], yt=yt[ii], zt=zt[ii], **sel_args(CHTYPE, CHARGS),)
        xt[ii + 1] = xt[ii] + (x_nt / DT)
        yt[ii + 1] = yt[ii] + (y_nt / DT)
        zt[ii + 1] = zt[ii] + (z_nt / DT)

    # #####################################################################
    # Calculate standardized moments
    # #####################################################################

    ds_3d = ("X", "Y", "Z")
    ch_3d = np.stack((xt, yt, zt))

    nn, mm = ch_3d.shape[0], ch_3d.shape[1]
    print("Calculate mean, variance, skewness, kurtosis and median for each " "coordinate of chaotic system:")

    m15 = np.zeros([nn, mm])
    for ii in range(nn):
        m15[ii, 0] = np.mean(ch_3d[ii, :])  # Mean
        m15[ii, 1] = np.var(ch_3d[ii, :])  # Variance
        m15[ii, 2] = skew(ch_3d[ii, :])  # Skewness
        m15[ii, 3] = kurtosis(ch_3d[ii, :])  # Kurtosis
        m15[ii, 4] = np.median(ch_3d[ii, :])  # Median

        print("%s axis: " % ds_3d[ii], end="")
        print("M[t]:  {:+.4f},  ".format(m15[ii, 0]), end="")
        print("D[t]:  {:+.4f},  ".format(m15[ii, 1]), end="")
        print("A[t]:  {:+.4f},  ".format(m15[ii, 2]), end="")
        print("E[t]:  {:+.4f},  ".format(m15[ii, 3]), end="")
        print("Md[t]: {:+.4f}.  ".format(m15[ii, 4]))

    # Find Probability density function
    n_pdf = 3000
    p_axi = np.zeros([nn, n_pdf])
    d_kde = np.zeros([nn, n_pdf])
    for ii in range(nn):
        p_axi[ii] = np.linspace(ch_3d[ii, :].min(), ch_3d[ii, :].max(), n_pdf)
        d_kde[ii] = gaussian_kde(ch_3d[ii, :]).evaluate(p_axi[ii, :])
        d_kde[ii] /= d_kde[ii].max()

    # #####################################################################
    # Calculate Autocorrelation (Cross-correlation) and FFT
    # #####################################################################

    # TODO implement FFT and autocorrelation
    d_acf = np.zeros([nn, mm])
    d_fft = np.zeros([nn, NFFT], dtype=np.complex)
    for ii in range(nn):
        d_acf[ii] = np.correlate(ch_3d[ii, :], ch_3d[ii, :], "same")
        d_acf[ii] /= d_acf[ii].max()
        d_fft[ii] = fft(ch_3d[ii, 1:NFFT], NFFT)

    d_fft = np.abs(fftshift(d_fft, axes=1))
    d_fft /= np.max(d_fft)
    d_fft = 20 * np.log10(d_fft)

    plt.rc("font", size=8)  # controls default text sizes
    plt.rc("axes", titlesize=10)  # fontsize of the axes title
    plt.rc("axes", labelsize=10)  # fontsize of the x and y labels
    plt.rc("legend", fontsize=8)  # legend fontsize

    lim_xyz = [(np.min(ch_3d[ii]), np.max(ch_3d[ii])) for ii in range(3)]

    # Plot 3D model
    # fig1 = plt.figure('3D model of chaotic system')
    # ax = fig1.gca(projection='3d')
    # ax.plot(xt, yt, zt, 'o-', linewidth=0.1, markersize=0.3)
    # ax.set_xlabel("X")
    # ax.set_ylabel("Y")
    # ax.set_zlabel("Z")
    # ax.set_xlim(lim_xyz[0])
    # ax.set_ylim(lim_xyz[1])
    # ax.set_zlim(lim_xyz[2])
    # ax.set_title("3D Chaotic Attractor")
    # plt.tight_layout()

    # Plot 2D coordinates of 3D model
    fig2 = plt.figure("3D Coordinates")
    plt.subplot(2, 2, 1)
    plt.plot(yt, xt, linewidth=0.75)
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xlim(lim_xyz[1])
    plt.ylim(lim_xyz[0])

    plt.subplot(2, 2, 2)
    plt.plot(yt, zt, linewidth=0.75)
    plt.grid()
    plt.xlabel("Z")
    plt.ylabel("Y")
    plt.xlim(lim_xyz[1])
    plt.ylim(lim_xyz[2])

    plt.subplot(2, 2, 3)
    plt.plot(zt, xt, linewidth=0.75)
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Z")
    plt.xlim(lim_xyz[2])
    plt.ylim(lim_xyz[0])

    ax = fig2.add_subplot(2, 2, 4, projection="3d")
    ax.plot(xt, yt, zt, linewidth=0.7)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.tight_layout()

    # Plot 2D data in timex
    plt.figure("Coordinates evolution in time")
    for ii in range(nn):
        plt.subplot(2, 2, ii + 1)
        plt.plot(ch_3d[ii], linewidth=0.75)
        plt.grid()
        plt.ylabel(ds_3d[ii])
        plt.xlim([0, NW - 1])
        plt.ylim(lim_xyz[ii])
    plt.tight_layout()

    # Plot Probability density function
    plt.figure("Probability density function")
    for ii in range(nn):
        plt.plot(d_kde[ii], ".")
        plt.xlim([0, n_pdf - 1])
        plt.grid()
    plt.tight_layout()

    # Plot Autocorrelation and Spectrum
    plt.figure("Autocorrelation and Spectrum")
    for ii in range(nn):
        plt.subplot(2, 3, ii + 1)
        plt.plot(d_acf[ii], linewidth=0.75)
        plt.grid()
        plt.subplot(2, 3, ii + 1 + 3)
        plt.plot(d_fft[ii], linewidth=0.75)
        plt.grid()
    plt.tight_layout()

    plt.show()


# Execute main function: Chaotic system
calc_chaos()

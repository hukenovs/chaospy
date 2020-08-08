r"""Argument parser for testing chaotic attractor.

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
# Release Date  : 2020/07/30
# License       : GNU GENERAL PUBLIC LICENSE

import argparse
from typing import Optional, Sequence

SET_OF_ATTRACTORS = {"lorenz", "rossler", "rikitake", "duffing", "wang", "nose-hoover", "chua", "lotka-volterra"}
DEFAULT_PARAMETERS = {
    "lorenz": {"sigma": 10, "beta": 8 / 3, "rho": 28},
    "rikitake": {"a": 1, "mu": 1},
    "duffing": {"a": 0.1, "b": 11},
    "rossler": {"a": 0.2, "b": 0.2, "c": 5.7},
    "chua": {"alpha": 0.1, "beta": 28, "mu0": -1.143, "mu1": -0.714},
}


def parse_arguments(
    input_args: Optional[Sequence[str]] = None, show_help: bool = False, show_args: bool = False
) -> argparse.Namespace:
    """This method is an useful command line helper. You can use it with command line arguments.

    Parameters
    ----------
    input_args: tuple

    show_help : bool
        Show help of argument parser.

    show_args : bool
        Display arguments and their values as {key : item}

    Returns
    -------
    arguments : Namespace
        Parsed arguments from command line. Note: some arguments are positional.

    Examples
    --------
    >>> from src.utils.parser import parse_arguments
    >>> command_line_str = "lorenz",
    >>> args = parse_arguments(command_line_str, show_args=True)
    attractor      = lorenz
    points         = 1024
    step           = 100
    show_plots     = False
    save_plots     = False
    sigma          = 10
    beta           = 2.6666666666666665
    rho            = 28
    >>> command_line_str = "rossler", "--show_plots"
    >>> args = parse_arguments(command_line_str, show_args=True)
    attractor      = rossler
    points         = 1024
    step           = 100
    show_plots     = True
    save_plots     = False
    a              = 0.2
    b              = 0.2
    c              = 5.7
    >>> print(args)
    Namespace(a=0.2, attractor='rossler', b=0.2, c=5.7, points=1024, save_plots=False, show_plots=True, step=100)
    """
    parser = argparse.ArgumentParser(
        description="Specify command line arguments for dynamic system."
        "Calculate some math parameters and plot some graphs of a given chaotic system."
    )
    parser.add_argument(
        "attractor",
        type=str.lower,
        choices={"lorenz", "chua", "rossler", "rikitake", "wang", "nose-hoover", "duffing", "lotka-volterra"},
        help=f"Select a chaotic model: Lorenz, Chua, Rossler, Duffing, etc. Default: Lorenz.",
    )

    parser.add_argument(
        "-p",
        "--points",
        type=int,
        default=1024,
        action="store",
        help=f"Number of points for dymanic system. Default: 1024",
    )

    parser.add_argument(
        "-s",
        "--step",
        type=int,
        default=100,
        action="store",
        help=f"Step size for calculating the next coordinates of chaotic system. Default: 100",
    )

    parser.add_argument("--show_plots", action="store_true", help="Show plots of a model. Default: False.")
    parser.add_argument("--save_plots", action="store_true", help="Save plots to PNG files. Default: False.")

    # Getting default parameters for chosen attractor:
    # TODO: Replace this to sys args !
    model_name = parser.parse_args(input_args).attractor
    # parser.set_defaults(attractor=model_name)
    model_args = DEFAULT_PARAMETERS.get(model_name)
    if model_args is not None:
        group_args = parser.add_argument_group("Parameters", f"Dynamyc system parameters for {model_name} model.")
        for key in model_args:
            group_args.add_argument(
                f"--{key}",
                type=float,
                default=model_args[key],
                action="store",
                help=f"{model_name} system parameter. Default: {model_args[key]}",
            )

    if show_help:
        parser.print_help()

    ret_args = parser.parse_args(input_args)
    if show_args:
        for arg in vars(ret_args):
            print(f"{arg :<14} = {getattr(ret_args, arg)}")
    return ret_args


if __name__ == "__main__":
    # parse_args = parse_arguments(input_args=("Rossler --show_plots".split()), show_help=True, show_args=True)
    # print(parse_args)
    import doctest

    doctest.testmod(verbose=True)

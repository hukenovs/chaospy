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
from typing import Optional, Sequence, Tuple, Union

from src.attractors.chua import Chua
from src.attractors.duffing import Duffing
from src.attractors.lorenz import Lorenz
from src.attractors.lotka_volterra import LotkaVolterra
from src.attractors.nose_hoover import NoseHoover
from src.attractors.rikitake import Rikitake
from src.attractors.rossler import Rossler
from src.attractors.wang import Wang

AttractorType = Union[Chua, Duffing, Rossler, Lorenz, Wang, NoseHoover, Rikitake, Wang, LotkaVolterra]

SET_OF_ATTRACTORS = ("lorenz", "rossler", "rikitake", "duffing", "wang", "nose-hoover", "chua", "lotka-volterra")
DEFAULT_PARAMETERS = {
    "lorenz": {"sigma": 10, "beta": 8 / 3, "rho": 28},
    "rikitake": {"a": 1, "mu": 1},
    "duffing": {"a": 0.1, "b": 11},
    "rossler": {"a": 0.2, "b": 0.2, "c": 5.7},
    "chua": {"alpha": 0.1, "beta": 28, "mu0": -1.143, "mu1": -0.714},
}


class Settings:
    r"""Attributes collection for chaotic system.

    Attributes
    ----------

    attractor : Optional[AttractorType]
        Chaotic model.

    points : step
        Number of points for 3D system.

    step : float
        Step for diff. equations.

    show_plots : bool
        Show plots after calculations: True / False.

    save_plots : bool
        Save plots after calculations: True / False.

    """
    __model_map = {
        "lorenz": Lorenz,
        "rossler": Rossler,
        "rikitake": Rikitake,
        "chua": Chua,
        "duffing": Duffing,
        "wang": Wang,
        "nose-hoover": NoseHoover,
        "lotka-volterra": LotkaVolterra,
    }

    def __init__(self, show_log: bool = False):
        self.show_log = show_log
        # Settings
        self.attractor: str = "lorenz"
        self.points: int = 1024
        self.init_point: Tuple[float, float, float] = (0.1, 0.1, 0.1)
        self.step: float = 10
        self.show_plots: bool = False
        self.save_plots: bool = False
        self.kwargs: dict = {}
        # Model
        self._model: Optional[AttractorType] = None

    @property
    def model(self):
        if self._model is None:
            self._model = self.__model_map.get(self.attractor)(
                num_points=self.points,
                init_point=self.init_point,
                step=self.step,
                show_log=self.show_log,
                **self.kwargs,
            )
        return self._model

    def update_params(self, input_args: Optional[Sequence[str]] = None, show_args: bool = False):
        r"""Update class attributes from command line parser.
        Kwargs is a dictionary and it can have some parameters for chaotic model.

        """
        args_dict = parse_arguments(input_args=input_args, show_args=show_args)
        for item in args_dict:
            if hasattr(self, item):
                setattr(self, item, args_dict[item])
            else:
                self.kwargs[item] = args_dict[item]


def parse_arguments(
    input_args: Optional[Sequence[str]] = None, show_help: bool = False, show_args: bool = False
) -> dict:
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
    arguments : dict
        Parsed arguments from command line. Note: some arguments are positional.

    Examples
    --------
    >>> from src.utils.parser import parse_arguments
    >>> command_line_str = "lorenz",
    >>> test_args = parse_arguments(command_line_str, show_args=True)
    points         = 1024
    step           = 100
    show_plots     = False
    save_plots     = False
    attractor      = lorenz
    sigma          = 10
    beta           = 2.6666666666666665
    rho            = 28
    >>> command_line_str = "--show_plots rossler --a 2 --b 4".split()
    >>> test_args = parse_arguments(command_line_str, show_args=True)
    points         = 1024
    step           = 100
    show_plots     = True
    save_plots     = False
    attractor      = rossler
    a              = 2.0
    b              = 4.0
    c              = 5.7
    >>> command_line_str = "--step 1 --points 10 wang".split()
    >>> test_args = parse_arguments(command_line_str)
    >>> print(test_args)
    Namespace(attractor='wang', points=10, save_plots=False, show_plots=False, step=1)
    """
    parser = argparse.ArgumentParser(
        description="Specify command line arguments for dynamic system."
        "Calculate some math parameters and plot some graphs of a given chaotic system."
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

    subparsers = parser.add_subparsers(
        title="Chaotic models", description="You can select one of the chaotic models", dest="attractor"
    )

    sub_list = []
    for attractor in SET_OF_ATTRACTORS:
        chosen_items = DEFAULT_PARAMETERS.get(attractor)
        chosen_model = f"{attractor}".capitalize()
        subparser = subparsers.add_parser(f"{attractor}", help=f"{chosen_model} chaotic model")
        if chosen_items is not None:
            group = subparser.add_argument_group(title=f"{chosen_model} model arguments")
            for key in chosen_items:
                group.add_argument(
                    f"--{key}",
                    type=float,
                    default=chosen_items[key],
                    action="store",
                    help=f"{chosen_model} system parameter. Default: {chosen_items[key]}",
                )
        sub_list.append(subparser)

    if show_help:
        parser.print_help()
        for item in sub_list:
            item.print_help()

    args = vars(parser.parse_args(input_args))
    if args["attractor"] is None:
        raise AssertionError(f"[FAIL]: Please select a chaotic model from the next set: {SET_OF_ATTRACTORS}")
    if show_args:
        print(f"[INFO]: Cmmaind line arguments: ")
        for arg in args:
            print(f"{arg :<14} = {args[arg]}")
        print("")
    return args


if __name__ == "__main__":
    # import doctest
    #
    # doctest.testmod(verbose=True)

    args_main = parse_arguments(show_args=True)
    print(args_main)

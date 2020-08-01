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


def parse_arguments(show_help: bool = False, show_args: bool = False):
    parser = argparse.ArgumentParser(
        description="Calculate some math parameters and plot some graphs of a given chaotic system."
    )
    parser.add_argument(
        "attractor",
        type=str.lower,
        choices={"lorenz", "chua", "rossler", "rikitake", "wang", "nose-hoover", "duffing"},
        help=f"Select a chaotic model: Lorenz, Chua, Rossler, etc. Default: Lorenz.",
    )

    group_plot = parser.add_mutually_exclusive_group()
    group_plot.add_argument("--show_plots", action="store_true", help="Show plots of a model. Default: False.")
    group_plot.add_argument("--hide_plots", action="store_false", help="Don't show plots. Default: True.")

    if show_help:
        parser.print_help()

    ret_args = parser.parse_args()
    if show_args:
        for arg in vars(ret_args):
            print(f"{arg :<14} = {getattr(ret_args, arg)}")
    return ret_args


if __name__ == "__main__":
    args = parse_arguments(show_help=False, show_args=True)

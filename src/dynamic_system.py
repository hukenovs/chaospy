"""Dynamic system class.

Description:
    Combine attractor, calculator and drawer.

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
# Release Date  : 2020/07/25
# License       : GNU GENERAL PUBLIC LICENSE

from src.attractors.attractor import BaseAttractor
from src.utils.calculator import Calculator
from src.utils.drawer import PlotDrawer


class DynamicSystem:
    """Main class for computing chaotic system.

    Parameters
    ----------
    # TODO: add parameters

    Attributes
    ----------
    drawer: PlotDrawer()
    calculator: Calculator()

    Examples
    --------
    # TODO: Add examples

    See Also:
    -----

    Dynamic systems:
    https://en.wikipedia.org/wiki/Dynamical_system
    https://en.wikipedia.org/wiki/Dynamical_systems_theory

    Differential equations:
    https://en.wikipedia.org/wiki/Differential_equation

    """

    def __init__(self, save_plots: bool = False):
        self.drawer = PlotDrawer(save_plots)
        self.calculator = Calculator()
        self.attractor = None

    def set_attractor(self, chaotic):
        self.attractor = chaotic

    # def __call__(self, save_plots: bool = False):
    #     if self.show_log:
    #         print("\n[INFO]: Calculate mean, variance, skewness, kurtosis and median for chaotic system:")
    #     _moments = self.check_moments()
    #     for _key in _moments:
    #         print(f"{_key:<10}: {_moments[_key]}")
    #
    #     if self.show_log:
    #         print("\n[INFO]: Calculate moments:")
    #     _global_moments = self.check_moments(is_global=True)
    #     for _key in _global_moments:
    #         print(f"{_key:<10}: {_global_moments[_key]}")
    #
    #     self.drawer.show_3d_plots()


if __name__ == "__main__":
    model = DynamicSystem()
    attractor = BaseAttractor(num_points=100, init_point=(0, 1, 2), step=10)
    model.set_attractor(attractor)

    moments = model.calculator.check_moments(model.attractor.coordinates)
    for _key in moments:
        print(f"{_key:<10}: {list(moments[_key])}")

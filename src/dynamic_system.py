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

from typing import Optional

import pandas as pd
from src.utils.calculator import Calculator
from src.utils.drawer import PlotDrawer
from src.utils.parser import AttractorType, Settings


class DynamicSystem:
    """Main class for computing chaotic system.

    Parameters
    ----------
    # TODO: add parameters

    Attributes
    ----------
    model: ChaoticAttractor()
    drawer: PlotDrawer()
    calculator: Calculator()
    settings: Settings()

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

    def __init__(self, input_args: Optional[tuple] = None, show_log: bool = False):
        # Main modules
        self.settings: Optional[Settings] = None
        self.model: Optional[AttractorType] = None
        self.drawer: Optional[PlotDrawer] = None
        self.calculator: Optional[Calculator] = None
        # Initialize attributes
        self.initialize(input_args, show_log)

    def initialize(self, input_args: Optional[tuple] = None, show_logs: bool = False):
        # Update parameters
        self.settings = Settings(show_logs=show_logs)
        self.settings.update_params(input_args)

        # Update chaotic model
        self.model = self.settings.model

        # Update drawer for plots
        self.drawer = PlotDrawer(self.settings.save_plots, self.settings.show_plots, self.settings.add_2d_gif)
        self.drawer.model_name = self.settings.attractor.capitalize()

        # Update main calculator
        self.calculator = Calculator()

    def collect_statistics(self):
        math_dict = {}
        _min_max = self.calculator.check_min_max()
        _moments = self.calculator.check_moments()
        math_dict.update({"Min": _min_max[0]})
        math_dict.update({"Max": _min_max[1]})
        math_dict.update(_moments)
        math_df = pd.DataFrame.from_dict(math_dict, columns=["X", "Y", "Z"], orient="index")
        return math_df

    def run(self):
        # Get vector of coordinates
        _points = self.model.get_coordinates()
        self.calculator.coordinates = _points

        # Calculate
        stats = self.collect_statistics()
        if self.settings.show_logs:
            print(f"[INFO]: Show statistics:\n{stats}\n")

        self.calculator.check_probability()
        self.calculator.calculate_fft()

        # Draw results
        if self.settings.show_plots or self.settings.save_plots:
            self.drawer.coordinates = _points

            # self.drawer.show_time_plots()
            # self.drawer.show_3d_plots()
            self.drawer.make_3d_plot_gif(50)
            # self.drawer.show_all_plots()


if __name__ == "__main__":
    command_line = (
        "--init_point",
        "1 -1 2",
        "--points",
        "2000",
        "--step",
        "50",
        "--save_plots",
        # "--show_plots",
        "--add_2d_gif",
        "rossler",
    )

    dynamic_system = DynamicSystem(input_args=command_line, show_log=True)
    dynamic_system.run()

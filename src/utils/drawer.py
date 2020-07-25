"""Plot drawer

Description   :
    Useful component for plotting results

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

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d  # noqa # pylint: disable=unused-import


class PlotDrawer:
    """Main class for drawing plots.

    See Also:
    -----

    """

    def __init__(self, model_name: str, coordinates: np.array, num_points: int, save_plots: bool = False):
        self.model_name = model_name
        self.coordinates = coordinates
        self.num_points = num_points
        self.save_plots = save_plots

    def show_time_plots(self):
        """Plot 3D coordinates as time series."""
        plt.figure("Coordinates evolution in time", figsize=(8, 6), dpi=100)
        for ii, axis in enumerate(["X", "Y", "Z"]):
            plt.subplot(3, 1, ii + 1)
            plt.plot(self.coordinates[:, ii], linewidth=0.75)
            plt.grid(True)
            if axis == "Z":
                plt.xlabel("Time")
            plt.ylabel(axis)
            plt.xlim([0, self.num_points - 1])
        plt.tight_layout()
        if self.save_plots:
            plt.savefig(f"{self.model_name}_coordinates_in_time.png")
        plt.show()

    def show_3d_plots(self):
        """Plot 3D coordinates as time series."""
        plot_axis = ((1, 0), (1, 2), (2, 0))
        plot_labels = {0: "X", 1: "Y", 2: "Z"}

        fig = plt.figure(f"3D model of {self.model_name} system", figsize=(8, 6), dpi=100)
        for ii, (xx, yy) in enumerate(plot_axis):
            plt.subplot(2, 2, 1 + ii)
            plt.plot(self.coordinates[:, xx], self.coordinates[:, yy], linewidth=0.75)
            plt.grid()
            plt.xlabel(plot_labels[xx])
            plt.ylabel(plot_labels[yy])
            # plt.xlim()
            # plt.ylim()

        ax = fig.add_subplot(2, 2, 4, projection="3d")
        ax.plot(self.coordinates[:, 0], self.coordinates[:, 1], self.coordinates[:, 2], linewidth=0.7)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.tight_layout()

        if self.save_plots:
            plt.savefig(f"{self.__class__.__name__}_coordinates.png")
        plt.show()


if __name__ == "__main__":
    pass

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
    Matplotlib: Visualization with Python:
    https://matplotlib.org/

    """

    def __init__(self, save_plots: bool = False, show_plots: bool = False):
        self.save_plots = save_plots
        self.show_plots = show_plots
        self._model_name = None
        self._close_test = False

    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, model):
        self._model_name = model

    def show_time_plots(self, coordinates: np.ndarray):
        """Plot 3D coordinates as time series."""
        _ = plt.figure("Coordinates evolution in time", figsize=(8, 6), dpi=100)
        for ii, axis in enumerate(["X", "Y", "Z"]):
            plt.subplot(3, 1, ii + 1)
            plt.plot(coordinates[:, ii], linewidth=0.75)
            plt.grid(True)
            if axis == "Z":
                plt.xlabel("Time (t)")
            plt.ylabel(axis)
            plt.xlim([0, len(coordinates) - 1])
        plt.tight_layout()
        if self.save_plots:
            plt.savefig(f"{self.model_name}_coordinates_in_time.png")
        if self.show_plots:
            plt.show()

    def show_3d_plots(self, coordinates: np.ndarray):
        """Plot 3D coordinates as time series."""
        plot_axis = ((1, 0), (1, 2), (2, 0))
        plot_labels = {0: "X", 1: "Y", 2: "Z"}

        fig = plt.figure(f"3D model of chaotic system", figsize=(8, 6), dpi=100)
        for ii, (xx, yy) in enumerate(plot_axis):
            plt.subplot(2, 2, 1 + ii)
            plt.plot(coordinates[:, xx], coordinates[:, yy], linewidth=0.75)
            plt.grid()
            plt.xlabel(plot_labels[xx])
            plt.ylabel(plot_labels[yy])
            # TODO: 2020/07/26: Set limits!
            # plt.xlim()
            # plt.ylim()

        ax = fig.add_subplot(2, 2, 4, projection="3d")
        ax.plot(coordinates[:, 0], coordinates[:, 1], coordinates[:, 2], linewidth=0.7)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.tight_layout()

        if self.save_plots:
            plt.savefig(f"{self.model_name}_3d_coordinates.png")
        if self.show_plots:
            plt.show()

    def show_all_plots(self):
        """Cannot show all plots while 'show_plots' is True.
        Note: After closing plots you cannot reopen them!
        """
        if not self.show_plots:
            plt.show()

    @staticmethod
    def close_all_plots():
        plt.clf()
        plt.cla()
        plt.close()


if __name__ == "__main__":
    drawer = PlotDrawer(save_plots=False)
    np.random.seed(42)
    points = np.cumsum(np.random.randn(200, 3), axis=1)
    drawer.show_time_plots(coordinates=points)
    drawer.show_3d_plots(coordinates=points)
    drawer.show_all_plots()
    # Trick: press Q on each plot for exit.

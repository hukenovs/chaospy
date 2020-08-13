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

from functools import lru_cache

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3  # noqa # pylint: disable=unused-import
import numpy as np


class PlotDrawer:
    """Main class for drawing plots.

    See Also:
    -----
    Matplotlib: Visualization with Python:
    https://matplotlib.org/

    """

    def __init__(self, save_plots: bool = False, show_plots: bool = False, model_name: str = None):
        self.save_plots = save_plots
        self.show_plots = show_plots
        self._model_name = model_name
        self._coordinates = None
        self._color_map = None

    def __len__(self):
        return len(self.coordinates)

    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value: str):
        self._model_name = value

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value: np.ndarray):
        self._coordinates = value

    @property
    @lru_cache(maxsize=8)
    def min_max_axis(self):
        return np.vstack([np.min(self.coordinates, axis=0), np.max(self.coordinates, axis=0)]).T

    def show_time_plots(self):
        """Plot 3D coordinates as time series."""
        _ = plt.figure("Coordinates evolution in time", figsize=(8, 6), dpi=100)
        for ii, axis in enumerate(["X", "Y", "Z"]):
            plt.subplot(3, 1, ii + 1)
            plt.plot(self.coordinates[:, ii], linewidth=0.75)
            plt.grid(True)
            if axis == "Z":
                plt.xlabel("Time (t)")
            plt.ylabel(axis)
            plt.xlim([0, len(self.coordinates) - 1])
        plt.tight_layout()
        if self.save_plots:
            plt.savefig(f"{self.model_name}_coordinates_in_time.png")
        if self.show_plots:
            plt.show()

    def axis_defaults(self, ax):
        ax.set_title(f"{self.model_name} attractor")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_xlim3d(self.min_max_axis[0])
        ax.set_ylim3d(self.min_max_axis[1])
        ax.set_zlim3d(self.min_max_axis[2])
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        # ax.set_axis_off()
        # ax.xaxis.pane.set_edgecolor('w')
        # ax.yaxis.pane.set_edgecolor('w')
        # ax.zaxis.pane.set_edgecolor('w')
        # ax.grid(False)
        # ax.tight_layout()

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
            # TODO: 2020/07/26: Set limits!
            plt.xlim(self.min_max_axis[xx])
            plt.ylim(self.min_max_axis[yy])

        ax = fig.add_subplot(2, 2, 4, projection="3d")
        ax.plot(self.coordinates[:, 0], self.coordinates[:, 1], self.coordinates[:, 2], linewidth=0.7)
        self.axis_defaults(ax)
        plt.tight_layout()

        if self.save_plots:
            plt.savefig(f"{self.model_name}_3d_coordinates.png")
        if self.show_plots:
            plt.show()

    def make_3d_plot_gif(self, step_size: int = 10):
        """Make git for 3D coordinates as time series."""

        fig = plt.figure(f"3D model of {self.model_name} system", figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111, projection="3d")
        self.axis_defaults(ax)
        (pic,) = plt.plot([], [], ".--", lw=0.75)

        step_dots = len(self.coordinates) // step_size
        self._color_map = plt.cm.get_cmap("hsv", step_dots)

        ani = animation.FuncAnimation(
            fig, self.update_coordinates, step_dots, fargs=(step_size, pic), interval=100, blit=False, repeat=True
        )

        if self.save_plots:
            ani.save(f"{self.model_name}_3d.gif", writer="imagemagick")
        if self.show_plots:
            plt.show()

    def update_coordinates(self, num, step, pic):
        pic.set_data(self.coordinates[0 : 1 + num * step, 0], self.coordinates[0 : 1 + num * step, 1])
        pic.set_3d_properties(self.coordinates[0 : 1 + num * step, 2])
        pic.set_color(self._color_map(num))

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
    np.random.seed(42)
    points = np.cumsum(np.random.randn(50, 3), axis=1)

    drawer = PlotDrawer(show_plots=True)
    drawer.coordinates = points
    drawer.model_name = "Chaotic"

    # print(drawer.min_max_axis)
    drawer.make_3d_plot_gif()
    # drawer.show_time_plots(coordinates=points)
    # drawer.show_3d_plots()
    # drawer.show_all_plots()

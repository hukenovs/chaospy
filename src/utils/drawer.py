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

    _plot_axis = ((0, 1), (2, 1), (0, 2))
    _plot_labels = {0: "X", 1: "Y", 2: "Z"}

    def __init__(
        self, save_plots: bool = False, show_plots: bool = False, add_2d_gif: bool = False, model_name: str = None,
    ):
        self.save_plots = save_plots
        self.show_plots = show_plots
        self.add_2d_gif = add_2d_gif
        self.time_or_dot = False

        self._model_name = model_name
        self._coordinates = None
        # Internal parameters
        self._color_map = None
        self._plot_list = None
        self._min_max_axis = None
        self.coordinates = None

    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value: str):
        self._model_name = value

    @staticmethod
    def __min_max_axis(coordinates: np.ndarray):
        return np.vstack([np.min(coordinates, axis=0), np.max(coordinates, axis=0)]).T

    def plot_kde(self, kde: np.ndarray, pdf: np.ndarray):
        """Plot Probability density function"""
        _ = plt.figure("Probability density function", figsize=(8, 6), dpi=100)
        for ii, axis in enumerate(self._plot_labels.values()):
            plt.subplot(3, 3, ii + 1)
            plt.title("KDE plots", y=1.0) if ii % 2 == 1 else None
            plt.plot(kde[ii], ".")
            plt.xlim([0, pdf - 1])
            plt.grid()
        plt.tight_layout()

    def show_spectrum_and_correlation(self, coordinates: np.ndarray, spectrums: np.ndarray, correlations: np.ndarray):
        """Plot 3D coordinates as time series."""
        _ = plt.figure("Autocorrelation and Spectrum", figsize=(8, 6), dpi=100)

        x_corr = np.linspace(-len(coordinates) // 2, len(coordinates) // 2, len(coordinates))
        x_ffts = np.linspace(-0.5, 0.5, len(spectrums))

        plt.suptitle(f"{self.model_name} attractor", x=0.1)
        for ii, axis in enumerate(self._plot_labels.values()):
            plt.subplot(3, 3, ii + 1)
            plt.title("Time plots", y=1.0) if ii % 2 == 1 else None
            plt.plot(coordinates[:, ii], linewidth=0.75)
            plt.grid(True)
            plt.ylabel(axis)
            plt.xlim([0, len(coordinates) - 1])
            plt.subplot(3, 3, ii + 4)
            plt.title("Spectrum plots", y=1.0) if ii % 2 == 1 else None
            plt.plot(x_ffts, spectrums[:, ii], linewidth=0.75)
            plt.grid(True)
            plt.ylabel(axis)
            plt.xlim([np.min(x_ffts), np.max(x_ffts)])
            plt.subplot(3, 3, ii + 7)
            plt.title("Correlation plots", y=1.0) if ii % 2 == 1 else None
            plt.plot(x_corr, correlations[:, ii], linewidth=0.75)
            plt.grid(True)
            plt.ylabel(axis)
            plt.xlim([np.min(x_corr), np.max(x_corr)])
        plt.tight_layout()

        if self.save_plots:
            plt.savefig(f"{self.model_name}_spectrum_correlations.png")
        if self.show_plots:
            plt.show()

    def show_time_plots(self, coordinates: np.ndarray):
        """Plot 3D coordinates as time series."""
        _ = plt.figure("Coordinates evolution in time", figsize=(8, 6), dpi=100)
        for ii, axis in enumerate(self._plot_labels.values()):
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

    def __axis_defaults_3d(self, plots, coordinates: np.ndarray):
        min_max = self.__min_max_axis(coordinates)
        plots.set_title(f"{self.model_name} model")
        plots.set_xlabel("X")
        plots.set_ylabel("Y")
        plots.set_zlabel("Z")
        plots.set_xlim3d(min_max[0])
        plots.set_ylim3d(min_max[1])
        plots.set_zlim3d(min_max[2])
        plots.xaxis.pane.fill = False
        plots.yaxis.pane.fill = False
        plots.zaxis.pane.fill = False

    def __axis_defaults_2d(self, plots, coordinates: np.ndarray):
        min_max = self.__min_max_axis(coordinates)
        for idx, (xx, yy) in enumerate(self._plot_axis):
            plots[idx].set_xlim(min_max[xx])
            plots[idx].set_ylim(min_max[yy])
            plots[idx].set_xlabel(self._plot_labels[xx])
            plots[idx].set_ylabel(self._plot_labels[yy])
            plots[idx].grid(True)
        # ax.set_axis_off()
        # ax.xaxis.pane.set_edgecolor('w')
        # ax.yaxis.pane.set_edgecolor('w')
        # ax.zaxis.pane.set_edgecolor('w')
        # ax.grid(False)
        # ax.tight_layout()

    def show_3d_plots(self, coordinates: np.ndarray):
        """Plot 3D coordinates as time series."""
        min_max = self.__min_max_axis(coordinates)

        fig = plt.figure(f"3D model of {self.model_name} system", figsize=(8, 6), dpi=100)
        for ii, (xx, yy) in enumerate(self._plot_axis):
            plt.subplot(2, 2, 1 + ii)
            plt.plot(coordinates[:, xx], coordinates[:, yy], linewidth=0.75)
            plt.grid()
            plt.xlabel(self._plot_labels[xx])
            plt.ylabel(self._plot_labels[yy])
            plt.xlim(min_max[xx])
            plt.ylim(min_max[yy])

        ax = fig.add_subplot(2, 2, 4, projection="3d")
        ax.plot(coordinates[:, 0], coordinates[:, 1], coordinates[:, 2], linewidth=0.75)
        self.__axis_defaults_3d(ax, coordinates)
        plt.tight_layout()

        if self.save_plots:
            plt.savefig(f"{self.model_name}_3d_coordinates.png")
        if self.show_plots:
            plt.show()

    def _add_2d_to_plots(self, figure, coordinates: np.ndarray):
        self._plot_list += [figure.add_subplot(2, 2, 1 + ii) for ii in range(3)]
        self.__axis_defaults_2d(self._plot_list[1:], coordinates)
        plt.tight_layout()

    def make_3d_plot_gif(self, coordinates: np.ndarray, step_size: int = 10):
        """Make git for 3D coordinates as time series."""
        nodes = 2 if self.add_2d_gif else 1
        posit = 4 if self.add_2d_gif else 1
        fig = plt.figure(f"3D model of {self.model_name} system", figsize=(8, 6), dpi=100)

        self._plot_list = [fig.add_subplot(nodes, nodes, posit, projection="3d")]
        self.__axis_defaults_3d(self._plot_list[0], coordinates)

        if self.add_2d_gif:
            self._add_2d_to_plots(fig, coordinates)

        # Convert ax to plot
        self._plot_list = [item.plot([], [], ".--", lw=0.75)[0] for item in self._plot_list]

        step_dots = len(coordinates) // step_size
        self._color_map = plt.cm.get_cmap("hsv", step_dots)

        self.coordinates = coordinates
        ani = animation.FuncAnimation(
            fig, self._update_coordinates, step_dots, fargs=(step_size,), interval=100, blit=False, repeat=True
        )

        if self.save_plots:
            ani.save(f"{self.model_name}_3d.gif", writer="imagemagick")
        if self.show_plots:
            plt.show()

    def _update_coordinates(self, num, step):
        """Update plots for making gif"""
        self._plot_list[0].set_data(self.coordinates[0 : 1 + num * step, 0], self.coordinates[0 : 1 + num * step, 1])
        self._plot_list[0].set_3d_properties(self.coordinates[0 : 1 + num * step, 2])
        self._plot_list[0].set_color(self._color_map(num))
        if self.add_2d_gif:
            for ii, (x, y) in enumerate(self._plot_axis):
                self._plot_list[ii + 1].set_data(
                    self.coordinates[0 : 1 + num * step, x], self.coordinates[0 : 1 + num * step, y]
                )
                self._plot_list[ii + 1].set_color(self._color_map(num))

    def show_all_plots(self, coordinates: np.ndarray, spectrums: np.ndarray, correlations: np.ndarray):
        """Cannot show all plots while 'show_plots' is True.
        
        Note: After closing plots you cannot reopen them!
        """
        show_plots, self.show_plots = self.show_plots, False
        self.show_time_plots(coordinates)
        self.show_3d_plots(coordinates)
        self.show_spectrum_and_correlation(coordinates, spectrums, correlations)
        plt.show()
        self.show_plots = show_plots


def random_circle(num_points: int = 100, sigma: float = 0.01, angle: float = 2.) -> np.ndarray:
    r"""Create random circle for 3D plots.

    Parameters
    ----------
    num_points : int
        Number of points to draw

    sigma : int
        Random shift

    angle : int
        Rotate angle

    Returns
    -------

    arr: np.ndarray
        Numpy 3D array with shapes [3, num_points]
    """

    theta = np.linspace(0, angle * np.pi, num_points)
    xyz = np.vstack([np.cos(theta), np.sin(theta), np.sin(np.linspace(0, 2.05 * np.pi, num_points))]).T
    xyz += sigma * np.cumsum(np.random.randn(num_points, 3), axis=1)
    return xyz


if __name__ == "__main__":
    np.random.seed(42)
    circle_points = random_circle(num_points=400, sigma=0.01)

    drawer = PlotDrawer(show_plots=True, add_2d_gif=True)
    drawer.model_name = "Chaotic"

    # print(drawer.min_max_axis)
    drawer.make_3d_plot_gif(step_size=10, coordinates=circle_points)
    # drawer.show_time_plots()
    # drawer.show_3d_plots()
    # drawer.show_all_plots()

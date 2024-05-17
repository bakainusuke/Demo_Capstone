import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class WaveRoseWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Create a vertical layout for the widget
        layout = QVBoxLayout(self)

        # Create matplotlib figure and canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def plot_wave_rose(self, data):
        # Clear previous plot
        self.ax.clear()

        # # Filter out rows with NaN ship types
        # df_filtered = data.dropna(subset=['ship_type'])

        # # Get unique ship types from the filtered dataset
        # ship_types = df_filtered['ship_type'].unique()

        # # Create subplots for each ship type (excluding NaN ship types)
        # for ship_type in ship_types:
           
        #  # Filter data for the current ship type
        #     subset = df_filtered[df_filtered['ship_type'] == ship_type]

        #     # Calculate normalized frequencies (manually normalize data)
        #     frequencies, bins = np.histogram(
        #         subset['course'], bins=36, range=(0, 360), weights=subset['speed'])
        #     frequencies = frequencies / frequencies.sum()  # Normalize frequencies

        #     # Plotting the wind rose (wave rose) graph for the current ship type
        #     ax = self.figure.add_subplot(111, polar=True)
        #     ax.bar(np.radians(bins[:-1]), frequencies,
        #            width=np.radians(10), edgecolor='white')

        #     # Customize the wind rose plot for the current ship type
        #     ax.set_title(f'Wave Rose Plot for Ship Type: {
        #                  ship_type}', fontsize=12)
        #     # Set clockwise direction for theta (degrees)
        #     ax.set_theta_direction(-1)
        #     # Set zero location to North (top of the plot)
        #     ax.set_theta_zero_location('N')
        # Calculate normalized frequencies for all ship data
        frequencies, bins = np.histogram(
            data['course'], bins=36, range=(0, 360), weights=data['speed'])
        # frequencies = frequencies / frequencies.sum()  # Normalize frequencies

        # Plotting the wind rose (wave rose) graph for all ship data
        ax = self.figure.add_subplot(111, polar=True)
        ax.bar(np.radians(bins[:-1]), frequencies,
               width=np.radians(10), edgecolor='white')

        # Customize the wind rose plot
        ax.set_title('Wave Rose Plot for All Ship Data', fontsize=12)
        # Set clockwise direction for theta (degrees)
        ax.set_theta_direction(-1)
        # Set zero location to North (top of the plot)
        ax.set_theta_zero_location('N')
       

        # Draw the plot
        self.canvas.draw()

        # Draw the plot
        self.canvas.draw()

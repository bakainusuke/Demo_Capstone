import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Sample DataFrame (replace this with your actual DataFrame)
data = {
    'ship_type': ['Cargo', 'Tanker', 'Fishing', 'Passenger'],
    'course': [120, 105, 95, 110]
}
df = pd.DataFrame(data)


class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a vertical layout for the widget
        layout = QVBoxLayout(self)

        # Create matplotlib figure and canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def plot_mean_course(self):
        # Calculate mean course by ship type
        mean_course_by_type = df.groupby(
            'ship_type')['course'].mean().sort_index()

        # Clear previous plot
        self.ax.clear()

        # Plot bar chart
        mean_course_by_type.plot(kind='bar', color='purple', ax=self.ax)
        self.ax.set_title('Mean Course by Ship Type')
        self.ax.set_xlabel('Ship Type')
        self.ax.set_ylabel('Mean Course (degrees)')
        self.ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Draw the plot
        self.canvas.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and geometry
        self.setWindowTitle("Mean Course by Ship Type")
        self.setGeometry(100, 100, 800, 600)

        # Create GraphWidget instance and add to main window
        self.graph_widget = GraphWidget(self)
        self.setCentralWidget(self.graph_widget)

        # Plot initial data
        self.graph_widget.plot_mean_course()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

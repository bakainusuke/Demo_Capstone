import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from wave_rose_widget import WaveRoseWidget
import pandas as pd
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Wave Rose Graph Example')
        self.setGeometry(100, 100, 800, 600)

        # Create the wave rose widget
        self.wave_rose_widget = WaveRoseWidget(self)
        self.setCentralWidget(self.wave_rose_widget)

        # Sample ship data (replace this with your actual DataFrame containing ship data)
        data = {
            # Example ship speeds (1-20 knots)
            'speed': np.random.randint(1, 20, 100),
            # Example ship courses (0-359 degrees)
            'course': np.random.randint(0, 360, 100),
            # Example ship types (including NaN)
            'ship_type': np.random.choice(['Cargo', 'Fishing Vessel', 'High-Speed Craft', np.nan], 100)
        }
        df = pd.DataFrame(data)

        # Plot the wave rose graph using the widget
        self.wave_rose_widget.plot_wave_rose(df)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

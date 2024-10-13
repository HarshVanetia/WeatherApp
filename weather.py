import sys
import requests
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt 


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.input_city = QLineEdit(self)
        self.button = QPushButton("Confirm", self)
        self.temprature = ...

def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())








if __name__ == "__main__":
    main()
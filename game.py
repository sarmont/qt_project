import sys
import os
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRadioButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.images = os.listdir("images")
        random.shuffle(self.images)
        self.buttonGroup.buttonClicked.connect(self.complexity_change)
        self.result_fild = []
        self.buttons_on_fild = []
        self.my_images = []

    def complexity_change(self):
        radio = self.sender()
        indexOfChecked = [radio.buttons()[x].isChecked() for x in
                          range(len(radio.buttons()))].index(True)
        if indexOfChecked == 0:
            self.create_fild(0)
        elif indexOfChecked == 1:
            self.create_fild(1)
        elif indexOfChecked == 2:
            self.create_fild(2)

    def create_fild(self, complexity):
        self.deleteAll()

        button_size = 60
        n = -1
        if complexity == 0:
            n = 4

        elif complexity == 1:
            n = 6

        elif complexity == 2:
            n = 8

        self.my_images = self.images[:n * 2]
        self.my_images = self.my_images + self.my_images
        random.shuffle(self.my_images)

        positions = [(i, j) for i in range(n) for j in range(n)]
        for position in positions:
            button = QPushButton(self)
            button.setFixedWidth(button_size)
            button.setFixedHeight(button_size)
            # self.element = my_images.pop()
            # button.setIcon(QIcon(f"images/{element}"))
            # self.result_fild.append(element)
            self.buttons_on_fild.append(button)
            button.clicked.connect(self.click_fild_button)
            self.grid.addWidget(button, *position)

    def click_fild_button(self):
        clicked_button = self.sender()
        if clicked_button in self.buttons_on_fild:
            button_index = self.buttons_on_fild.index(clicked_button)
            print(button_index)
            clicked_button.setIcon(QIcon(f"images/{self.my_images[button_index + 1]}"))
            clicked_button.setIconSize(QSize(50, 50))

    def deleteAll(self):
        while self.grid.count():
            item = self.grid.takeAt(0)
            widget = item.widget()
            widget.deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

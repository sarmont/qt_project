import sys
import os

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QTimer
import random


class FildButton(QPushButton):
    def __init__(self, image, index):
        super().__init__()
        self.button_size = 60
        self.isClicked = False
        self.image = image
        self.index = index
        self.setFixedWidth(self.button_size)
        self.setFixedHeight(self.button_size)
        self.opened = False


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.images = os.listdir("images")
        self.timer = QTimer()
        self.buttonGroup.buttonClicked.connect(self.complexity_change)
        self.start_position()
        print(self.images)
        self.progressBar.setValue(0)

    def start_position(self):
        random.shuffle(self.images)
        self.result_fild = []
        self.buttons_on_fild = []
        self.my_images = []
        self.click_counter = 0
        self.attempts = 0
        self.opened = 0

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

        n = -1
        if complexity == 0:
            n = 4

        elif complexity == 1:
            n = 6

        elif complexity == 2:
            n = 8

        self.my_images = self.images[:n ** 2 // 2]
        self.my_images = self.my_images + self.my_images
        random.shuffle(self.my_images)

        positions = [(i, j) for i in range(n) for j in range(n)]
        for position in positions:
            # self.element = my_images.pop()
            # button.setIcon(QIcon(f"images/{element}"))
            # self.result_fild.append(element)
            index = position[0] * n + position[1]
            button = FildButton(self.my_images[index], index)

            self.buttons_on_fild.append(button)
            button.clicked.connect(self.click_fild_button)
            self.grid.addWidget(button, *position)
        print(list(self.buttons_on_fild))

    def click_fild_button(self, n):
        clicked_button = self.sender()
        self.click_counter += 1
        if clicked_button.isClicked is False and clicked_button.opened is False:
            clicked_button.isClicked = True
            clicked_button.setIcon(QIcon(f"images/{clicked_button.image}"))
            clicked_button.setIconSize(QSize(50, 50))
        # print([el.isClicked for el in self.buttons_on_fild])
        if self.click_counter % 2 == 0:
            self.timer.singleShot(2000, self.check_similar)

    def check_similar(self):
        self.attempts += 1
        self.attempts_counter.setText(str(self.attempts))
        btn1, btn2 = [el for el in self.buttons_on_fild if el.isClicked is True and not el.opened]
        print(btn2.image, btn1.image)

        if btn1.image == btn2.image:
            btn1.opened = True
            btn2.opened = True
            self.opened += 1
            self.opened_images_pair.setText(
                f"Открыто пар картинок: {str(self.opened)} из {str(len(self.buttons_on_fild) // 2)}")
            self.progressBar.setValue(int(self.opened // (len(self.buttons_on_fild) // 2) * 100))
        else:
            btn1.isClicked = False
            btn2.isClicked = False
            btn1.setIcon(QIcon())
            btn2.setIcon(QIcon())

    def deleteAll(self):
        while self.grid.count():
            item = self.grid.takeAt(0)
            widget = item.widget()
            widget.deleteLater()
        self.start_position()

    def is_finish_situation(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

import sys
import os
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRadioButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.images = os.listdir("images")
        print(self.images)
        self.names = ['Cls', 'Bck', '', 'Close',
                      '7', '8', '9', '/',
                      '4', '5', '6', '*',
                      '1', '2', '3', '-',
                      '0', '.', '=', '+']
        self.buttonGroup.buttonClicked.connect(self.complexity_change)



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
        self.start_text.isVisible = False
        button_size = 60
        n = -1
        if complexity == 0:
            n = 4

        elif complexity == 1:
            n = 6

        elif complexity == 2:
            n = 8


        positions = [(i, j) for i in range(n) for j in range(n)]
        for position in positions:
            button = QPushButton(self)
            button.setFixedWidth(button_size)
            button.setFixedHeight(button_size)
            button.setIcon(QIcon(f"images/{self.images[position[0]]}"))
            button.setIconSize(QSize(50, 50))
            self.grid.addWidget(button, *position)

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

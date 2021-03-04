import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PIL import Image


class GUILayout(QMainWindow):
    def __init__(self):
        super().__init__()

        self.image_dict = {
            0: 'assets/imgs/1.png',
            1: 'assets/imgs/2.png',
            2: 'assets/imgs/3.png'
        }

        self.current_image_index = 0
        self.setWindowTitle("Medhub exercise")
        self.setFixedSize(1280, 1080)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.create_left_button())
        self.create_image_container()
        self.layout.addWidget(self.create_next_button())
        self.layout.addWidget(self.create_previous_button())
        self.layout.addWidget(self.create_save_button())

    def create_left_button(self):
        button = QPushButton('Close', self)
        button.setGeometry(50, 50, 100, 100)
        button.clicked.connect(self.close_window)
        return button

    def close_window(self):
        GUILayout.close(self)

    def create_image_container(self):
        self.label = QLabel(self)
        self.label.setGeometry(150, 180, 850, 650)
        self.layout.addWidget(self.label)
        self.load_image(self.current_image_index)
        return self.label

    def load_image(self, image_index):
        image_path = self.image_dict[image_index]
        pixmap = QPixmap(image_path)
        bigger_pixmap = pixmap.scaled(850, 650, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(bigger_pixmap)

    def create_next_button(self):
        next_button = QPushButton('Next', self)
        next_button.setGeometry(1050, 180, 150, 50)
        next_button.clicked.connect(self.next_image)
        return next_button

    def next_image(self):
        self.previous_button.setVisible(True)
        if self.current_image_index < 2:
            self.current_image_index += 1
            self.load_image(self.current_image_index)

    def create_previous_button(self):
        self.previous_button = QPushButton('Previous', self)
        self.previous_button.setGeometry(1050, 250, 150, 50)
        self.previous_button.setVisible(False)
        self.previous_button.clicked.connect(self.return_to_first_image)
        return self.previous_button

    def return_to_first_image(self):
        self.current_image_index = 0
        self.load_image(self.current_image_index)
        self.previous_button.setVisible(False)

    def create_save_button(self):
        save_button = QPushButton('Save', self)
        save_button.setGeometry(475, 850, 200, 80)
        save_button.clicked.connect(self.save_image)
        return save_button

    def save_image(self):
        current_image_path = self.image_dict[self.current_image_index]
        image = Image.open(current_image_path)
        image.save("assets/saved_images/"+str(self.current_image_index+1)+".bmp")


def main():
    medhub_app = QApplication(sys.argv)
    view = GUILayout()
    view.showFullScreen()
    sys.exit(medhub_app.exec())


if __name__ == "__main__":
    main()

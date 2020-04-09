import sys
import json
from typing import List

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject

from ui import design
from network.perceptron import Perceptron
from functions.activation import binary_fun


def create_zero_list(length: int) -> List[int]:
    return [0] * length


def create_perceptrons() -> List[Perceptron]:
    return [
        Perceptron("0", pixel_number, binary_fun),
        Perceptron("1", pixel_number, binary_fun),
        Perceptron("2", pixel_number, binary_fun),
        Perceptron("3", pixel_number, binary_fun),
        Perceptron("4", pixel_number, binary_fun),
        Perceptron("5", pixel_number, binary_fun),
        Perceptron("6", pixel_number, binary_fun),
        Perceptron("7", pixel_number, binary_fun),
        Perceptron("8", pixel_number, binary_fun),
        Perceptron("9", pixel_number, binary_fun)
    ]


def save_file():
    with open('data/learning_data.json', 'w') as outfile:
        json.dump(object_to_learn, outfile, default=lambda o: o.__dict__, indent=4)


def convert_result(result: int) -> bool:
    return result == 1


def learn_perceptrons():
    with open("data/learning_data.json", "r") as infile:
        json_data = infile.read()
        learning_data = json.loads(json_data)
        inputs_list = []
        targets_list = []
        for learning_instance in learning_data:
            inputs_list.append(learning_instance[pixels_key])
            targets_list.append(learning_instance[classname_key])
        for perceptron in perceptrons:
            perceptron.learn_massive(inputs_list, targets_list)


class Application(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save_button.clicked.connect(save_file)
        self.done_button.clicked.connect(self.on_done_clicked)
        self.clear_button.clicked.connect(self.on_clear_clicked)
        self.learn_button.clicked.connect(self.on_learn_clicked)
        self.test_button.clicked.connect(self.on_test_clicked)

    def get_classname(self) -> str:
        return self.class_name.text()

    def get_pixel_buttons(self) -> List[QObject]:
        return list(filter(lambda x: "pixel" in x.objectName(), self.pixel_frame.children()))

    def get_pixels(self) -> List[int]:
        pixel_buttons = self.get_pixel_buttons()
        pixels = create_zero_list(len(pixel_buttons))
        for pixel_button in pixel_buttons:
            if pixel_button.isChecked():
                pixel_index = int(pixel_button.objectName().split("pixel", 1)[1])
                pixels[pixel_index - 1] = 1
        return pixels

    def on_done_clicked(self):
        object_to_learn.append({classname_key: self.get_classname(), pixels_key: self.get_pixels()})

    @staticmethod
    def on_learn_clicked():
        learn_perceptrons()
        for perceptron in perceptrons:
            print(perceptron.weights)

    def on_clear_clicked(self):
        for pixel_button in self.get_pixel_buttons():
            pixel_button.setChecked(False)
        self.output.clear()

    def on_test_clicked(self):
        result = ""
        for perceptron in perceptrons:
            result += "perceptron " + perceptron.name + ": " \
                      + str(convert_result(perceptron.test(self.get_pixels()))) + "\n"
        self.output.setPlainText(result)


classname_key = "classname"
pixels_key = "pixels"
pixel_number = 40
object_to_learn = []
perceptrons = create_perceptrons()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

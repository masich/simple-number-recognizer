# SimpleNumberRecognizer

### Perceptron-based simple number recognizer written using pure Python 3.
[![CodeFactor](https://www.codefactor.io/repository/github/masich/simple-number-recognizer/badge)](https://www.codefactor.io/repository/github/masich/simple-number-recognizer)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

This project is created just for fun and practice.

The project's goal is very primitive: the user "draws" some numbers (0-9) using buttons, and the program tries to guess the drawn number. You can teach an internal perceptron-based neural network or use a simple predefined learning dataset in a ```data``` folder. 

## Instruction
![Interface](images/readme/interface.png)

## For teaching
* Use buttons **(1)** to draw the number you want to teach the system.
* Give the name of the number class (0 - 9) by putting it into the Class name field **(4)**.
* Click the Done button **(5)**. Now your number and its class are saved into internal program memory.
* Repeat these two steps as often as you wish to teach the system as best as possible.
* Click the Save file **(8)**. All your inputted numbers and classes will be saved as ```data/learning_data.json```.
* Click on Learn button **(9)** to teach your system using ```data/learning_data.json```.

## For testing
* Click on Learn button **(9)** to teach your system using ```data/learning_data.json```.
* Use buttons **(1)** to draw the number.
* Click Test button **(2)** to try to recognize the number.
* The output will be displayed on the **(3)** field. Each perceptron corresponds to a particular number. For example, 
the system thinks that you have drawn the number 4 if the value of the perceptron 4 is ```True```.   
* To clear the input **(1)** and output **(3)** you can use Clear button **(7)**.

## Screenshots
![Example_1](images/readme/example_1.png)
![Example_2](images/readme/example_2.png)
![Example_3](images/readme/example_3.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

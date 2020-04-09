from random import randint
from copy import copy

default_weight_min = 1
default_weight_max = 10
default_iterations_number = 100_000
default_lr = 0.2  # learning rate
default_bias_input = 1


class Perceptron:
    def __init__(self, name, number_of_inputs, activation_function, bias_input=default_bias_input, lr=default_lr):
        self.name = name
        self.number_of_inputs = number_of_inputs
        self.activation_function = activation_function
        self.weights = [randint(default_weight_min, default_weight_max) / 10.0 for _ in range(number_of_inputs + 1)]
        self.bias_input = bias_input
        self.lr = lr

    def __sum(self, inputs):
        return sum(inputs[i] * self.weights[i] for i in range(self.number_of_inputs + 1))

    def __update_weights(self, inputs, err):
        for i in range(self.number_of_inputs + 1):
            self.weights[i] = self.weights[i] - self.lr * err * inputs[i]

    def learn(self, inputs, target, iterations=default_iterations_number):
        # Todo: fixme
        target = 1 if target == self.name else 0
        inputs = copy(inputs)
        inputs.append(self.bias_input)
        for iteration in range(iterations):
            if len(inputs) != self.number_of_inputs + 1:
                raise AttributeError
            result = self.__activate(inputs)
            if result == target:
                return iteration
            err = result - target
            self.__update_weights(inputs, err)
        return -1

    def learn_massive(self, inputs_list, targets_list, iterations=default_iterations_number):
        if len(inputs_list) != len(targets_list):
            raise AttributeError
        learned = 0
        for _ in range(iterations):
            for i in enumerate(inputs_list):
                learning_iter = self.learn(inputs_list[i], targets_list[i], iterations=iterations)
                if learning_iter != 0:
                    learned = 0
                else:
                    learned += 1
                if learned >= len(inputs_list):
                    return

    def test(self, inputs):
        inputs = copy(inputs)
        inputs.append(self.bias_input)
        return self.__activate(inputs)

    def __activate(self, inputs):
        return self.activation_function(self.__sum(inputs))

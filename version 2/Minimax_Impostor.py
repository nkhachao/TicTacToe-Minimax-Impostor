import numpy as np
import DNA_Data


def init():
    global input_layer_size
    global hidden_layers_sizes
    global hidden_layer_count
    global output_layer_size
    global loss_function
    global amplify

    # Define Hyperparameters
    input_layer_size = 9
    hidden_layers_sizes = [360]
    hidden_layer_count = 1
    output_layer_size = 9

    # Weights (parameters)
    set_DNA()


def process_DNA():
    input_weight = np.reshape(DNA_Data.DNA0,
                                   (input_layer_size, hidden_layers_sizes[0]))

    hidden_weights = []
    output_weight = np.reshape(DNA_Data.DNA2,
                              (hidden_layers_sizes[hidden_layer_count - 1], output_layer_size))

    # Biases
    hidden_biases = [np.array(DNA_Data.DNA1)]
    output_bias = np.array(DNA_Data.DNA3)

    return input_weight, hidden_weights, output_weight, hidden_biases, output_bias


def set_DNA():
    global input_weight
    global hidden_weights
    global output_weight
    global hidden_biases
    global output_bias

    input_weight, hidden_weights, output_weight, hidden_biases, output_bias = process_DNA()


def respond(input):
    # Propagate inputs though network
    output = propagate(input, input_weight, hidden_weights, output_weight, hidden_biases, output_bias)
    return output


def propagate(input, input_weight, hidden_weights, output_weight, hidden_biases, output_bias):
    to_hidden = np.dot(input, input_weight)
    for i in range(hidden_layer_count - 1):
        out_hidden = sigmoid(np.add(to_hidden, hidden_biases[i]))
        to_hidden = np.dot(out_hidden, hidden_weights[i])

    out_hiddens = sigmoid(np.add(to_hidden, hidden_biases[hidden_layer_count - 1]))
    to_output = np.dot(out_hiddens, output_weight)
    out_output = sigmoid(np.add(to_output, output_bias))

    return out_output


def sigmoid(input):
    clipped_input = np.clip(input, -500, 500)       # Prevent overflow
    # Apply sigmoid activation function to scalar, vector, or matrix
    return 1 / (1 + np.exp(-clipped_input))



class MinimaxImpostor(object):
    def make_move(self, board):
        move = respond(board)
        return move.argmax()

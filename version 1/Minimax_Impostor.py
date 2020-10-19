import numpy as np
import copy
import DNA_Data


class Brain(object):
    def __init__(self):
        # Define Hyperparameters
        self.input_layer_size = 9
        self.hidden_layers_sizes = [72,72]
        self.hidden_layer_count = 2
        self.output_layer_size = 1

        self.set_DNA(np.array(DNA_Data.data))

        # Output amplification (since sigmoid's maximum output is only 1)
        self.amplify = 8

    def process_DNA(self, DNA):
        # start: The starting index of the part of the weight group in the DNA sequence
        # end: The ending index of the part of the weight group in the DNA sequence
        input_weight_end = self.input_layer_size * self.hidden_layers_sizes[0]
        input_weight = np.reshape(DNA[0:input_weight_end],
                                       (self.input_layer_size, self.hidden_layers_sizes[0]))

        hidden_weights = []
        hidden_weight_start = input_weight_end
        hidden_weight_end = input_weight_end
        for i in range(1, self.hidden_layer_count):
            hidden_weight_end = hidden_weight_start + self.hidden_layers_sizes[i-1] * self.hidden_layers_sizes[i]
            hidden_weight = np.reshape(DNA[hidden_weight_start:hidden_weight_end],
                                  (self.hidden_layers_sizes[i-1], self.hidden_layers_sizes[i]))
            hidden_weights.append(hidden_weight)
            hidden_weight_start = copy.deepcopy(hidden_weight_end)

        output_weight_end = hidden_weight_end + self.hidden_layers_sizes[self.hidden_layer_count - 1] * self.output_layer_size
        output_weight = np.reshape(DNA[hidden_weight_end:output_weight_end],
                                  (self.hidden_layers_sizes[self.hidden_layer_count - 1], self.output_layer_size))

        return input_weight, hidden_weights, output_weight

    def set_DNA(self, DNA):
        input_weight, hidden_weights, output_weight = self.process_DNA(DNA)
        self.input_weight = input_weight
        self.hidden_weights = hidden_weights
        self.output_weight = output_weight
        self.DNA_size = DNA.size

    def respond(self, input):
        # Propogate inputs though network
        output = self.propagate(input, self.input_weight, self.hidden_weights, self.output_weight)
        return output

    def propagate(self, input, input_weight, hidden_weights, output_weight):
        to_hidden = np.dot(input, input_weight)
        for i in range(self.hidden_layer_count - 1):
            out_hidden = self.sigmoid(to_hidden)
            to_hidden = np.dot(out_hidden, hidden_weights[i])

        out_hiddens = self.sigmoid(to_hidden)
        to_output = np.dot(out_hiddens, output_weight)
        out_output = self.sigmoid(to_output)

        output = out_output * self.amplify
        return output

    def sigmoid(self, input):
        clipped_input = np.clip(input, -500, 500)       # Prevent overflow
        return 1 / (1 + np.exp(-clipped_input))

class MinimaxImpostor(object):
    def __init__(self):
        self.brain = Brain()

    def make_move(self, board):
        move = self.brain.respond(board)
        return np.rint(move).astype(int)

# TicTacToe-Minimax-Impostor

Minimax Impostor is a neural network that plays Tic Tac Toe by mimicking Minimax algorithm. The goal is to create a less CPU intensive alternative to Minimax, which allows implementation on larger Tic Tac Toe boards.

Each major version of Minimax Impostor will be added as a separate file instead of replacing its predecessor.

### Quick Start Guide

To play Tic Tac Toe agaisnt Minimax Impostor, run Playground.py. No configuration needed

- Where the game lies: TicTacToe.py. A library for playing GUI Tic Tac Toe on Python
- Where the neural network lies: Minimax_Impostor.py
- Where the magic lies: DNA_Data.py. This is where parameters of the neural network are stored.
- No training code available. 

### Notes

Required libraries:
- numpy
- copy 
- tkinter

### Specifications

Version 1:

- Architecture: 4-layer (9-72-72-1) feedforward neural network.
- Parameter count: 5904 parameters.
- Activation function: sigmoid, sigmoid, sigmoid
- Fitness: about 955


Version 2:

- Architecture: 3-layer (9-360-9) feedforward neural network.
- Parameter count: 6849 parameters.
- Activation function: sigmoid, sigmoid
- Fitness: about 93

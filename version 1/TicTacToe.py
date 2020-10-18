import numpy as np
import copy
from tkinter import *
from tkinter import messagebox

class Game(object):
    def __init__(self):
        self.board_length = 9
        self.board_size = 3
        self.board = np.full((1, 9), 0)[0]
        self.current_player = -1
        self.winner = 0
        self.invalid_player = 0

    def reset(self):
        self.board = np.full((1, self.board_size * self.board_size), 0)[0]
        self.current_player = -1
        self.winner = 0
        self.invalid_player = 0

    def board_isnt_full(self):
        for block in self.board:
            if block == 0:
                return 1
        return 0

    def valid_move(self, move):
        if move < 0:
            return False

        if self.board[move] != 0:
            return False
        return True

    def find_winner(self):
        # check rows
        board_2D = self.board_2D()
        for row in range(0, 3):
            if board_2D[row][0] == board_2D[row][1] == board_2D[row][2] and board_2D[row][0] != 0:
                return board_2D[row][0]
        # check columns
        for col in range(0, 3):
            if board_2D[0][col] == board_2D[1][col] == board_2D[2][col] and board_2D[0][col] != 0:
                return board_2D[0][col]
        # check 1st diagonal
        if board_2D[0][0] == board_2D[1][1] == board_2D[2][2] and board_2D[0][0] != 0:
            return board_2D[0][0]
        # check 2nd diagonal
        if board_2D[0][2] == board_2D[1][1] == board_2D[2][0] and board_2D[0][2] != 0:
            return board_2D[0][2]
        return 0

    def board_2D(self):
        return np.reshape(self.board,
                       (self.board_size, self.board_size))

    def add_move(self, move):
        if not self.valid_move(move):
            self.winner = -self.current_player
            self.invalid_player = self.current_player
        self.board[move] = copy.deepcopy(self.current_player)
        if self.winner == 0:
            self.winner = self.find_winner()
        self.current_player = - self.current_player

    def add_human_move(self):
        human_input = list(map(int, input('Make your move (type 0-8 or row,column): ').split(',')))
        if len(human_input) > 1:
            move = self.board_size * human_input[0] + human_input[1]
        else:
            move = human_input[0]
        self.add_move(move)

    def print_board(self):
        print(self.board_2D())


class GUITicTacToe(object):
    def __init__(self):
        self.game = Game()

        self.root = Tk()  # Window defined
        self.root.title("Tic-Tac-Toe")  # Title given
        self.gui_board = [[], [], []]
        for i in range(3):
            for j in range(3):
                self.gui_board[i].append(self.button(self.root))
                self.gui_board[i][j].config(command=lambda row=i, col=j: self.click(row, col))
                self.gui_board[i][j].grid(row=i, column=j)

    def button(self, frame):          #Function to define a button
        return Button(frame,padx=1,bg="white",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)

    def reset(self):                #Resets the game
        temp = copy.deepcopy(self.game.current_player)
        self.game.reset()
        self.game.current_player = temp
        for i in range(self.game.board_size):
            for j in range(self.game.board_size):
                    self.gui_board[i][j]["text"] = " "
                    self.gui_board[i][j]["state"] = NORMAL

    def current_player(self):
        if self.game.current_player == -1:
            return 'x'
        else:
            return 'o'

    def click(self, row,column):
        move = self.game.board_size * row + column
        self.add_move(move)
        self.extra_actions()

    def add_move(self, move):
        colour = {'x': 'red', 'o': "black"}
        invalid_player = {-1: ' Bot made an invalid move', 1: ' You made an invalid move', 0:''}
        row = int(move / self.game.board_size)
        column = int(move % self.game.board_size)
        self.gui_board[row][column].config(text=self.current_player(), state=DISABLED, disabledforeground=colour[self.current_player()])
        self.game.add_move(move)
        if self.game.winner == 1:
            messagebox.showinfo("You won!","You won!" + invalid_player[self.game.invalid_player])
            self.reset()
        elif self.game.winner == -1:
            messagebox.showinfo("Bot won!","Bot won!" + invalid_player[self.game.invalid_player])
            self.reset()
        elif not self.game.board_isnt_full():
            messagebox.showinfo("Draw", "Its a draw! Board is full")
            self.reset()

    def extra_actions(self):
        return

    def human_vs_human(self):
        def do_nothing():
            return

        self.extra_actions = do_nothing
        self.root.mainloop()

    def human_vs_bot(self, bot):
        def bot_move():
            self.add_move(bot.make_move(self.game.board))
            return

        self.extra_actions = bot_move
        human_first = messagebox.askyesno("askyesno", "Do you wanna go first?")
        if human_first:
            self.game.current_player = 1
        else:
            self.game.current_player = -1
            self.add_move(bot.make_move(self.game.board))

        self.root.mainloop()
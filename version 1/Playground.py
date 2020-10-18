import TicTacToe
import Minimax_Impostor

gui_game = TicTacToe.GUITicTacToe()
bot = Minimax_Impostor.MinimaxImpostor()

gui_game.human_vs_bot(bot)


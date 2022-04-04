from player import HumanPlayer, RandomPlayer, AI_Player

class Tic_Tac_toe:
	def __init__(self):
		self.board = [[' ' for row in range(3)] for col in range(3)]
		self.cells = [cell for cell in self.cells]

	def display_board(self):
		"""Displays Header, tic-tac-toe board, and displays currently player position."""
		for index,row in enumerate(self.cells):
			print(f'{row[0]} | {row[1]} | {row[2]}')

	def make_move(self, player_move):
		""""Recieves player move and updates to constructor"""
		pass

	def available_moves(self):
		"""Sees what moves are available"""
		pass



def play():
	pass
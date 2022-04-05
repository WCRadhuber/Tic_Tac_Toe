from player import HumanPlayer
import os

class Tic_Tac_Toe:
	def __init__(self):
		self.num_row = 3
		self.num_col = 3
		self.board = [[' ' for row in range(self.num_row)] for col in range(self.num_col)]
		self.cells = [i for self.cells in self.board for i in self.cells]

	def display_board(self):
		"""Displays Header, tic-tac-toe board, and displays currently player position."""
		os.system("clear")
		print("Welcome to Tic-Tac-Toe")
		for index,row in enumerate(self.board):
			if index <= 2:
				print(f' {row[0]} | {row[1]} | {row[2]} ')
			if index < 2:
				print("___________")

	def make_move(self, player_move, player_letter):
		""""Recieves player move and updates to constructor"""
		self.cells[player_move] = player_letter
		self.board = [self.cells[i:i+self.num_row] for i in range(0, len(self.cells), self.num_col)]

	def available_moves(self):
		"""Returns available moves"""
		return [i for i, x in enumerate(self.cells) if x == " "]

	def is_winner(self, letter):
		"""Returns True or False dependent on win or not"""
		win = [letter, letter, letter]
		columns = [[col[i] for col in self.board] for i in range(self.num_col)]
		diagonal_1 = [self.board[i][i] for i in range(len(self.board))]
		diagonal_2 = [self.board[i][len(self.board) - 1 - i] for i in range(len(self.board))]
		#Check row for win
		for row in self.board:
			if row == win:
				return True
		"""check Column for win"""
		for col in columns:
			if col == win:
				return True
		"""checks diagonals for win """
		if diagonal_1 == win or diagonal_2 == win:
			return True
		return False



def play(game, player_1, player_2):
	"""Main play function"""

	while game.available_moves():
		game.display_board()
		player_1.get_name("Player 1")
		player_2.get_name("Player 2")
		
		player_1.get_letter()

		if player_1.letter == 'x':
			player_2.letter = 'o'
		if player_1.letter == 'o':
			player_2.letter = 'x'

		game.display_board()
		player_1.get_move(t)
		game.make_move(player_1.current_move, player_1.letter)
		game.display_board()
		if game.is_winner(player_1.letter):
			print(f"Congragulations {player_1.name}!!! You Win!!!")
			break

		player_2.get_move(t)
		game.make_move(player_2.current_move, player_2.letter)
		game.display_board()
		if game.is_winner(player_2.letter):
			print(f"Congragulations {player_2.name}!!! You Win!!!")
			break



if __name__ == '__main__':
	player_1 = HumanPlayer()
	player_2 = HumanPlayer()
	t = Tic_Tac_Toe()
	play(t, player_1, player_2)
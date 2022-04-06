from player import HumanPlayer
import os

class Tic_Tac_Toe:
	def __init__(self):
		self.num_row = 3
		self.num_col = 3
		self.board = [[' ' for row in range(self.num_row)] for col in range(self.num_col)]
		self.cells = [i for self.cells in self.board for i in self.cells]
		self.counter = 0

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

	def ask_replay(self):
		replay = input("Would you like to play again? y/n: ")
		if replay.lower() == 'y':
			return True
		elif replay.lower() == 'n':
			return False

			

	def reset(self, player_1, player_2):
		self.__init__()
		player_1.__init__()
		player_2.__init__()

def play(game, player_1, player_2):
	"""Main play function"""

	while True:
		"""Displays board and collects names once."""
		game.display_board()
		player_1.letter = 'X'
		player_2.letter = 'O'
		player_1.get_name("Player 1, (X)", game)
		player_2.get_name("Player 2, (O)", game)
		game.display_board()
		
		"""Switches player dependent on game counter number"""
		if game.counter % 2 == 0:
			player = player_1
		else:
			player = player_2

		"""Collects move from player and adds to game counter"""
		player.get_move(t)
		game.make_move(player.current_move, player.letter)
		game.display_board()
		game.counter += 1
		

		"""Checks for winner or tie. If either asks to replay"""
		if game.is_winner(player.letter):
			print(f"Congragulations {player.name}!!! You Win!!!")
			if game.ask_replay():
				game.reset(player_1, player_2)
			else:
				break
		elif not game.available_moves():
			game.reset(player_1, player_2)
			print("It's a tie!!!")
			if game.ask_replay():
				game.reset(player_1, player_2)
			else:
				break
			

if __name__ == '__main__':
	player_1 = HumanPlayer()
	player_2 = HumanPlayer()
	t = Tic_Tac_Toe()
	play(t, player_1, player_2)
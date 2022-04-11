import math
import random

class Player:
	"""Parent class for X and O players"""
	def __init__(self, name=None, letter=None, current_move=None):
		self.name = name
		self.letter = letter
		self.current_move = current_move


	def get_name(self, player, game):
		"""Collects name from human player"""
		if self.name == None:
			temp_name = input(f"{player} is your name?: ")
			if temp_name.isalpha():
				self.name = temp_name
			else:
				game.display_board()
				print("Invalid name. Try again.")
				self.get_name(player, game)
		else:
			pass


class HumanPlayer(Player):
	"""Class that colllects human player information"""
	def __init__(self):
		super().__init__(name=None, letter=None, current_move=None)
	

	def get_move(self, game):
		"""Collects move from human player and checks to see if valid move."""
		try:
			temp_move= int(input(f'{self.name}({self.letter}), please choose an available square 1-9: ')) - 1
			if temp_move in game.available_moves():
				self.current_move = temp_move
			else:
				print("Already guessed. Try again")
				self.get_move(game)
		except(TypeError, ValueError):
			print("Invalid Input. Try again.")
			self.get_move(game)


class ComputerPlayer(Player):
	"""Computer player that picks a square at random"""
	def __init__(self):
		super().__init__(name="Slow Eddie", letter=None, current_move=None)


	def get_move(self, game):
		"""Takes in game class, and returns a random choice of cell"""
		cell = random.choice(game.available_moves())
		self.current_move = cell
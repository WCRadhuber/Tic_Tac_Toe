

class Player:
	"""Defining the parent class for X and O players"""
	def __init__(self, name=None, letter=None, current_move=None):
		self.name = name
		self.letter = letter
		self.current_move = current_move


	def get_move(self):
		pass


class HumanPlayer(Player):
	def __init__(self):
		super().__init__(name=None, letter=None, current_move=None)
	
	def get_name(self, player):
		"""Collects name from human player"""
		if self.name == None:
			temp_name = input(f"{player} is your name?: ")
			if temp_name.isalpha():
				self.name = temp_name
			else:
				print("Invalid name. Try again.")
				self.get_name()
		else:
			pass

	def get_letter(self):
		"""Collects name from human player"""
		if self.letter == None:
			letter = input(f"{self.name} letter would you like to play, X or O?: ")
			if letter.lower() == 'x' or 'o':
				self.letter = letter.lower()
			else:
				print("Invalid character. Try again.")
				self.get_letter()
		else:
			pass

	def get_move(self, game):
		"""Collects move from human player and checks to see if valid move."""
		try:
			temp_move= int(input(f'{self.name}({self.letter}), please choose an available square 1-9: ')) - 1
			if temp_move in game.available_moves():
				self.current_move = temp_move
		except(TypeError, ValueError):
			print("Invalid Input. Try again.")
			self.get_move()



# class RandomPlayer(Player):
# 	def __init__(self):
# 		super().__init__(self, name="Slow Eddie", letter=None)


# 	def get_letter(self):
# 		"""Determines letter based on human or computer choice"""
# 		pass

# 	def get_move(self, game):
# 		"""Takes in game class, and returns a random choice of cell"""
# 		cell = random.choice(game.available_moves())
# 		self.current_move = cell


# class AI_Player(Player):
# 	def __init__(self, name="Unbeatable Joe"):
# 		super().__init__(self, name="Unbeatable Joe", letter =None)

# 	def get_letter(self):
# 		"""Determines letter based on human or computer choice"""
# 		pass

# 	def get_move(self):
# 		"""Collects move from AI"""
# 		pass
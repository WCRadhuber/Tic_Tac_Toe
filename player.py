class Player:
	"""Defining the parent class for X and O players"""
	def __init__(self, name=None):
		self.name = name


	def get_move(self):
		pass


class HumanPlayer(Player):
	def __init__(self, name):
		super().__init__(self, name=None)
		pass
	
	def get_name(self):
		"""Collects name from human player"""
		pass

	def get_move(self):
		"""Collects move from human player and checks to see if valid move."""
		pass

class RandomPlayer(Player):
	def __init__(self, name=""):
		super().__init__(self, name="")

class AI_Player(Player):
	def __init__(self, name="Unbeatable Joe"):
		super().__init__(self, name="Unbeatable Joe")

	def get_move(self):
		"""Collects move from AI"""
		pass
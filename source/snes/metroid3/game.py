from source.meta.gui.gamelib import GameParent

class Game(GameParent):
	def __init__(self):
		super().__init__()
		# FIXME: Do we want to translate the game's display name?
		self.name = "Super Metroid"			#to be replaced by a name like "Super Metroid"
		self.console_name = "snes"			#to be replaced by the console name, e.g. "snes"
		self.internal_name = "metroid3"	#to be replaced by the specific folder name that this app uses, e.g. "metroid3"

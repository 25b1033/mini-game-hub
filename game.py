import sys
import numpy as np

from abc import ABC, abstractmethod

player1 = sys.argv[1]
player2 = sys.argv[2]

#------------------------------------------BASECLASS---------------------------------------------------------------

class Gamebase(ABC):
	"""
	Base class for all 2-player, turn-based board games.
	Handles player info, turn switching, and board initialization.
	Subclasses must implement check_win().
	"""

	def __init__(self, player1, player2, board_shape):
		#Initialize the game with players and board shape.

		self.players = [player1,player2]          #arraymwith player names
		self.currentplayerindex = 0               #array index of the player whose turn it is
		self.board = np.zeros(board_shape)        #numpy array for the game board
	def switch_turn(self):
		#This is a function implemented to switch turns
		#the turn switching for othello comes with se conditions whic shall be looked into its class.

		self.currentmove = 1 - self.currentmove

	def currentturn_player(self):
		#This function is implemented to return the player name whose turn it is

		return self.players[self.currentplayerindex]

	@abstractmethod
	def check_win(self):
		"""
		Abstract method for checking win/draw.
        	Subclasses must implement this.	
		"""
		pass

#--------------------------------------------------------------------------------------------------------------------

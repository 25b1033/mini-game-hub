#Importing required libraries
import numpy as np
import pygame
from game import Gamebase

#Class for Connect4
class Connect4(Gamebase):
	
	def __init__(self,player1,player2):
		#inherit the consturctor from the base class
		super().__init__(player1,player2,(7,7))

	def checkmove(self, row, column):
		#This function checks if the click is inside the board and the column has a empty cell or not
		if 0<= column <7 and self.board[0][column] == 0:
			return True
		else:
			return False

	def make_move(self,row,column):
		#This function is to implement move that is made by the click
		if self.checkmove(row,column):
			for r in range(6,-1,-1):
				if self.board[r][column] == 0:
					self.board[r][column] = -2*(self.currentplayerindex) + 1
					return True
		else:
			return False

	def valid_move(self):
		#This function check the next player has a valid move or not
		return (self.board[0] == 0).any()

	def check_win(self):
		#This function is to check win/draw and return 0 in game is ongoing, 1 if it is a win, 2 if it is a draw

		t = self.board
		row = t[:, :-3] + t[:, 1:-2] + t[:, 2:-1] + t[:, 3:]
		column = t[:-3, :] + t[1:-2, :] + t[2:-1, :] + t[3:, :]
		diag1 = t[:-3, :-3] + t[1:-2, 1:-2] + t[2:-1, 2:-1] + t[3:, 3:]
		diag2 = t[3:, :-3] + t[2:-1, 1:-2] + t[1:-2, 2:-1] + t[:-3, 3:]
		
		#Check row for win
		if np.max(row) == 4 or np.min(row) == -4:
			return 1
		#Check column for win
		elif np.max(column) == 4 or np.min(column) == -4:
			return 1
		#Check diagonal for win
		elif np.max(diag1) == 4 or np.min(diag1) == -4:
			return 1
		#Check anti-diagonal for win
		elif np.max(diag2) == 4 or np.min(diag2) == -4:
			return 1
		#Check draw condition
		elif not self.valid_move():
			return 2
		#if not the game is still ongoing
		else:
			return 0
		
	def draw_piece(self,screen,cellsize):
		#This function draws the piece by checking the numpy array
		for r in range(7):
			for c in range(7):
				if self.board[r][c] != 0:
					center_x = c*cellsize + 100 + cellsize//2
					center_y = r*cellsize + 100 + cellsize//2
					
					if self.board[r][c] == 1:
						pygame.draw.circle(screen,(255,0,0),(center_x,center_y),cellsize//2 - 5)
					else:
						pygame.draw.circle(screen,(0,0,255),(center_x,center_y),cellsize//2 - 5)


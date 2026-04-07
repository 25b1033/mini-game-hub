import numpy as np
import pygame

class Connect4(GameBase):
	
	def __init__(self,player1,player2):
		
		super().__init__(player1,player2,(7,7))

	def checkmove(self, row, column):

		if 0<= column <7 and self.board[0][column] == 0:
			return True
		else:
			return False

	def make_move(self,row,column):
	
		if self.checkmove(row,column):
			for r in range(6,-1,-1):
				if self.board[r][column] == 0:
					self.board[r]column] == self.currentplayerindex + 1
					return True
		else
			return False

	def valid_move(self):
		return (self.board[0] == 0).any()


	def checkwin(self):
		
	def draw_piece(self,screen,cellsize):
		for r in range(7):
			for c in range(7):
				if self.board[r][c] != 0:
					center_x = c*cellsize + 100 + cellsize//2
					center_y = r*cellsize + 100 + cellsize//2
					
					if self.board[r][c] == 1:
						pygame.draw.circle(screen,(255,0,0),(center_x,center_y),cellsize//2 - 5)
					else:
						pygame.draw.circle(screen,(0,0,255),(center_x,center_y),cellsize//2 - 5)


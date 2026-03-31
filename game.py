#Importing sys fo command line arguments
import sys
#Importing numpy lib for board array
import numpy as np
#Importing pygame for GUI menu and Gameplay
import pygame
#Importing ABC(Abstract Base Class) and abstract method to allow creating a base class with methods that must be implemented by all subclasses
from abc import ABC, abstractmethod
#Importing specific game classes from the games package so that the menu can create instances of each game when selected
from games.tictactoe import TicTactoe
from games.connect4 import Connect4
from games.othello import Othello

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

#---------------------------------------------Setting up the window-----------------------------------------------------------------------
#initialise pygame
pygame.init()

#Set up the window
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("MINI GAME HUB")
font = pygame.font.Font(None, 40)

#-----------------------------------------GAME MENU-----------------------------------------------------------------------------------

#Function to display main menu with three game buttons
def show_menu():
	screen.fill((0,0,0)) #black background

	#Hardcoded buttons
	rect1 = pygame.Rect(200, 100, 200, 100)
	rect2 = pygame.Rect(200, 250, 200, 100)
	rect3 = pygame.Rect(200, 400, 200, 100)

	pygame.draw.rect(screen, (100,200,100) , rect1)
	pygame.draw.rect(screen, (100,200,100) , rect2)
	pygame.draw.rect(screen, (100,200,100) , rect3)

	# Blitting by creating a surface with required text
	screen.blit(font.render("TicTacToe", True, (0,0,0)),(rect1.x + 50, rect1.y + 30))
	screen.blit(font.render("Connect4", True, (0,0,0)), (rect2.x + 50, rect2.y + 30))
	screen.blit(font.render("Othello" , True, (0,0,0)), (rect3.x + 50, rect3.y + 30))

	pygame.display.flip()
	
	# Returning buttons for click detection
	return rect1, rect2, rect3

# Function for main menu loop, waits for the players to select a game
def menu_loop():
    rect1, rect2, rect3 = show_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if rect1.collidepoint(pos):
                    return TicTacToe
                elif rect2.collidepoint(pos):
                    return Connect4
                elif rect3.collidepoint(pos):
                    return Reversi

	#Small delay to reduce CPU usage
        pygame.time.wait(50) 

#------------------------------------------------GAME LOOP------------------------------------------------------------------

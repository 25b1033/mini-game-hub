#---------------------------------------------------Importing necessary modules and libraries--------------------------------------------------------------
#Importing sys fo command line arguments
import sys
#Importing numpy lib for board array
import numpy as np
#Importing pygame for GUI menu and Gameplay
import pygame
#Importing ABC(Abstract Base Class) and abstract method to allow creating a base class with methods that must be implemented by all subclasses
from abc import ABC, abstractmethod
#importing path to read history.csv
from pathlib import Path
#importing pyplot to plot bargraph and pie chart
from matplotlib import pyplot as plt
#importing counter to count for plotting
from collections import Counter
from datetime import date
#importing subprocess to give command to terminal
import subprocess

player1 = sys.argv[1]
player2 = sys.argv[2]

#----------------------------------------------------------------------BASECLASS---------------------------------------------------------------

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
	
	@abstractmethod
	def valid_move(self):
		#Checks if the opponent has valid move or not and if not the function switch_turn will implement a pass
		pass
	def switch_turn(self):
		#This is a function implemented to switch turns
		if self.valid_move():
			self.currentplayerindex = 1 - self.currentplayerindex
		else:
			print("Player has no legal moves hence it is a pass")

	def otherplayer(self):
		self.other_player_index=1-self.currentplayerindex
		return self.players[self.other_player_index]
	
	def currentturn_player(self):
		#This function is implemented to return the player name whose turn it is

		return self.players[self.currentplayerindex]

	@abstractmethod
	def check_win(self):
		"""
		Abstract method for checking win/draw.
        	Subclasses must implement this.
		returns 0 if its not a win/draw
		returns 1 if win
		returns 2 if it is a draw	
		"""
		pass
	@abstractmethod
	def checkmove(self,row,column):
		"""Abstract method for checking if a move is valid or not """

	@abstractmethod
	def make_move(self, row, column):
		"""
		Abstract method for making a move on (row,column)
		returns true if move was applied
		returns false if the move is invalid 
		Subclasses must implement rule
		"""
		pass

	@abstractmethod
	def draw_piece(self,screen,cellsize):
		"""
		Abstract method for drawing piece by reading the numpy array
		"""

#---------------------------------------------------------------------Setting up the window-------------------------------------------------------------------------------
#initialise pygame
pygame.init()

#Set up the window
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("MINI GAME HUB")
font = pygame.font.Font(None, 40)

#----------------------------------------------------------------------------GAME MENU-----------------------------------------------------------------------------------

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
				pygame.quit() #close pygame window
				sys.exit() #Exit program
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos
				if rect1.collidepoint(pos):
					from games.tictactoe import TicTactoe #importing  class Tictactoe from game file
					return TicTactoe
				elif rect2.collidepoint(pos):
					from games.connect4 import Connect4 #Importing class connect4 from the respective game file
					return Connect4
				elif rect3.collidepoint(pos):
					from games.othello import Othello #Importing class Othello from the respective game file
					return Othello

	#Small delay to reduce CPU usage
		pygame.time.wait(50)
#----------------------------------------------------------------------------------------------------------------------------------------------
#define path to history.csv
history=Path("history.csv")

#record results of game-----------------------------------------------------------------------------------------------------------------
def record_result(winner,loser,game):
        with history.open("a") as f:
                f.write("\n"+winner + "," + loser + "," + str(date.today()) + "," + game)

#show leaderboard-----------------------------------------------------------------------------------------------------------------------
def show_leaderboard():
        screen= pygame.display.set_mode((500,200)) #window to allow user to choose screen for leaderboard
        pygame.display.set_caption("Metric Choice")# set title for window

        font = pygame.font.SysFont('Arial',20)#define font for display

        #define target for clicking
        win_btn =pygame.Rect(50,100,100,30)
        loss_btn =pygame.Rect(200,100,100,30)
        ratio_btn =pygame.Rect(350,100,100,30)

        running = True
        while running:
                #event loop so the window responds
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                #if wins is clicked then argument for leaderboard is wins and the program is closed
                                if win_btn.collidepoint(event.pos):
                                        arg = "wins" 
                                        running=False
                                elif loss_btn.collidepoint(event.pos):
                                        arg="losses"
                                        running=False
                                elif ratio_btn.collidepoint(event.pos):
                                        arg="ratio"
                                        running=False
                #fill screen with black color
                screen.fill((0,0,0))

                #draw target
                pygame.draw.rect(screen,(255,255,0),win_btn)
                pygame.draw.rect(screen,(255,255,0),loss_btn)
                pygame.draw.rect(screen,(255,255,0),ratio_btn)
        
                #define text to be written
                text= font.render("CHOOSE METRIC FOR LEADERBOARD",True,(255,255,255))
                win_text= font.render("WINS",True,(0,0,0))
                loss_text= font.render("LOSSES",True,(0,0,0))
                ratio_text= font.render("RATIO",True,(0,0,0))

                #write text
                screen.blit(text,(60,50))
                screen.blit(win_text,(70,105))
                screen.blit(loss_text,(210,105))
                screen.blit(ratio_text,(370,105))

                #update display
                pygame.display.update()

        subprocess.run(['bash','leaderboard.sh',arg])

#Visualization-------------------------------------------------------------------------------------------------------------------------------------
def plotting():
        with history.open() as f:
                f.readline() #skip header

                winners= [] #define a list of winners
                games= [] #define a list of games

                for line in f:
                        winner,loser,date,game = line.strip().split(",")
                        winners.append(winner) #add winner to list
                        games.append(game) #add game to list

        #plot bargraph and pie chart
        fig, (ax1,ax2) = plt.subplots(1,2)

        #count values and find top 5 for bar graph
        wins_count=Counter(winners)
        top5 = wins_count.most_common(5)
        names = [x[0] for x in top5]
        counts= [x[1] for x in top5]
        #plot bar graph
        ax1.bar(names,counts)
        ax1.set_title("Top 5 Players by win")
        ax1.set_xlabel("Name of player")
        ax1.set_ylabel("Number of wins")

        #draw pie chart
        game_counts=Counter(games)
        ax2.pie(game_counts.values(), labels=game_counts.keys(), autopct="%1.1f%%")
        ax2.set_title("Most Played Games")

        plt.show(block=False)
        plt.pause(1)

#post-game loop---------------------------------------------------------------------------------------------------------------------------------
def post_game_loop(screen):
		screen = pygame.display.set_mode((600, 600))
		pygame.display.set_caption("PLAY AGAIN")
		font = pygame.font.SysFont('Arial',20)#define font for display
		running=True
		play_btn=pygame.Rect(100,200,150,60)
		quit_btn=pygame.Rect(350,200,150,60)

		while running:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if play_btn.collidepoint(event.pos):
						return
					elif quit_btn.collidepoint(event.pos):
						pygame.quit()
						sys.exit()
			screen.fill((0,0,0))
			pygame.draw.rect(screen, (255,255,0), play_btn)
			pygame.draw.rect(screen, (255,255,0),  quit_btn)
			play_txt = font.render("Play Again", True, (0,0,0))
			quit_txt = font.render("Quit", True, (0,0,0))
			screen.blit(play_txt,(125,220))
			screen.blit(quit_txt,(395,220))
			pygame.display.update()
#-----------------------------------------------------------------------------GAME LOOP----------------------------------------------------------------------------------------


#Function to for the gameplay 
def gameplay(game_class):
	game = game_class(player1,player2) #creating a class object
	cellsize = 50 #defining cellsize
	rows,columns = game.board.shape #extracting no. of rows and columns
	running = True #variable to make sure game keeps running until exited
	winner = None #variable to store winner's name
	loser = None #variable to store loser's name

	#Main game loop , keeps running until win,draw or exit.
	while running:
		#Drawing game board
		screen.fill((100,100,100))
		for r in range(rows):
			for c in range(columns):
				rect = pygame.Rect(c*cellsize + 100, r*cellsize + 100, cellsize, cellsize)
				pygame.draw.rect(screen, (200,100,200), rect , 3)
	
		#Drawing the piece
		game.draw_piece(screen,cellsize)

		#Displaying which player's turn it is 
		text = font.render(f"{game.currentturn_player()}'s turn", True, (255, 255, 255))
		screen.blit(text,(100,30))
		pygame.display.flip()
		
		#Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()#close pygame window
				sys.exit() #Exit program
			elif event.type == pygame.MOUSEBUTTONDOWN:
				x,y = event.pos
				#Convert mouse click position to board coordinates
				column = (x-100) // cellsize
				row = (y-100) // cellsize
				#Attempt to make a move
				if game.make_move(row,column):
					# Check if the game has been won or drawn 
					result = game.check_win()
					if result == 0:
						# No win/draw -> switch turns
						game.switch_turn()
					elif result == 1:
						#Current player wins
						winner = game.currentturn_player()
						loser = game.otherplayer()
						running = False
					else: 
						#Draw
						winner = "Draw"
						running = False
	
	# Display the final result
	screen.fill((0, 0, 0))
	if winner == "Draw":
		win_text = font.render("It's a Draw!", True, (255, 255, 0))
	else:
		win_text = font.render(f"{winner} wins!", True, (255, 255, 0))
		record_result(winner,loser,game.__class__.__name__)
	screen.blit(win_text, (150, 250))
	pygame.display.flip()
	
	pygame.time.wait(3000)

	#Recording game results and analytics
	show_leaderboard()
	plotting()
	post_game_loop(screen)
#----------------------------------------------------------------------------------------MAIN FUNCTION--------------------------------------------------------------------------------------
def main():
	#Main program: shows menu , runs selected game, repeat.
	while True:
		game_class = menu_loop() #Wait for the player selection
		gameplay(game_class) #Runs the selected game

#Run the program 
if __name__ == "__main__":
	main()

from game import Gamebase
import pygame
import numpy as np
class TicTactoe(Gamebase):
    def __init__(self,player1,player2,):
        super().__init__(player1,player2,(10,10))
        self.move_count = [0,0]
        self.empty_index=np.arange(101)

    def valid_move(self):
        return (self.board == 0).any() #check if board is empty
    
    def checkmove(self,row,column):
        return 0<=row<10 and 0<=column<10 and self.board[row][column]==0 #check if move is inside board
    
    def make_move(self,row,column):
        if self.checkmove(row,column):
            a=self.empty_index
            if self.move_count[self.currentplayerindex]%3==2:
                b=np.random.choice(a,1)
                c=b[0]
                self.board[c//10][c%10]=-2*self.currentplayerindex+1
                a=a[a!=c]
            else:
                self.board[row][column]= - 2*self.currentplayerindex + 1 #set -1 for player with index 0 and 1 for player with index 1
                a=a[a!=10*row+column]
            self.move_count[self.currentplayerindex]+=1
            return True
        return False
    
    def check_win(self):
        t=self.board
        row = t[:,0:6] + t[:,1:7] + t[:,2:8] + t[:,3:9] + t[:,4:] #sum of cells of all possible sets of 5 adjacent cells in a row
        col = t[0:6,:] + t[1:7,:] + t[2:8,:] + t[3:9,:] + t[4:,:] #sum of cells of all possible sets of 5 adjacent cells in a col 
        diag1= t[0:6,0:6] + t[1:7,1:7] + t[2:8,2:8] + t[3:9,3:9] + t[4:,4:] #sum of cells of all possible sets of 5 adjacent cells in a diagonal
        diag2= t[4:,0:6] + t[3:9,1:7] + t[2:8,2:8] + t[1:7,3:9] + t[0:6,4:] #sum of cells of all possible sets of 5 adjacent cells in other diagonal

        #check in row
        #win conditions occur in max or min sum
        if np.max(row)==5 or np.min(row)==-5:
            return 1
        #check in column
        elif np.max(col)==5 or np.min(col)==-5:
            return 1        
        #check in diagonal
        elif np.max(diag1)==5 or np.min(diag1)==-5:
            return 1
        #check in antidiagonal
        elif np.max(diag2)==5 or np.min(diag2)==-5:
            return 1
        elif not self.valid_move():
            return 2
        else:
            return 0

    def draw(self,screen,cellsize):
        for r in range(10):
            for c in range(10):
                #draw the board
                b_x = 100 + c * cellsize
                b_y = 100 + r * cellsize
                pygame.draw.rect(screen,(255,255,255),(b_x,b_y,cellsize,cellsize),2)

		#posn to start the text
                x = c*cellsize + 100 + cellsize//4
                y = r*cellsize + 100 + cellsize//4

                font = pygame.font.SysFont('Arial',cellsize//2)# font

                if self.board[r][c]==-1:
                    o_txt=font.render("O",True,(79,245,0)) # draw O
                    screen.blit(o_txt,(x,y))
                elif self.board[r][c]==1:
                    x_txt=font.render("X",True,(245,74,0)) # draw X
                    screen.blit(x_txt,(x,y))


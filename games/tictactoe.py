from game import Gamebase
import pygame
import numpy as np
class TicTactoe(Gamebase):
    def __init__(self,player1,player2,):
        super().__init__(player1,player2,(10,10))

    def validmove(self):
        return (self.board[0] == 0).any()
    
    def checkmove(self,row,column):
        return row<=10 and column<=10 and self.board[row][column]==0
    
    def make_move(self,row,column):
        if self.checkmove():
            self.board[row][column]=-2*self.currentplayerindex + 1
            return True
        return False
    
    def check_win(self):
        t=self.board
        row = t[:,0:6] + t[:,1:7] + t[:,2:8] + t[:,3:9] + t[:,4:]
        col = t[0:6,:] + t[1:7,:] + t[2:8,:] + t[3:9,:] + t[4:,:]
        diag1= t[0:6,0:6] + t[1:7,1:7] + t[2:8,2:8] + t[3:9,3:9] + t[4:,4:]
        diag2= t[4:,0:6] + t[3:9,1:7] + t[2:8,2:8] + t[1:7,3:9] + t[0:6,4:]

        #check in row
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
        elif np.any(t==0):
            return 2
        else:
            return 0

    def draw_piece(self,screen,cellsize):
        for r in range(10):
            for c in range(10):
                x = c*cellsize + 100 + cellsize//4
                y = r*cellsize + 100 + cellsize//4

            font = pygame.font.SysFont('Arial',cellsize//2)

            if self.board[r][c]==-1:
                o_txt=font.render("O",True,(0,0,0))
                screen.blit(o_txt,(x,y))
            elif self.board[r][c]==1:
                x_txt=font.render("X",True,(0,0,0))
                screen.blit(x_txt,(x,y))
            
            pygame.display.update()
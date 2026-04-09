from game import Gamebase
import pygame
import numpy as np
class Othello(Gamebase):
    def __init__(self,player1,player2,):
        super().__init__(player1,player2,(8,8))
        self.board[3][3] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.board[4][4] = 1

    def valid_move(self):
        for r in range (8):
            for c in range (8):
                if self.checkmove(r,c):
                    return True
        return False
    
    def checkmove(self,row,column):
        if self.board[row][column]!=0:
            return False
        for r in range (-1,2):
            for c in range(-1,2):
                ar=row+r
                ac=column+c
                if 0<=ac<8 and 0<=ar<8 and self.board[ar][ac]==2-self.currentplayerindex:
                    for k in range (2,8):
                        dr= row+k*r
                        dc=column+k*c
                        if not (0<=dr<8 and 0<=dc<8):
                            break
                        if self.board[dr][dc]==self.currentplayerindex+1:
                            return True
                        if self.board[dr][dc]==0:
                            break
        return False
          
    def make_move(self,row,column):
        if self.checkmove(row,column):
            self.board[row][column]=self.currentplayerindex + 1
            for r in range(-1, 2):
                for c in range(-1, 2):
                    ar = row + r
                    ac = column + c
                    if 0 <= ar < 8 and 0 <= ac < 8 and self.board[ar][ac] == 2 - self.currentplayerindex:
                       for k in range(2, 8):
                        dr = row + k * r
                        dc = column + k * c
                        if not (0 <= dr < 8 and 0 <= dc < 8):
                            break
                        if self.board[dr][dc] == self.currentplayerindex + 1:
                            for m in range(1, k):  # start at 1, not 0
                                self.board[row + m * r][column + m * c] = self.currentplayerindex + 1
                            break
                        if self.board[dr][dc] == 0:
                            break
            return True
        return False
    
    def check_win(self):
        a=self.board
        p1=a[a==1]
        p2=a[a==2]
        if np.any(self.board==0):
            return 0
        elif p1.size==p2.size:
            return 2
        else:
            return 1

    def draw_piece(self,screen,cellsize):
        for r in range(8):
            for c in range(8):
                x = c*cellsize + 100 + cellsize//2
                y = r*cellsize + 100 + cellsize//2

                if self.board[r][c]==2:
                    pygame.draw.circle(screen,(255,255,255),(x,y),cellsize//3)
                elif self.board[r][c]==1:
                    pygame.draw.circle(screen,(0,0,0),(x,y),cellsize//3)    
from game import Gamebase
import pygame
import numpy as np
class Othello(Gamebase):
    def __init__(self,player1,player2,):
        super().__init__(player1,player2,(8,8))
        #initial center pieces
        self.board[3][3] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.board[4][4] = 1

    def valid_move(self):
        for r in range (8):
            for c in range (8):
                if self.checkmove(r,c):
                    return True #checks if move is possible for any square
        return False
    
    def checkmove(self,row,column):
        if 0<=row<8 and 0<=column<8 and self.board[row][column]==0:
            for r in range (-1,2):
                for c in range(-1,2):
                    ar=row+r #adjacent square row
                    ac=column+c #adjacent square column
                    if 0<=ac<8 and 0<=ar<8 and self.board[ar][ac]==2-self.currentplayerindex:
                        for k in range (2,8):
                            dr= row+k*r #row of squares in that direction
                            dc=column+k*c #column of squares in that direction
                            if not (0<=dr<8 and 0<=dc<8):
                                break #if out of range then break
                            if self.board[dr][dc]==self.currentplayerindex+1:
                                return True #checks for another piece of same colour for trap
                            if self.board[dr][dc]==0:
                                break #trap is not possible if any square is empty
        return False
          
    def make_move(self,row,column):
        if self.checkmove(row,column):
            self.board[row][column]=self.currentplayerindex + 1 #fill the numpy board
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
                                self.board[row + m * r][column + m * c] = self.currentplayerindex + 1 #change all trapped pieces
                            break
                        if self.board[dr][dc] == 0:
                            break
            return True
        return False
    
    def check_win(self):
        a=self.board
        p1=a[a==1]#array of '1's that appear in board
        p2=a[a==2]#array of '2's that appear in board
        if p1.size==0:
            self.currentplayerindex= 1#to set current player to the winning player
            return 1
        elif p2.size==0:
            self.currentplayerindex=0#to set current player to winning player
            return 1
        elif np.any(self.board==0):
            return 0#no draw conditions
        elif p1.size==p2.size:
            return 2#draw condition
        elif p1.size>p2.size:
            self.currentplayerindex=0
            return 1
        else:
            self.currentplayerindex=1
            return 1

    def draw(self,screen,cellsize):
        for r in range(8):
            for c in range(8):
                b_x = c * cellsize + 80
                b_y = r * cellsize + 80
                #center of cell
                x = c*cellsize + 80 + cellsize//2
                y = r*cellsize + 80 + cellsize//2
                rect=pygame.Rect(b_x,b_y,cellsize,cellsize)#draw green board
                pygame.draw.rect(screen,(0,255,0),rect)
                pygame.draw.rect(screen,(0,0,0),(b_x,b_y,cellsize,cellsize),1)#draw grid lines
                if self.board[r][c]==2:
                    pygame.draw.circle(screen,(255,255,255),(x,y),cellsize//3) #draw a white piece
                elif self.board[r][c]==1:
                    pygame.draw.circle(screen,(0,0,0),(x,y),cellsize//3) #draw a black piece
                font = pygame.font.SysFont('Arial',50) #font 
                a=self.board
                text=font.render("black: "+str(a[a==1].size),True,(255,255,255)) #text for score of black
                text2=font.render("White: "+ str(a[a==2].size),True,(255,255,255))#text for score of white
                #display score
                screen.blit(text,(80,10))
                screen.blit(text2,(700,10))    

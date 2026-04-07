from game import Gamebase
import pygame
import numpy as np
class TicTactoe(Gamebase):
    def __init__(self,player1,player2,):
        super().__init__(player1,player2,(10,10))

    def validmove():
        return True
    
    def checkmove():
        return row<=10 and column<=10 and self.board[row][column]
    
    def make_move():
        if self.checkmove():
            self.board.[row][col]=self.currentplayerindex + 1
            return True
        return False
    
    def draw_piece():
        for r in range(10):
            for c in range(10):
                x = c*cellsize + 100 + cellsize//4
                y = r*cellsize + 100 + cellsize//4

            font = pygame.font.SysFont('Arial',cellsize//2)

            if self.board[r][c]==2:
                o_txt=font.render("O",True,(0,0,0))
                screen.blit(o_txt,(x,y))
            elif self.board[r][c]==1:
                x_txt=font.render("X",True,(0,0,0))
                screen.blit(x_txt,(x,y))
            
            pygame.display.update()
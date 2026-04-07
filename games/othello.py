from game import Gamebase
import pygame
import numpy as np
class Othello(Gamebase):
    def __init__(self,player1,player2,):
        super().__init__(player1,player2,(8,8))

    def validmove():
        
    
    def checkmove():
        
    
    def make_move():
        if self.checkmove():
            self.board.[row][col]=self.currentplayerindex + 1
            return True
        return False
    
    def check_win():
        p1=a[a==1]
        p2=a[a==2]
        if p1.size > p2.size:
            return 1
        elif p2.size > p1.size:
            return 2
        else:
            return 0

    def draw_piece():
        for r in range(10):
            for c in range(10):
                x = c*cellsize + 100 + cellsize//2
                y = r*cellsize + 100 + cellsize//2

            font = pygame.font.SysFont('Arial',cellsize//2)

            if self.board[r][c]==2:
                pygame.draw.circle(screen,(255,255,255),(x,y),cellsize//3)
            elif self.board[r][c]==1:
                pygame.draw.circle(screen,(0,0,0),(x,y),cellsize//3)
        screen.fill((0,255,0))    
        pygame.display.update()
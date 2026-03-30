



































































































from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
from datetime import date
import pygame
import subprocess

#define path to history.csv
history=Path("history.csv")

'''#append the results of game to history.csv
with history.open("a") as f:
        f.write(winner + "," + loser + "," + str(date.today()) + "," + game + "\n")
'''

#show leaderboard
pygame.init()
metric= pygame.display.set_mode((500,200)) #window to allow user to choose metric for leaderboard
pygame.display.set_caption("Metric Choice")# set title for window

font = pygame.font.SysFont('Arial',20)#define font for display

#define target for clicking
win =pygame.Rect(50,100,100,30)
loss =pygame.Rect(200,100,100,30)
ratio =pygame.Rect(350,100,100,30)

running = True
while running:
        #event loop so the window responds
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        #if wins is clicked then argument for leaderboard is wins and the program is closed
                        if win.collidepoint(event.pos):
                                arg = "wins"
                                running=False 
                        elif loss.collidepoint(event.pos):
                                arg="losses"
                                running=False
                        elif ratio.collidepoint(event.pos):
                                arg="ratio"
                                running=False
        #fill screen with black color
        metric.fill((0,0,0))

        #draw target
        pygame.draw.rect(metric,(255,255,0),win)
        pygame.draw.rect(metric,(255,255,0),loss)
        pygame.draw.rect(metric,(255,255,0),ratio)
        
        #define text to be written
        text= font.render("CHOOSE METRIC FOR LEADERBOARD",True,(255,255,255))
        win_text= font.render("WINS",True,(0,0,0))
        loss_text= font.render("LOSSES",True,(0,0,0))
        ratio_text= font.render("RATIO",True,(0,0,0))

        #write text
        metric.blit(text,(60,50))
        metric.blit(win_text,(70,105))
        metric.blit(loss_text,(210,105))
        metric.blit(ratio_text,(370,105))

        #update display
        pygame.display.update()

pygame.quit()

subprocess.run(['bash','leaderboard.sh',arg])

#read  history.csv
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

plt.show()
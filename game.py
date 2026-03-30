



































































































from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt
from datetime import date

#define path to history.csv
history=Path("history.csv")

#append the results of game to history.csv
with history.open("a") as f:
	f.write(winner + "," + loser + "," + str(date.today()) + "," + game + "\n")

#read  history.csv
with history.open() as f:
	f.readline() #skip header
	
	winners= [] #define a list of winners
	games= [] #define a list of games

	for line in f:
		winner,loser,date,game = line.strip().split(",")
		winners.append(winner) #add winner to list
		games.append(game) #add game to list


plt.bar(names,counts)
plt.title("Top 5 Players by win")
plt.xlabel("Name of player")
plt.ylabel("Number of wins")
plt.show


plt.pie(game_counts.values(), labels=game_counts.keys(), autopct="%1.1f%%")
plt.title("Most Played Games")
plt.show()

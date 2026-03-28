#!/bin/bash

#store argument
sort_by=$1

#check if any game is played in history.csv
if[ ! -f history.csv ];then
	echo "No games played yet"
	exit 1
fi

#store  metric for sorting leaderboard
if[ "$sort_by" == "wins" ];then
	sort_col=2
elif[ "$sort_by" =="losses" ];then
	sort_col=3
else 
	sort_col=4
fi

#print header row
echo "Player	Wins	Losses	Ratio"
echo "-------------------------------"


#calculate the leaderboard data
awk ' BEGIN{ FS="," #define field separator } 
NR>1{
	wins[$1]++ #increase number of wins of winner
	losses[$2]++ #increase number of losses of loser
} 
END{
	for(player in wins){
		w=wins[player] #store number of wins of player in w
		l=losses[player] #store number of losses of player in l
		if(l==0)
			ratio=w
		else
			ratio= w/l #store win loss ratio in ratio
			printf "%s %d %d %.2f\n" , player , w , l , ratio 
	}
} '
history.csv| sort -k${sort_col} -rn | awk '{printf "%-15s %-5s %-7s %.2f\n" , $1, $2, $3, $4}' #sort the rows and use awk for formatting 


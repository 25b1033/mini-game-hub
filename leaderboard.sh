#!/bin/bash

#store argument
isort_by=$1

#check if any game is played in history.csv
if [ ! -f history.csv ]; then
	echo "No games played yet"
	exit 1
fi

#store  metric for sorting leaderboard
if [ "$sort_by" == "wins" ]; then
	sort_col=2
elif [ "$sort_by" == "losses" ]; then
	sort_col=3
else 
	sort_col=4
fi

#print header row
echo "Player          Wins  Losses  Ratio"
echo "-----------------------------------"


#calculate the leaderboard data
awk -F ',' ' 
NR>1 {
	wins[$1]++
	losses[$2]++
} 
END{
	for(player in wins){
		w=wins[player] 
		l=losses[player]
		if(l==0)
			ratio=w
		else
			ratio= w/l
			printf "%s %d %d %.2f\n" , player , w , l , ratio 
	}
} ' history.csv| sort -k${sort_col} -rn | awk '{printf "%-15s %-5s %-7s %.2f\n" , $1, $2, $3, $4}' #sort the rows and use awk for formatting 


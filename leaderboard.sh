sort_by=$1

if[ ! -f history.csv ];then
	echo "No games played yet"
	exit 1
fi

if[ "$sort_by" == "wins" ];then
	sort_col=2
elif[ "$sort_by" =="losses" ];then
	sort_col=3
else 
	sort_col=4
fi

echo "Player	Wins	Losses	Ratio"
echo "-------------------------------"


awk ' BEGIN{ FS="," } 
NR>1{
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
	}
} '
history.csv



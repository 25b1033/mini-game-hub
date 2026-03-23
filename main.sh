#!/bin/bash

USER_FILE="users.tsv"
echo "Welcome to Mini Game Hub"
# Function to hash password
hash_password(){
	echo -n "$1" | sha256sum | cut -d ' ' -f1 	
}
#Function to register a new user
register_user(){
	read -p "Enter a username:" username
	read -s -p "Enter a password:" password
	hpass=$(hash_password "$password")
	echo -e "$username\t$hpass" >> "$USER_FILE"	
}
#Function to authenticate existing users
authenticate_user(){
while true; do
	read -p "Enter a username: " username
	#Checks if user is existing or not
	if grep -q "^$username\t" "$USER_FILE"; then
		while true; do
			read -s -p "Enter password:" password
			pass=$(hash_password "$password")
			if grep -q "^$username[[:space:]]$pass$" "$USER_FILE"; then
				echo "Login successful!"
				echo "$username"
				return
			else 
				echo "Incorrect password. Try again."
			fi
		done
	#Ask if username wants to register
	else
		read -p "Username not found. Do you want to register? (y/n): " choice
			if [ "$choice" = "y" ]; then
				register_user
				echo "$username"
				return
			else 
				echo "Please enter username again."
				continue
			fi
	fi
done
}
user1=$(authenticate_user)
user2=$(authenticate_user)

# ensures that both the users are different 
while [ "$user1" = "$user2" ]; do
	echo "Error: Both users cannot have the same usernames."
	# Both usernames are the same, so resolve conflict by re-authenticating one user
	while true; do
		read -p "Which user wishes to re-login? (1/2): " choice
		if [ "$choice" = "1" ]; then
			user1=$(authenticate_user)
		elif [ "$choice" = "2" ]; then
			user2=$(authenticate_user)
		#invalid input re-prompt
		else 
			echo "Invalid input. Choose 1 or 2."
		fi
	done
done
# launch the game with the authenticated users
python3 game.py "$user1" "$user2"

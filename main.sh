
#!/bin/bash

#File to store username and hashed passwords
USER_FILE="users.tsv"

echo "Welcome to Mini Game Hub"

#---------------------------------------------------------------------------------
# Function to hash password
# Purpose: Takes a plaintext password and returns its SHA256 hash
#---------------------------------------------------------------------------------

hash_password(){
	echo -n "$1" | sha256sum | cut -d ' ' -f1 	
}

#-----------------------------------------------------------------------------------
#Function to register a new user
# Purpose: Registers a new user with unique username and confirmed password
#-----------------------------------------------------------------------------------

register_user(){
	#Loop until unique password is entered
	while true; do
		read -p "Enter a username:" username

		#checks for non empty username
		if [ -z "$username" ]; then
			echo "Username cannot be empty" >&2
			continue
		fi
		
		#Removes extra blank spaces from the input
		username=$(echo "$username" | xargs)

		if grep -q "^$username\t" "$USER_FILE"; then
			echo "Username already exists. Try another username" >&2
			continue
		else
			break
		fi
	done

	#loop until the password and confirm passwords match
	while true; do
		read -s -p "Enter a password: " password1
		printf "\n"

		#Enforces minimum password length requirement of 8 characters
		if [ ${#password1} -lt 8 ]; then
			echo "Password must be atleast 8 characters long" >&2
			continue
		fi
		read -s -p "Confirm password:" password2
		printf "\n"
		
		#Checks if the passwords match
		if [ "$password1" = "$password2" ]; then
			hpass=$(hash_password "$password1")
			echo -e "$username\t$hpass" >> "$USER_FILE"
			echo "Registration successful!" >&2
			reguser="$username"

			return
		else
			echo "Passwords do not match. Please try again." >&2
			continue
		fi
		break
	done
	return
}

#------------------------------------------------------------------------------------------------------
#Function to authenticate existing users
#Purpose: Authenticates a existing user and allows registration if user not found.
#------------------------------------------------------------------------------------------------------

authenticate_user(){
#Loop until valid login or registration
while true; do
	read -p "Enter a username: " username

	#Ensures username input is not empty
	if [ -z "$username" ]; then
		echo "Username cannot be empty" >&2
		continue
	fi

	#removes extra spaces
	username=$( echo "$username" | xargs )

	#Checks if user is exists
	if grep -q "^$username\t" "$USER_FILE"; then

		#password verification loop
		while true; do
			read -s -p "Enter password:" password
			printf "\n"
			if [ ${#password} -lt 8 ]; then
				echo "Password must be atleast 8 charcaters long." >&2
				continue
			fi
			pass=$(hash_password "$password")
			if grep -q "^$username\t$pass$" "$USER_FILE"; then
				echo "Login successful!" >&2
				echo "$username"
				return
			else 
				echo "Incorrect password. Try again." >&2
				continue
			fi
		done
	#Prompt user to register if username not found
	else
		while true; do
			read -p "Username not found. Do you want to register? (y/n): " choice
			if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
				register_user
				#returns newly registered username
				echo "$reguser"
				return
			elif [ "$choice" = "n" ] || [ "$choice" = "N" ]; then
				echo "Please enter username again." >&2
				break
			else
				echo "Invalid input. Please choose y or n" >&2
				continue
			fi
		done
	fi
done
}

#Authenticates two users
user1=$(authenticate_user | xargs)
user2=$(authenticate_user | xargs)
# ensures that both the users are different 
while [ "$user1" = "$user2" ]; do
	echo "Error: Both users cannot have the same usernames."
	# Both usernames are the same, so resolve conflict by re-authenticating one user
	while true; do
		read -p "Which user wishes to re-login? (1/2): " choice
		if [ "$choice" = "1" ]; then
			user1=$(authenticate_user | xargs)
			if [ "$user1" != "$user2" ]; then
				break
			else
				echo "Username is already taken by other user. Please try another username."
			fi
		elif [ "$choice" = "2" ]; then
			user2=$(authenticate_user | xargs)
			if [ "$user2" != "$user1" ]; then
				break
			else
				echo "Username is already taken by other user. Please try another username."
			fi
		#invalid input re-prompt
		else 
			echo "Invalid input. Choose 1 or 2." 
			continue
		fi
	done
done

# launch the game with the authenticated users
python3 game.py "$user1" "$user2"
# Mini game hub
This is a multi-user game built using Bash and Python(Pygame).
This allows two authenticated users to play board games via a graphical interface

#Project Structure
mini-game-hub/
│───────────── main.sh
│───────────── game.py
│───────────── leaderboard.sh
│
├───────────── games/
│ ├───────────────── tictactoe.py
│ ├───────────────── othello.py
│ └───────────────── connect4.py
│
├───────────── users.tsv
└───────────── history.csv

#Requirements
Ensure the following are installed in your system
- Python 3.10
- Bash
- python libraries(numpy,pygame,matplotlib)
If not install the required libraries
''' bash
pip install pygame-ce numpy matplotlib

#How to run
1. Navigate to the project directory
   cd mini-game-hub

2. Give execution permissions
   chmod +x main.sh
   chmod +x leaderboard.sh

3. Run the program
   bash main.sh

4. Authentication flow
   - The program starts from main.sh.
   - Two users are required to log in.
   - New users can register if their username doesn't exist.
   - Login credentials are being stored in users.tsv.

5. Execution flow
   - The program starts with a terminal-based authentication via main.sh.
   - After successful login, game.py launches.
   - A pygame window with the game menu opens.
   - Players choose the game which they wish to play from the menu.
   - The selected game runs in the Pygame window.
   - After the game :
     - The winner is displayed on the pygame window.
     - The same result is stored in history.csv.
     - A metric appears asking you to choose suitable options to view the stats.
     - After the choice is made suitable plots appear in a window and leaderboard is printed on the terminal
     - A postgame window appears asking the users if they wish to play again or quit

#Note:
- Start the program using main.sh only
- No command line arguments are required
- Ensure all the dependencies are installed in your system before running the game
- Project uses relative paths, hence it should work on all systems

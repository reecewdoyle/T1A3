from colored import fore, back, attr
from lmpl_functions import (
    print_teams, print_this_round, print_round, team_draw,
    enter_results, edit_results, view_results
)
import pyfiglet as pfg
import csv

# App Logo
text = pfg.print_figlet(text = "Lake Macquarie Premier League", font = "standard", colors = "red")

# App Greeting
print(f"{fore('red')}{back('white')} Welcome to the Lake Macquarie Premier League App for 23/24!{attr('reset')}\n")

file_name = "results.csv"

try:
    # open the file in read mode
    results = open(file_name, "r")
    results.close()
    # print("In try block")
    # if it throws an error, the file doesn't exist
    # if no error, the files exists
except FileNotFoundError:
    # Now, we know the file doesn't exist
    # Create a new file
    results = open(file_name, "w")
    results.write("Game Number,Home Team,Home Goals,Away Team,Away Goals\n")
    results.close()
    # print("In except block")

def create_menu():
    print(f"{fore('blue')} Enter 1 to view THIS YEAR'S TEAMS. {attr('reset')}")
    print(f"{fore('blue')} Enter 2 to view THIS WEEK'S GAMES. {attr('reset')}")
    print(f"{fore('blue')} Enter 3 to view a ROUND. {attr('reset')}")
    print(f"{fore('blue')} Enter 4 to view a TEAM'S DRAW. {attr('reset')}")
    print(f"{fore('blue')} Enter 5 to ENTER the RESULTS from a game.  {attr('reset')}")
    print(f"{fore('blue')} Enter 6 to REMOVE the RESULTS from a game.  {attr('reset')}")
    print(f"{fore('blue')} Enter 7 to VIEW the RESULTS.  {attr('reset')}")
    print(f"{fore('blue')} Enter 8 to exit.\n")
    choice = input(f"{fore('red')} {back('white')} Enter your selection:{attr('reset')}")
    return choice

users_choice = ""

while users_choice != "8":
    users_choice = create_menu()
    print(users_choice)
    if (users_choice == "1"):
        print_teams()
    elif (users_choice == "2"):
        print_this_round()
    elif (users_choice == "3"):
        print_round()
    elif (users_choice == "4"):
        team_draw()
    elif (users_choice == "5"):
        enter_results(file_name)
    elif (users_choice == "6"):
        edit_results()
    elif (users_choice == "7"):
        view_results()
    elif (users_choice == "8"):
        continue
    else:
        print("Invalid Input")

# App Fareweall and Logo
print(f"{fore('red')} {back('white')} Thank you for using the Lake Macquarie Premier League App!{attr('reset')}")
text = pfg.print_figlet(text = "Thank You !\n\nL . M . P . L", font = "standard", colors = "red")
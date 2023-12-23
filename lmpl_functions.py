import re
import csv
import datetime
from colored import fore, back, attr
from prettytable import from_csv

file_name = "results.csv"
teams = [
    f"{fore('white')}{back('red')}Belmont Bandits{attr('reset')}", 
    f"{fore('white')}{back('blue')}Boolaroo Bulldogs{attr('reset')}", 
    f"{fore('white')}{back('yellow')}Charlestown Cobras{attr('reset')}", 
    f"{fore('white')}{back('131')}Eleebana Eagles{attr('reset')}", 
    f"{fore('white')}{back('56')}Glendale Guardians{attr('reset')}", 
    f"{fore('white')}{back('172')}Speers Point Spartans{attr('reset')}", 
    f"{fore('white')}{back('22')}Swansea Silverbacks{attr('reset')}", 
    f"{fore('white')}{back('13')}Warners Bay Wanderers{attr('reset')}"
]

team_mascots = [
    f"{fore('white')}{back('red')}Bandits{attr('reset')}", 
    f"{fore('white')}{back('blue')}Bulldogs{attr('reset')}", 
    f"{fore('white')}{back('yellow')}Cobras{attr('reset')}", 
    f"{fore('white')}{back('131')}Eagles{attr('reset')}", 
    f"{fore('white')}{back('56')}Guardians{attr('reset')}", 
    f"{fore('white')}{back('172')}Spartans{attr('reset')}", 
    f"{fore('white')}{back('22')}Silverbacks{attr('reset')}", 
    f"{fore('white')}{back('13')}Wanderers{attr('reset')}"
]

# 1. - THIS YEAR'S TEAMS

# Print out the list of teams particiapting in the competition this year.

def print_teams():
    print("\nCongratulations to the following teams who've won selection "
      "in the Lake Macquarie Premier League for the 23/24 season: \n")

    print(*teams, sep="\n")
    print("\n")

# 2 - THIS WEEK'S GAMES

# This function uses the datetime package to determine the week of the year
# at the current date. If the date is accessed outside of the season, it
# throws an exception of "No Games this week".

    
def print_this_round():
    from datetime import date
    # Show actual date
    my_date = datetime.date.today()
    print(my_date)
    # Using isocalendar() function
    year, week_num, day_of_week = my_date.isocalendar()
    print("Week #" + str(week_num))
    print("This week's games are: ")
    with open("lmpl.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == str(week_num):
                print("\n" "Round " + row[1] + "," +
                    " " + "Game" + " " + row[2] + "," +
                    " " + row[3] + " " + "vs" + " " +
                    row[4] + " " + row[5] + "," +
                    " " + row[6] + "," + " " + row[7])
                print("\n")
            if week_num in range(6, 43):
                print("No Games this week.")

# 3.  SELECT A ROUND TO VIEW

# This function prints out the results for a particular Round. 
# As it's a 14 Round competition, the user must select a number 
# between 1 and 14. 

def print_round():
    print("There are 14 rounds in the LMPL Competition for this year.\n")
    print("Each team plays each other twice, once at Home, and once Away.\n")
    round_number = 0
    rounds = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"
    ]


    while str(round_number) not in rounds:
        try:
            round_number = int(input("Enter the round (1-14) you'd like to print:\n"))
            if str(round_number) in rounds:
                with open("lmpl.csv", "r") as f:
                    reader = csv.reader(f)
                    round_selected = rounds[round_number - 1]
                    print(f"These are the games in Round {round_selected}\n")
                    for row in reader:
                        try:
                            if row[1] == round_selected:
                                print(f"Round {row[1]}, Game {row[2]}, {row[3]} vs {row[4]}, "
                                      f"{row[5]}, {row[6]}, {row[7]}")

                                print("\n")
                        except IndexError:
                            print("Invalid CSV structure. Check your CSV file format.")
                            break
        except ValueError:
            print("Invalid input! Must be a number between 1 and 14")

# 4 TEAM'S DRAW

# Ask for name of the team
# Print out only the row that features a match with the team name. Should always be 14 games total.
# Game data should include Round, Home Team, Away Team, Game Number, Field, Time, Date, Day of the week.

def team_draw():
    for _index, team  in enumerate(teams):
        print(f"{_index + 1}. {team}")

    team_selection = 0
    teams_menu = ["Belmont Bandits", 
                  "Boolaroo Bulldogs", 
                  "Charlestown Cobras", 
                  "Eleebana Eagles", 
                  "Glendale Guardians", 
                  "Speers Point Spartans", 
                  "Swansea Silverbacks", 
                  "Warners Bay Wanderers"]
    while team_selection not in teams_menu:
        try:
            with open("lmpl.csv", "r") as f:
                reader = csv.reader(f)
                team_selection = int(input("Team Number: "))
                if(team_selection not in range(1,9)):
                    raise ValueError
                team_draw = teams_menu[((team_selection) - 1)]
                print("This is the" + " " + team_draw + " " + "draw for this season.")
                for row in reader:
                        if row[3] == team_draw or row[4] == team_draw:
                            print(f"Round {row[1]}, {row[3]} vs {row[4]}, {row[5]}, {row[6]}, {row[7]}\n")
               
                team_selection = teams_menu[team_selection]

        except ValueError:
            print("Must be a number between 1 and 8 which corresponds to the team.")
                  
        # except: ValueError,print("Must be a number between 1 and 8 which corresponds to to the team.")

# 5 - ENTER RESULTS

# This function asks the user to enter some data to put into the CSV file. 
# It shows the table from the view results function, so you can see what's already been entered. 
# The user enters the Game Number, Home Team Mascot, Home Team Goals, Away Team Mascot, and Away Team Goals.
# The row of the CSV file is then viewable in Function 7.
   
def enter_results(file_name):
    view_results()

    print("\nLet's enter the results of a game!")
    print("\nFirst, we need the Unique Game Number. It will be a number from 1 to 56 and can only be used once.")
    print("\nNOTE: Don't enter a game number that has already been used in the table above.\n")
    with open(file_name, "a") as f:
        game_number = int
        while game_number != 0:
            try:
                game_number = int(input("Enter the Game Number. (enter 0 to return to the main menu): "))
                if game_number not in range(1, 57):
                    print("Must be a number between 1 and 56")
                else:
                    break
            except ValueError:
                print("Must be a number between 1 and 56")

        if game_number != 0:
            print("\nNow we need to enter the MASCOT of the HOME TEAM")
            print("Type the name of the MASCOT out, just as you see it below.")
            print("NO SPACES, NUMBERS, or SPECIAL CHARACTERS")
            print_team_mascots()
            home_team_name = True
            while home_team_name:
                home_team = input("\nEnter the Home Team:\n")
                invalid_name = re.search("[^A-Za-z]+", home_team)

                if invalid_name:
                    print("No special characters will be accepted.")
                elif not home_team:
                    print("You must type something in!")
                else:
                    print("\nAccepted.\n")
                    home_team = home_team.lower()
                    home_team = home_team.title()
                    n = False
                    break

            home_goals = 0
            while True:
                try:
                    home_goals = int(input("Enter the Home Goals: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

        if game_number != 0:
            away_team_name = True
            print("\nGreat! Now onto the AWAY TEAM\n")
            print("Enter the MASCOT of the AWAY TEAM")
            print("Type the name of the MASCOT out, just as you see it below.")
            print("NO SPACES, NUMBERS, or SPECIAL CHARACTERS")
            print_team_mascots()
            while away_team_name:
                away_team = input("\nEnter the Away Team:\n")
                invalid_name = re.search("[^A-Za-z]+", away_team)

                if invalid_name:
                    print("No special characters will be accepted.")
                elif not away_team:
                    print("You must type something in!")
                else:
                    print("\nAccepted.\n")
                    away_team = away_team.lower()
                    away_team = away_team.title()
                    n = False
                    break

            away_goals = 0
            while True:
                try:
                    away_goals = int(input("Enter the Away Goals: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            writer = csv.writer(f)
            writer.writerow([game_number, home_team, home_goals, away_team, away_goals])
            print("\nThank you! You can check your entry with option 7 on the main menu.\n")

def print_team_mascots():
    for mascot in team_mascots:
        print(mascot)

# 6 REMOVE RESULTS

# This function allows the user to remove any rows from the CSV that might have been entered incorrectly.
# It copy all the contents of the csv into a new csv with the same name.
# You specify the game number that corresponds to the row you want to remove, so it leaves that row out of the copy.

def edit_results():
    game_results = ""
    removed_result = ""

    while game_results != "0":
        view_results()
        print("Remove results")

        try:
            games_list = []

            game_results = input("Enter the GAME NUMBER for the RESULTS you want to REMOVE "
                     "(enter 0 to return to the main menu): ")

            if not game_results.isdigit():
                raise ValueError
        except ValueError:
            print("Must be a number")

        try:
            current_game_numbers = []    
            with open(file_name, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    current_game_numbers.append(row[0])
                    if game_results != row[0]:
                        games_list.append(row)
                    else:
                        removed_result = row[0]

            with open(file_name, "w") as f:
                writer = csv.writer(f)
                writer.writerows(games_list)

            if game_results not in current_game_numbers and game_results != "0":
                raise UnboundLocalError

        except UnboundLocalError:
            print("Must be a number that corresponds with the Game Number "
                  "for the Game you want to delete.")


# 7 VIEW RESULTS

# Prints the results in a nice table 

def view_results():
    print("Here are the results from the season so far")
    with open("results.csv") as f:
        table = from_csv(f)
    print(table)   

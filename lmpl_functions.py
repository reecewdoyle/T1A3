import csv
import datetime
from colored import fore, back, attr
from prettytable import from_csv
file_name = "results.csv"
teams = [f"{fore('white')}{back('red')}Belmont Bandits{attr('reset')}", 
         f"{fore('white')}{back('blue')}Boolaroo Bulldogs{attr('reset')}", 
         f"{fore('white')}{back('yellow')}Charlestown Cobras{attr('reset')}", 
         f"{fore('white')}{back('131')}Eleebana Eagles{attr('reset')}", 
         f"{fore('white')}{back('56')}Glendale Guardians{attr('reset')}", 
         f"{fore('white')}{back('172')}Speers Point Spartans{attr('reset')}", 
         f"{fore('white')}{back('22')}Swansea Silverbacks{attr('reset')}", 
         f"{fore('white')}{back('13')}Warners Bay Wanderers{attr('reset')}"]

# ************************************************************************************************************************************************************************************************
# 1. - THIS YEAR'S TEAMS
# ************************************************************************************************************************************************************************************************

# Print out the list of teams particiapting in the competition this year.

def print_teams():
    print("\n""Congratulations to the following teams who've won selection in the Lake Macquarie Premier League for the 23/24 season: \n")
    print(*teams, sep="\n")
    print("\n")

# ************************************************************************************************************************************************************************************************
# 2 - THIS WEEK'S GAMES
# ************************************************************************************************************************************************************************************************

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
                print("\n" "Round " + row[1] + "," + " " + "Game" + " " + row[2] + "," + " " + row[3] + " " + "vs" + " " + row[4] + " " + row[5] + "," + " " + row[6] + "," + " " + row[7])
                print("\n")
            if week_num in range(6, 43):
                print("No Games this week.")

# Use a date and time extension to tell what date it is on the day the user is accessing the app.
# Have the games for the rounds in a seperate csv file
# Print only the games for the round this week

# ************************************************************************************************************************************************************************************************
# 3.  SELECT A ROUND TO VIEW
# ************************************************************************************************************************************************************************************************

def print_round():
    print("There are 14 rounds in the LMPL Competition for this year. ""\n")
    print("Each team plays each other twice, once at Home, and once Away. ""\n")
    round = 0
    rounds = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    while str(round) not in rounds:
        try:   
            round = int(input("Enter the round (1-14) you'd like to print: ""\n"))
            if (round in rounds):
                with open("lmpl.csv", "r") as f:
                    reader = csv.reader(f)
                    round_selected = rounds[((round) - 1)]
                    print(f"These are the games is Round {round_selected} \n")
                    for row in reader:                  
                        if row[1] == round_selected:
                                print( "Round " + row[1] + "," + " " + "Game" + " " + row[2] + "," + " " + row[3] + " " + "vs" + " " + row[4] + " " + row[5] + "," + " " + row[6] + "," + " " + row[7])
                                print("\n")
        except IndexError:
            print("Must be a number between 1 and 14")
        except ValueError:
            print("No text! Must be a number between 1 and 14")

# ************************************************************************************************************************************************************************************************
# 4 TEAM'S DRAW
# ************************************************************************************************************************************************************************************************


def team_draw():
    for _index, team  in enumerate(teams):
        print(f"{_index + 1}. {team}")

    team_selection = 0
    teams_menu = ["Belmont Bandits", "Boolaroo Bulldogs", "Charlestown Cobras", "Eleebana Eagles", "Glendale Guardians", "Speers Point Spartans", "Swansea Silverbacks", "Warners Bay Wanderers"]
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
                        if row[3] == team_draw:    
                            print("Round " + row[1] + ","" " +row[3] + " " + "vs" + " " + row[4] + "," + " " + row[5] + "," + " " + row[6] + "," + " " + row[7] + "\n")
                        elif row[4] == team_draw:
                            print("Round " + row[1] + ","" " +row[3] + " " + "vs" + " " + row[4] + "," + " " + row[5] + "," + " " + row[6] + "," + " " + row[7] + "\n")
                
                team_selection = teams_menu[team_selection]
                            
        except: ValueError,print("Must be a number between 1 and 8 which corresponds to to the team.")



# Ask for name of the team
# Print out only the row that features a match with the team name. Should always be 14 games total.
# Game data should include Round, Home Team, Away Team, Game Number, Field, Time, Date, Day of the week.

# ************************************************************************************************************************************************************************************************
# 5 - ENTER RESULTS
# ************************************************************************************************************************************************************************************************


def enter_results(file_name):
    view_results()

    print("Let's enter the results of a game!")
    with open(file_name, "a") as f:
        game_number = int
        while((game_number != 0)):
            try:    
                game_number =  int(input("Enter the Game Number(enter 0 to return to main menu): "))
                if game_number not in range(1,57):
                    print("Must be a number between 1 and 56")
                else:
                    break
            except ValueError:
                print("Must be a number between 1 and 56")

        if(game_number != 0):
            print("Type the name of the Home Team as you see it below.")
            for team in teams:
                print(f"{team}")
            home_team = input("\nEnter the Home Team: ")
                

            home_goals = 0  
            while True:    
                try:
                    home_goals = int(input("Enter the Home Goals: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                
            print("Type the name of the Away Team as you see it below.")
            for team in teams:
                print(f"{team}")
            away_team = input("\nEnter the Away Team: ")


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
   
   
   

   
   
    # try:
    #     away_team = input("Enter the Away Team: ")
    #     away_goals = 0
    #     away_goals = int(input("Enter the Away Team Goals: "))
    # except: ValueError
    # print("Must be a Number")
   
   
    # try:
    #     home_goals = 0
    #     home_goals = int(input("Enter the Home Team Goals: "))
    #     # raise Exception("Please enter numbers only")
    # except: ValueError, print("Must be a Number")
   
   
    # except Exception:
    #     print("Something went wrong. Please try again")

    # Ask for game number
        # game_round = int(input("Enter the Round of the game:"))
        # game_number = 0
        # while 1 > game_number or 56 < game_number:
        #     try:
        #         game_number = int(input("Please enter your game number (1 - 56) : "))
        #     except ValueError:
        #         print("Must be a number between 1 and 56")


        # try:
        #     game_number = 0
        #     while 1 > game_number or 56 < game_number:
        #         game_number = int(input("Please enter your game number (1 - 56) : "))

        # except ValueError:
        #     print("Must be a number between 1 and 56")

# ************************************************************************************************************************************************************************************************
# 6 REMOVE RESULTS
# ************************************************************************************************************************************************************************************************

# def edit_results():
#     print("Remove results")
#     game_results = input("Enter the GAME NUMBER for the RESULTS you want to REMOVE: ")
#     # copy all the conents of the csv into a new csv
#     # while doing this, we constantly check for the condition
#     # when we encounter the game results to be removed, we don't copy that one
#     # the final game result with be written in the csv file
#     games_list =[]
#     with open(file_name, "r") as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if game_results != row[0]:
#                 games_list.append(row)
#     with open(file_name, "w") as f:
#         writer = csv.writer(f)
#         writer.writerows(games_list)
         
def edit_results():
    game_results = ""
    removed_result = ""
    while(game_results != "0"):
        view_results()
        print("Remove results")
        try:
            games_list = []

            game_results = input("Enter the GAME NUMBER for the RESULTS you want to REMOVE(enter 0 to return to main menu): ")
            if(not game_results.isdigit()):
                raise ValueError
        except ValueError:
            print("Must be a number")
            # copy all the contents of the csv into a new csv
            # while doing this, we constantly check for the condition
            # when we encounter the game results to be removed, we don't copy that one
            # the final game result with be written in the csv file
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
            if(game_results not in current_game_numbers and game_results != "0"):
                raise UnboundLocalError
        except UnboundLocalError:
            print("Must be a number that corresponds with the Game Number for the Game you want to delete.")


# ************************************************************************************************************************************************************************************************
# 7 VIEW RESULTS
# ************************************************************************************************************************************************************************************************

def view_results():
    print("Here are the results from the season so far")
    with open("results.csv") as f:
        table = from_csv(f)
    print(table)   
    
    
    # from prettytable import from_csv
    # with open("results.csv") as f:
    #     mytable = from_csv(f)
    # print(mytable)
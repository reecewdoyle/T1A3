import csv
import datetime
from colored import fore, back, attr
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
    print("\n""Congratulations to the following teams who've won selection in the Lake Macquiare Premier Leauge for the 23/24 season: \n")
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

    # try:

def print_round():
    print("There are 14 rounds in the LMPL Competition for this year. ""\n")
    print("Each team plays each other twice, once and Home, and once Away. ""\n")
    
    with open("lmpl.csv", "r") as f:
            reader = csv.reader(f)
            round = int(input("Enter the round (1-14) you'd like to print: ""\n"))
            rounds = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
            round_selected = rounds[((round) - 1)]
            print(f"These are the games is Round {round_selected} \n")

            for row in reader:                  
                if row[1] == round_selected:
                        print( "Round " + row[1] + "," + " " + "Game" + " " + row[2] + "," + " " + row[3] + " " + "vs" + " " + row[4] + " " + row[5] + "," + " " + row[6] + "," + " " + row[7])
                        print("\n")













        # with open("lmpl.csv", "r") as f:
        #     reader = csv.reader(f)
        #     round = input("Enter the round (1-14) you'd like to print: ""\n")
        #     print(f"These are the games is Round {round} \n")
        #     for row in reader:                  
        #         if row[1] == round:
        #                 print( "Round " + row[1] + "," + " " + "Game" + " " + row[2] + "," + " " + row[3] + " " + "vs" + " " + row[4] + " " + row[5] + "," + " " + row[6] + "," + " " + row[7])
        #                 print("\n")


    # except:
            # else:
            #     print("Invalid Input")




                    # if row[8] == True:
                    # print(row[9] + " " + "-" + " " + row[10])
                    # if row[9] > row[10]:
                    #     print("\n" + row[3] + " " + "Win!" "\n")
                    # elif row[9] < row[10]:
                    #     print("\n" + row[4] + " " "Win!" "\n")
                    # elif row[9] == row[10]:
                    #         print("\n" "Draw" "\n")
                    # if row[8] == False:                        print("Game hasn't been played yet")

                    # print("\n" "Round " + row[1] + "," + " " + "Game" + " " + row[2] + "," + " " + row[3] + " " + "vs" + " " + row[4] + " " + row[5] + "," + " " + row[6] + "," + " " + row[7] + " " + row[9] + " " + "-" + " " + row[10])
# Enter the round (1-14) you'd like to see the results or fixtures for.
# Print the results and fixtures. 

# ************************************************************************************************************************************************************************************************
# 4
# ************************************************************************************************************************************************************************************************


def team_draw():
    print(f"1. {teams[0]}")
    print(f"2. {teams[1]}")
    print(f"3. {teams[2]}")
    print(f"4. {teams[3]}")
    print(f"5. {teams[4]}")
    print(f"6. {teams[5]}")
    print(f"7. {teams[6]}")
    print(f"8. {teams[7]}")

    with open("lmpl.csv", "r") as f:
        reader = csv.reader(f)
        team = int(input("Team Numner: "))
        teams_menu = ["Belmont Bandits", "Boolaroo Bulldogs", "Charlestown Cobras", "Eleebana Eagles", "Glendale Guardians", "Speers Point Spartans", "Swansea Silverbacks", "Warners Bay Wanderers"]
        team_draw = teams_menu[((team) - 1)]
        print("\n")
        print("This is the" + " " + team_draw + " " + "draw for this season.")
        print("\n")

        for row in reader:
                if row[3] == team_draw:    
                    print("Round " + row[1] + ","" " +row[3] + " " + "vs" + " " + row[4] + "," + " " + row[5] + "," + " " + row[6] + "," + " " + row[7] + "\n")
                elif row[4] == team_draw:
                    print("Round " + row[1] + ","" " +row[3] + " " + "vs" + " " + row[4] + "," + " " + row[5] + "," + " " + row[6] + "," + " " + row[7] + "\n")
        print("\n")
        # else:
        #     print("Invalid Input")


    # print("Team draw view")
# Ask for name of the team
# Print out only the row that features a match with the team name. Should always be 14 games total.
# Game data should include Round, Home Team, Away Team, Game Number, Field, Time, Date, Day of the week.

# file_name = "results.csv"

# ************************************************************************************************************************************************************************************************
# 5
# ************************************************************************************************************************************************************************************************


def enter_results(file_name):
    print("game results")
    with open(file_name, "a") as f:
    # Ask for game number
        # game_round = int(input("Enter the Round of the game:"))
        game_number =  int(input("Enter the Game Number: "))
        print(f"1. {teams[0]}")
        print(f"2. {teams[1]}")
        print(f"3. {teams[2]}")
        print(f"4. {teams[3]}")
        print(f"5. {teams[4]}")
        print(f"6. {teams[5]}")
        print(f"7. {teams[6]}")
        print(f"8. {teams[7]}")
        home_team = input("\nEnter the Home Team: ")
        home_goals = int(input("Enter the Home Team Goals: "))
        away_team = input("Enter the Away Team: ")
        away_goals = int(input("Enter the Away Team Goals: "))
        writer = csv.writer(f)
        writer.writerow([game_number, home_team, home_goals, away_team, away_goals])

# ************************************************************************************************************************************************************************************************
# 6
# ************************************************************************************************************************************************************************************************


         
def edit_results(file_name):
    print("Remove results")
    game_results = input("Enter the GAME NUMBER for the RESULTS you want to REMOVE: ")
    # copy all the conents of the csv into a new csv
    # while doing this, we constantly check for the condition
    # when we encounter the game results to be removed, we don't copy that one
    # the final game result with be written in the csv file
    games_list =[]
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if game_results != row[0]:
                games_list.append(row)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(games_list)


# ************************************************************************************************************************************************************************************************
# 7
# ************************************************************************************************************************************************************************************************

def view_results(file_name):
    print("Here are the results from the season so far")
    from prettytable import from_csv
    with open("results.csv") as f:
        table = from_csv(f)
    print(table)   
    


    # with open(file_name, "r") as f:
    #     reader = csv.reader(f)
    #     reader.__next__()
    #     for row in reader:
    #         print(*row)
    
    
    
    
    # from prettytable import from_csv
    # with open("results.csv") as f:
    #     mytable = from_csv(f)
    # print(mytable)
import csv



def print_teams():
    teams = ["\n" "Belmont Bandits", "Boolaroo Bulldogs", "Charlestown Cobras", "Eleebana Eagles", "Glendale Guardians", "Speers Point Spartans", "Swansea Silverbacks", "Warners Bay Wanderers" "\n"]
    print("\n""Congratulations to the following teams who've won selection in the Lake Macquiare Premier Leauge for the 23/24 season: ")
    print(*teams, sep="\n")
# Print out the list of teams particiapting in the competition this year.

def print_this_round():
    print("Print this round")
    
# Use a date and time extension to tell what date it is on the day the user is accessing the app.
# Have the games for the rounds in a seperate csv file
# Print only the games for the round this week
    
def print_round():

    with open("lmpl.csv", "r") as f:
        reader = csv.reader(f)
        round = input("Enter the round (1-14) you'd like to print: ""\n")
        for row in reader:
            if row[1] == round:    
                print("Round " + row[1] + ","" " +row[2] + " " + "vs" + " " + row[3])
                print("\n")
# Enter the round (1-14) you'd like to see the results or fixtures for.
# Print the results and fixtures. 



def team_draw():
    print("1. Belmont Bandits")
    print("2. Boolaroo Bulldogs")
    print("3. Charlestown Cobras")
    print("4. Eleebana Eagles")
    print("5. Glendale Guardians")
    print("6. Speers Point Spartans")
    print("7. Swansea Silverbacks")
    print("8. Warners Bay Wanderers")

    with open("lmpl.csv", "r") as f:
        reader = csv.reader(f)
        team = int(input("Team Numner: "))
        teams_menu= ["Belmont Bandits", "Boolaroo Bulldogs", "Charlestown Cobras", "Eleebana Eagles", "Glendale Guardians", "Speers Point Spartans", "Swansea Silverbacks", "Warners Bay Wanderers"]
        team_draw = teams_menu[((team) - 1)]
        for row in reader:
                if row[2] == team_draw:    
                    print("Round " + row[1] + ","" " +row[2] + " " + "vs" + " " + row[3])
                elif row[3] == team_draw:
                    print("Round " + row[1] + ","" " +row[2] + " " + "vs" + " " + row[3])

        # else:
        #     print("Invalid Input")


    # print("Team draw view")
# Ask for name of the team
# Print out only the row that features a match with the team name. Should always be 14 games total.
# Game data should include Round, Home Team, Away Team, Game Number, Field, Time, Date, Day of the week.

def game_results():
    print("Enter game results")
# Enter game number.
# Enter Home Team
# Enter Away Goals


# def select_team_draw():
#     print("Enter the number that corresponds to the team you'd like to see the season draw for.")
#     print("1. Belmont Bandits")
#     print("2. Boolaroo Bulldogs")
#     print("3. Charlestown Cobras")
#     print("4. Eleebana Eagles")
#     print("5. Glendale Guardians")
#     print("6. Speers Point Spartans")
#     print("7. Swansea Silverbacks")
#     print("8. Warners Bay Wanderers")


        # team_menu = int(input("Enter the number that corresponds to the team to see their draw: ""\n"))
        # if team_menu == "1":
        #     team_draw = input("Belmont Bandits")
        # elif team_menu == "2":
        #     team_draw = input("Boolaroo Bulldogs")
        # elif team_menu == "3":
        #     team_draw = input("Charlestown Cobras")
        # elif team_menu == "4":
        #     team_draw = input("Charlestown Cobras")
        # elif team_menu == "5":
        #     team_draw = input("Charlestown Cobras")
        # elif team_menu == "6":
        #     team_draw = input("Charlestown Cobras")
        # elif team_menu == "7":
        #     team_draw = input("Charlestown Cobras")
        # elif team_menu == "8":
        #     team_draw = input("Charlestown Cobras")    
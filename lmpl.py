from colored import fore, back, attr
from lmpl_functions import print_teams, print_this_round, print_round, team_draw, game_results
import pyfiglet

# App Greeting


# logo = pyfiglet.figlet_format(text = "Lake Macquarie Premier League", font = "standard", color = "red")
text = pyfiglet.print_figlet(text = "Lake Macquarie Premier League", font = "standard", colors = "red")
# print(logo)

print(f"{fore('red')} {back('white')} Welcome to the Lake Macquarie Premier League App for 23/24!{attr('reset')}")

def create_menu():
    print(f"{fore('blue')}Enter 1 to view THIS YEAR'S TEAMS. {attr('reset')}")
    print(f"{fore('blue')}Enter 2 to view THIS WEEK'S GAMES. {attr('reset')}")
    print(f"{fore('blue')}Enter 3 to view a ROUND. {attr('reset')}")
    print(f"{fore('blue')}Enter 4 to view a TEAM'S DRAW. {attr('reset')}")
    print(f"{fore('blue')}Enter 5 to ENTER the RESULTS from a game.  {attr('reset')}")
    print(f"{fore('blue')}Enter 6 to exit.")
    print("\n")
    choice = input(f"{fore('red')} {back('white')}Enter your selection:{attr('reset')}")
    return choice

users_choice = ""

while users_choice != "6":
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
        game_results()
    elif (users_choice == "6"):
        continue
    else:
        print("Invalid Input")

print(f"{fore('red')} {back('white')} Thank you for using the Lake Macquarie Premier League App!{attr('reset')}")


# 1. Print fixture this round.
            # Game number, Home Team, Away Team, Oval, Time, Day, Date,
            # Game number, Home Team, Away Team, Oval, Time, Day, Date,
            # Game number, Home Team, Away Team, Oval, Time, Day, Date,
            # Game number, Home Team, Away Team, Oval, Time, Day, Date,
# 2. Print fixture for the following rounds:
    # 1. Round 1
            # Game number, Home Team, Away Team, Oval, Time, Day, Date,
            # Game number, Home Team, Away Team, Oval, Time, Day, Date,
            # Game number, Home Team, Away Team, Oval, Time, Day, Date,
            # Game number, Home Team, Away Team, Oval, Time, Day, Date,
    # 2. Round 2
    # 3. Round 3
    # 4. Round 4
    # 5. Round 5       
    # 6. Round 6
    # 7. Round 7
    # 8. Round 8
    # 9. Round 9
    # 10. Round 10
    # 11. Round 11
    # 12. Round 12
    # 13. Round 13
    # 14. Round 14

# 3. Print fixture for a team
    # 1. Belmont Bandits
    # 2. Boolaroo Bulldogs
    # 3. Charlestown Cobras
    # 4. Eleebana Eagles
    # 5. Glendale Guardians
    # 6. Speers Point Spartans
    # 7. Swansea Silverbacks
    # 8. Warners Bay Wanderers

# 4. Print League Table

# 5. Enter Results
    # 1. Game number
        # Home Team Goals
        # Away Team Goals
        
# Lake Macquarie Premier League App

# App Greeting
print("Welcome to the Lake Macquarie Premier League App for 23/24!")


def create_menu():
    print("1. Enter 1 to print the fixture for this week's round. ")
    print("2. Enter 2 to print the fixture and results for a particular round. ")
    print("3. Enter 3 to print the fixture for a specific team. ")
    print("4. Enter 4 to enter the results from a game.  ")
    print("5. Enter 5 to exit.")
    choice = input(" Enter your selection: ")
    return choice

users_choice = ""

while users_choice != "5":
    users_choice = create_menu()
    print(users_choice)
    if (users_choice == "1"):
        print("You entered 1")
    elif (users_choice == "2"):
        print("You entered 2")
    elif (users_choice == "3"):
        print("You entered 3")
    elif (users_choice == "4"):
        print("You entered 4")
    elif (users_choice == "5"):
        continue
    else:
        print("Invalid Input")

print("Thank you for using the Lake Macquarie Premier League App!")


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
        

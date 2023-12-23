import csv
import datetime

def print_this_round():
    # from datetime import date
    # # Show actual date
    # my_date = datetime.date.today()
    # print(my_date)
    # # Using isocalendar() function
    # year, week_num, day_of_week = my_date.isocalendar()
    # print("Week #" + str(week_num))
    # print("This week's games are: ")
    
    week_num = week_num_to_test

    found_games = False  # Variable to track if any games are found
    
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
                found_games = True  # Set to True if at least one game is found

    if not found_games and week_num in range(6, 43):
        print("No Games this week.")

# Test the function with a specific week_num value
week_num_to_test = 10  # Change this to the desired week number
print_this_round()

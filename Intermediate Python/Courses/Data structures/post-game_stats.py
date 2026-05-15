'''
Imagine you have a dataset with information about your favorite sports team. 🏀🎾⚽ The goal is to use Python's data structures to organize and analyze this data.

If you can't think of any, feel free to use the Super Bowl 2024 champions, the Kansas City Chiefs. 🏈

As a data analyst for the Kansas City Chiefs you have been given a dataset containing information about the players, their positions, and some game statistics.

Let's start analyzing!
    Create a list of dictionaries where each dictionary represents a player. Include attributes such as 'name,' 'position,' and 'jersey number.'
    Print out a list of all player positions in the dataset.
    Choose a player and update their game statistics in the dataset.
    Calculate the average statistics (e.g., yards gained, touchdowns) for all players and print the results.
'''
# Write code below 💖

# Task 1: Create Player Data
players_data = [
  {"name": "Patrick Mahomes", "position": "Quarterback", "jersey_number": 15, "yards_gained": 400, "touchdowns": 3},
  {"name": "Tyreek Hill", "position": "Wide Receiver", "jersey_number": 10, "yards_gained": 150, "touchdowns": 2},
]

names = [player["name"] for player in players_data]
print("Players Names:", names)

# Task 2: Analyze Player Positions
positions = [player["position"] for player in players_data]
print("Player Positions:", positions)

# Task 3: Update Player Statistics
players_data[0]["yards_gained"] += 50
players_data[0]["touchdowns"] += 1

# Task 4: Calculate Average Stats
average_yards = sum(player["yards_gained"] for player in players_data) / len(players_data)
average_touchdowns = sum(player["touchdowns"] for player in players_data) / len(players_data)
print("Average Yards Gained:", average_yards)
print("Average Touchdowns:", average_touchdowns)
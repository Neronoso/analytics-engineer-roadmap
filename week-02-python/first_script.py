# Task 1:
# Goal: Write a script that stores a list of 5 analytics tools you want to learn
#, then prints each one on a separate line with a number in front.

# list1 = ['SQL', 'Python', 'dbt', 'Git', 'Airflow']

# for i, x in enumerate(list1, start=1):
#     print(f"{i}. {x}")

# Task 2:
# Goal: Write a script that stores your tools as a dictionary where the key is the tool name 
# and the value is your current skill level. Then write a function that prints each tool and level.

# Note:
# I need to use items() to unpack the dictionary

# dict1 = {   'SQL':'Advanced'
#          ,  'Python': 'Beginner'
#          ,  'dbt': 'No experience'
#          ,  'Git': 'Beginner'
#          ,  'Airflow': 'No experience'
#          }
# def print_skills(var):
#     for i, x in var.items():
#         print(f"{i} - {x}")

# print_skills(dict1)
#Task 3:
#Goal: Write a script that:
# Creates a list of dictionaries — each one representing a player with name, country, and total_bets
# Prints only the players who have more than 100 bets

players = [
    {'name': 'Alex', 'country': 'UA', 'total_bets': 250},
    {'name': 'Maria', 'country': 'PL', 'total_bets': 80},
    {'name': 'John', 'country': 'UK', 'total_bets': 310},
    {'name': 'Anna', 'country': 'DE', 'total_bets': 45},
    {'name': 'Ivan', 'country': 'UA', 'total_bets': 175},
]

# for x in players:
#     if x['total_bets'] >= 100:
#         print(f"{x['name']} | {x['country']} | {x['total_bets']} bets")

### Task 4:
# Goal: Write a function called summarize_players that takes the players list and prints:

# Total players: 5
# Active players (>100 bets): 3
# Top player: John (310 bets)

### Old version:
# total_players_list = []
# active_players_list = []
# top_player = {}

# for x in players:
#     if x['name'] not in total_players_list:
#         total_players_list.append(x['name'])
#     if x['name'] not in active_players_list and x['total_bets'] > 100:
#         active_players_list.append(x['name'])

# print(len(active_players_list))

### New version:
def summarize_players(players):
    total_players = len(players)
    active_players = 0
    biggest_bet_dict = max(players, key = lambda players: players['total_bets'])
    biggest_bet_player = biggest_bet_dict['name']
    biggest_bet_num = biggest_bet_dict['total_bets']

    for x in players:
        if x['total_bets'] > 100:
            active_players += 1
    print(f"Total players: {total_players} \nActive players (>100 bets): {active_players}\nTop player: {biggest_bet_player} ({biggest_bet_num} bets)")


summarize_players(players)
        

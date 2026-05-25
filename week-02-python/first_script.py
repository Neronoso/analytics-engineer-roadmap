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

for x in players:
    if x['total_bets'] >= 100:
        print(f"{x['name']} | {x['country']} | {x['total_bets']} bets")

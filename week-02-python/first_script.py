# Task 1:
# Goal: Write a script that stores a list of 5 analytics tools you want to learn
#, then prints each one on a separate line with a number in front.

# list1 = ['SQL', 'Python', 'dbt', 'Git', 'Airflow']

# for i, x in enumerate(list1, start=1):
#     print(f"{i}. {x}")

# Task 2:
# Goal: Write a script that stores your tools as a dictionary where the key is the tool name 
# and the value is your current skill level. Then write a function that prints each tool and level.
# dict1 = {   'SQL':'Advanced'
#          ,  'Python': 'Beginner'
#          ,  'dbt': 'No experience'
#          ,  'Git': 'Beginner'
#          ,  'Airflow': 'No experience'
#          }

# for i, x in dict1.items():
#     print(f"{i} - {x}")
# Note:
# I need to use items() to unpack the dictionary

dict1 = {   'SQL':'Advanced'
         ,  'Python': 'Beginner'
         ,  'dbt': 'No experience'
         ,  'Git': 'Beginner'
         ,  'Airflow': 'No experience'
         }
def print_skills(var):
    for i, x in var.items():
        print(f"{i} - {x}")

print_skills(dict1)

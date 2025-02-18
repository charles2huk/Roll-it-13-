import random

# Intialise rounds points
user_points = 0
comp_points = 0
double_user = "no"


# Roll the dice for the user and note if they got a double
user_one = random.randint(1, 6)
user_two = random.randint(1, 6)
if user_one == user_two:
    double_user = "yes"

# roll the dice for the computer
comp_one = random.randint(1, 6)
comp_two = random.randint(1, 6)

# update the user / computer points
user_points += user_one + user_two
comp_points += comp_one + comp_two

# Output the results

print("\nIntial Points")
print(f"user    - Roll 1: {user_one} \t| Roll 2 {user_two} \t| Total: {user_points} ")
print(f"Computer    - Roll 1: {comp_one} \t| Roll 2 {comp_two} \t| Total: {comp_points} ")

# Let the user know if they qualify for double points
if double_user == "yes":
    print("Great news - if you win, you will earn double points")

import random
from logo_higher_lower_game import logo , vs
from game_data import data
import sys
sys.path.append("C:\VScode_workspace\python_vscode")
from clear import clear
clear()
print(logo)


random_data1 = random.choice(data)
random_data2 = random.choice(data)
print(f"Compare A: {random_data1['name']}, a {random_data1['description']}, from {random_data1['country']}")
print(vs)
print(f"Against B: {random_data2['name']}, a {random_data2['description']}, from {random_data2['country']}")

names_list=[]
names_list.append(random_data1["name"])
names_list.append(random_data2["name"])
score=0
end = False
def compare(a,b,guess):
    global end
    global score
    if guess == 'a' and (a['follower_count']>b['follower_count']):
        score += 1
        # clear()
        # print(logo)
        print(f"You're right! Current score: {score}.")
        print()
        names_list.append(a["name"])
        return a
    elif guess == 'b' and b['follower_count']>a['follower_count']:
        score += 1
        # clear()
        # print(logo)
        print(f"You're right! Current score: {score}.")
        print()
        names_list.append(b["name"])
        return b
    else:
        print(f"Sorry, that's wrong. Final Score {score}")
        end = True

guess = input("Who has more followers in Instagram? Type 'A' or 'B': ").lower()
previous_data = compare(random_data1,random_data2,guess)

while end is False:
    random_data_new = random.choice(data)
    print("first   ",random_data_new["name"])
    while random_data_new["name"] in names_list:
        random_data_new = random.choice(data)
    print(f"Compare A: {previous_data['name']}, a {previous_data['description']}, from {previous_data['country']}")
    print(vs)
    print(f"Against B: {random_data_new['name']}, a {random_data_new['description']}, from {random_data_new['country']}")

    guess = input("Who has more followers in Instagram? Type 'A' or 'B': ").lower()
    previous_data = compare(random_data_new,previous_data,guess)
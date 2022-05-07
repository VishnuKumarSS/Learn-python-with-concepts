# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
sum_name=name1+name2.lower()
count1=0
count2=0
for i in sum_name:
    if i == "t" or i == "r" or i == "u" or i =="e":
        count1+=1
    if i =="l" or i == "o" or i == "v" or i=="e":
        count2+=1
final2=str(count1)+str(count2)
final=int(final2)
if final>=40 and final <=50:
    print(f"Your score is {final2}, you are alright together.")
elif final <10 or final > 90:
    print(f"Your score is {final2},you go together like coke and mentos.")
else:
    print(f"Your score is {final2}.")



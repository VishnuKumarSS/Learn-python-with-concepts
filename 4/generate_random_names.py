# program to generate random name to pay the bill :)

import random
string=input("Enter the names seperated by comma  ")
string_split=string.split(",")
length=len(string_split)
a=random.randint(0,length-1)
if length>1:
    print(f"{string_split[a]} is gonna pay the bill")
else:
    print("Enter some names")

    
#we can also use choice function under the random module to generate random choice of elements

#print(random.choice(string_split))
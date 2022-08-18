import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word= random.choice(word_list)
print(chosen_word)

list1=[]
for i in range(len(chosen_word)):
    list1+="_" #or    list1.append("_")
print(list1)

while "_" in list1:
    guess=input("Enter a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i]==guess:
            list1[i]=guess
    print(list1)
    if "_" not in list1:
        print("You won")
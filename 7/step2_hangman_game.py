import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word= random.choice(word_list)
print(chosen_word)
guess=input("Enter a letter: ").lower()

list1=[]
for i in range(len(chosen_word)):
    list1+="_" #or    list1.append("_")
print(list1)

for i in range(len(chosen_word)):
    if chosen_word[i]==guess:
        list1[i]=guess
print(list1)

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word= random.choice(word_list)
print(chosen_word)

list1=[]
for i in range(len(chosen_word)):
    list1+="_" #or    list1.append("_")
print(list1)

chances=len(stages)-1
while "_" in list1:
    guess=input("Enter a letter: ").lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                list1[i]=guess
        print(list1)
    elif guess not in chosen_word:
        print(stages[chances-1])
        chances-=1
    
    if chances==0:
        print("You Lose")
        break
    if "_" not in list1:
        print("You won")
        break
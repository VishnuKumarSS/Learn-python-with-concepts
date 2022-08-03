dictionary = {
    "name1":"starz",
    "name2":"vishnu",
    3:"sathish",
}
print(dictionary)

# accessing values in a dictionary is archived by using its key as a index.
a=dictionary[3]
b=dictionary["name1"]
print(a)
print(b)

# adding new items to the dictionary
dictionary["name4"]="kumar"
print(dictionary)

# renaming the item in a dictionary
dictionary["name1"]="starzzzz"
print(dictionary)

# deleting dictionary
dictionary={} # here we overwrited the already existing dictionary
print(dictionary)

# creating empty dictionary
dictionary2={}
dictionary3=dict()

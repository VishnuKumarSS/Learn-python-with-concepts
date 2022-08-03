# normal dictionary
dictionary={"name":"starz"}

# nested values
dictionary1={
    "name1":"vishnu",
    "name2":"kumar"
}
print(dictionary1)
# nesting a list in a dictionary
dictionary2={
    "class1":["starz","vishnu","kumar"],
    "class2":["sathish","karthick"]
}
print(dictionary2) # here the class 1 and class 2 are the keys

# nesting dictionary in a dictionary
dictionary3={
    "class1":{
        "names":["starz","vishnu","kumar"],
        "total_names":3},
    "class2":{
        "names":["sathish","karthick"],
        "total_names":2}, # ? here we included comma (",") to add more elements in the dictionary easily
}
print(dictionary3) # here class 1 and class 2 are the keys

# nesting dictionary in a list
dictionary4=[ 
    {
        "ece":"class1",
        "names":["starz","vishnu","kumar"],
        "total_names":3
    },
    {
        "cse":"class2",
        "names":["sathish","karthick"],
        "total_names":2
    },
] # list

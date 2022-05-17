# normal class without constructor

class User:
    pass


print("\nWithout Constructor.\n")
# creating a object called user_1
user_1 = User() 
# creating attributes to that object called user_1
user_1.id = 28
user_1.name= "Starz"
print(user_1.id,user_1.name)

# creating a object called user_2
user_2 = User() 
# creating attributes to that object called user_1
user_2.id=38
user_2.name= "Vishnu"
print(user_2.id,user_2.name)

'''------------------------------------------------------------------------------------------------------------------------------------------------'''
# using
# constructor

class UserDetails:
    def __init__(self,id_no,name): # here the id_no could either be id or id_no....we can use whatever name we want like id_no...

        print("\nconstructor created.")
        self.id = id_no   
        self.name = name
        self.department = "ECE" # here we set the default value for the department attribute, there is no need to pass the argument in the class when we are want to use.


print("\nConstructor with attributes.")
# now we can easily create the objects from the class by the help of constructor.
user1 = UserDetails(28,"Starz") 

user2 = UserDetails(38,"Vishnu")

print(user1.id,user1.name) 
print(user2.id,user2.name,"\n")

print(user1.department,user2.department) # here for both the objects department is same. we set it as ECE by default.


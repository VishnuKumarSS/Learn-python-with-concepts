
class User:
    def __init__(self,user_id, username):
        # attributes 
        self.id = user_id
        self.name = username
        self.following = 0
        self.followers = 0

    # method
    def follow(self, another_user):
        another_user.followers += 1
        self.following += 1
    
# calling the attributes ,just to pass the values
user_1 = User("001","starz")
user_2 = User("002","vishnu")



# calling the methods,
user_1.follow(user_2)  # here user_2 is the another_user that we defined above.
# user_1 acts as self in the above declared method

# printing the method, to know whats going on.
print("user_1 followers: ",user_1.followers)
print("user_1 following: ",user_1.following)

print("user_2 followers: ",user_2.followers)
print("user_2 following: ",user_2.following)
print()


user_1.follow(user_2)
print("user_1 followers: ",user_1.followers)
print("user_1 following: ",user_1.following)

print("user_2 followers: ",user_2.followers)
print("user_2 following: ",user_2.following)
print()


user_2.follow(user_1)
print("user_1 followers: ",user_1.followers)
print("user_1 following: ",user_1.following)

print("user_2 followers: ",user_2.followers)
print("user_2 following: ",user_2.following)
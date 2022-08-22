# class inheritance
#--------------------------------------------------------------

# normal class
class Animal:
    def __init__(self):
        self.eyes = 2
        # .......
    def breathe(self):
        print("Inhale, Exhale")


# # normal class
# class Fish: 
#     def swim(self):
#         print("swimming in water.")


# here the class Fish is going to inherit the Animal class.
class Fish(Animal): 
    def __init__(self):
        super().__init__() # to inherit the everything form the animal class we are using super function
    def swim(self):
        print("swimming in water.")
    # below we are gonna modify the breathe method in the Animal class.
    def breathe(self):
        super().breathe() # adding the extra behaviour to the super class.
        print("breathing in water.")

fish = Fish() # create a fish object with the Fish class

fish.swim()
print()
fish.breathe() # method from the super class Animal
print()
print(fish.eyes) # this is the attribute from the super class Animal
print()
# below we are printing the values of Animal class without the inheritance
ani = Animal()
ani.breathe()


# class Dog:
#     def __init__(self):
#         self.temperament = "loyal"
#     def bark(self):
#         print("Woof, woof!")


# class Labrador(Dog):
#     def __init__(self): 
#         super().__init__() # we can't access the class Dog attributes. if we don't use super() function.

        
# new = Labrador()
# print(new.temperament)
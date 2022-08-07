################### Scope ####################



# local scope
def sample():
    new=2 # here new is the local variable, we cannot access it outside the function.
    print(new)
sample() # this will print 2
'''print(new)''' #the above line will show error'''



# global scope
test = 10 # here, test is the global variable we can access and modify this inside the function also.
def sample2():
    print(test)
sample2() # here this will print 10
print(test) # this also will print 10
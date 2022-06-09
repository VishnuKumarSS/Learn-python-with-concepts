# when the function has another function as a parameter, that function is called as
# HIGHER ORDER FUNCTION.

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

# here, calculator is a higher order function, because it has another function as a parameter.
def calculator(n1,n2,func): 
    return func(n1,n2)

result = calculator(2,4,add) # here add is a function, when passing a function to another function, we should not use () brackets.
print(result)
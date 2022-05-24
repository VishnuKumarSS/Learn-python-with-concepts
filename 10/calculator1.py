# defining functions
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

a=int(input("Enter the first number: "))
operations={
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division,
}

for i in operations: # to print all the operators
    print(i)

action=input("Enter an operator to perform: ")
b=int(input("Enter the second number: "))

calc_function=operations[action]
first_answer = calc_function(a,b) # this function acts depending upon the corresponding operations.

print(f"{a} {action} {b} = {first_answer}")


action=input("Enter an operator to perform: ")
calc_function=operations[action]
c=int(input("Enter the next number: "))
second_answer=calc_function(first_answer,c) # here we should use first argument as ----- first_answer
                                            # we should not use the calc_function in the place of first_answer....it will make the code to execute wrong.
print(f"{first_answer} {action} {c} = {second_answer}")


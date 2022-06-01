# defining functions
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

a=float(input("Enter the first number: "))
operations={
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division,
}

for i in operations: # to print all the operators
    print(i)

action=input("Enter an operator to perform: ")
b=float(input("Enter the second number: "))

calc_function=operations[action]
answer = calc_function(a,b) # this function acts depending upon the corresponding operations.

print(f"{a} {action} {b} = {answer}")

end_flag = True # this method is called as Flag
while end_flag:
    end=input("Enter 'y' to continue 'n' to exit.")
    if end =="n":
        print()
        print(f"Total: {answer}")
        end_flag=False
        break
    action=input("Enter an operator to perform: ")
    calc_function=operations[action]
    c=float(input("Enter the next number: "))
    old_answer=answer
    answer=calc_function(answer,c) # here we should use first argument as ----- first_answer
                                                # we should not use the calc_function in the place of first_answer....it will make the code to execute wrong.
    print(f"{old_answer} {action} {c} = {answer}")


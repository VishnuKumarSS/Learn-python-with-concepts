
enemies = "skeleton" # global variable
sample=0
def increase_enemies():
  global sample # note: avoid altering the global variables (i.e) global scope inside the function
  sample+=1 # this shows error if we type this without defining the global keyword in the above line

  enemies = "zombie" # local variable
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# if we want to modify the global variable
# use this method
test=10
def sample():
  return test + 1 # this will return the current value of test variable

#? ***** '''we can access the global variable inside the function but we cannot modify it''' the only way is we can do that with the help of return keyword*****
test = sample()
print(test)
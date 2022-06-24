# Here we are importing prettytable module and typing some code to know about the objects,classes,attributes,methods 
from prettytable import PrettyTable
table = PrettyTable() # here we are creating object called table by assigning the blue print (i.e) class called PrettyTable to it.

table.add_column("Name",["vishnu","sathish","kumar"])
table.add_column("Number",[5,3,7])
print("Default") 
print(table) # this prints the data like table.
# by default the table is center aligned

print("left aligned")
table.align = "l" # here align is the attribute (i.e) variable, so we can't pass the argument to the variables. we can only assign the values to the variables. 
print(table)

print("right aligned")
table.align = "r"
print(table)
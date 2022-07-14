# to get the list as user input
list_of_values = input().split()
for n in range(0, len(list_of_values)):
  list_of_values[n] = int(list_of_values[n])
print(list_of_values)


# below is the function of " min() ""
minimum=list_of_values[0]
for minn in range(len(list_of_values)):
    if list_of_values[minn]<minimum:
        minimum = list_of_values[minn]
print(minimum)
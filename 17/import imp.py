
lis = [ 1,5,6,7,9,2,3,4,6,7,2,1,8,9,5 ]
sorted_list = []
for i in lis:
    for item in sorted_list:
        if i == item:
            break
    else:

        # if i not in sorted_list:
        
        sorted_list += [i]
print(sorted_list)

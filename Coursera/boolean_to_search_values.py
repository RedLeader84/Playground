#using boolean to search for an existing value 

found = False
print("Before", found)
for value in [47, 76, 23, 11, 9, 36, 73, 51, 29, 2] :
    if value == 11 :
        found = True
    print(found, value)
print("After", found)
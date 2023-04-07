smallest_so_far = None
print("Beginning", smallest_so_far)
for value in [12, 55, 8, 36, 99, 14, 87, 66, 23]:
    if smallest_so_far is None:
        smallest_so_far = value
    elif value < smallest_so_far : 
        smallest_so_far = value
    print(smallest_so_far, value)
print("after", smallest_so_far)
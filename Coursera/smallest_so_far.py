smallest = None
print("Beginning")
for value in [12, 55, 8, 36, 99, 14, 87, 66, 23]:
    if smallest is None:
        smallest = value
    elif value < smallest : 
        smallest = value
    print(smallest, value)
print("after", smallest)
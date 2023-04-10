largest = -1
print("Beginning", largest)
for num in [12, 55, 8, 36, 99, 14, 87, 66, 23]:
    if num > largest:
        largest = num
    print(largest, num)

print("after", largest)
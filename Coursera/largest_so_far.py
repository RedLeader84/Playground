largest_so_far = -1
print("Beginning", largest_so_far)
for the_num in [12, 55, 8, 36, 99, 14, 87, 66, 23]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print("after", largest_so_far)
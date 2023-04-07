#How to find the average from the values in a list using a loop
count = 0 
total = 0 
print("Before", count, total)
for value in [47, 76, 23, 11, 9, 36, 73, 51, 29, 2] :
    count = count + 1
    total = total + value
    print(count, total, value)
print("After", count, total, total / count)
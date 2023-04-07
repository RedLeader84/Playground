count = 0 
sum = 0 
print("Before", count, sum)
for value in [ 47, 76, 23, 11, 9, 36, 73, 51, 29, 2] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count)
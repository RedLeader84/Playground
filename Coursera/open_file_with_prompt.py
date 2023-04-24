fname = input("Enter file name: ")
fhand = open(fname, mode = "r")
for line in fhand:
    line = line.rstrip()
    line = line.upper()
print(fhand)
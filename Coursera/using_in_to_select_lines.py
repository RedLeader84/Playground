fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not "@uct.ac.za" in line :
        continue
    print(line)
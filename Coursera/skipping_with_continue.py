fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("from:") :
        continue
    print(line)
    
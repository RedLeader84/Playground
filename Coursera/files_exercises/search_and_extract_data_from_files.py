# Use the file name mbox-short.txt as the file name
import os
os.chdir("/Users/garrettblankenship/Documents/repo/github/playground/coursera/files_exercises")

count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname,'r')
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        continue
total = float(total)
total = total + fh
print(count, total, fh)
print(line)
print("Done")
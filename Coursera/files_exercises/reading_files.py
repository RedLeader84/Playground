# Use words.txt as the file name
import os
os.chdir("/Users/garrettblankenship/Documents/repo/github/playground/coursera/files")

fname = input("Enter file name: ")
try:
    fhand = open(fname,'r')
except:
    print("File cannot be opened as it does not exist: ", fname)
    quit()
for line in fhand: 
    line = line.upper()
    print(line.rstrip())

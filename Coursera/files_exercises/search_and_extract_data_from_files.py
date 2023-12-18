# Use the file name mbox-short.txt as the file name
count = 0
total = 0 

fname = input("Enter file name: ")
try:
    fh = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    quit()
    
for line in fh:
    if line.startswith("X-DSPAM-Confidence: "):
        count = count + 1
        colpos = line.find(':')
        number = line[colpos + 1:].strip()
        SPAM_C = float(number)
        total = total + SPAM_C
        
average = total / count
print("Average spam confidence:", average)
text = "X-DSPAM-Confidence:    0.8475"
fpos = text.find("0")
num = text[fpos:len(text)]
num2 = float(num)
print(num)
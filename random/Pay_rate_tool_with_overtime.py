#Pay rate tool with overtime
hrs = input("Enter Hours Worked:")
rate = float(input("Enter Rate of Pay:"))
h = float(hrs)
r = float(rate)
if h <= 40:
    print(h*r)
else:
    print((h-40)*(1.5*r)+(40*r));
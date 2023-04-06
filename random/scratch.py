#hrs = float(input("Enter Hours:"))35
#rate = float(input("Enter Rate of Pay:"))
#pay = hrs * rate
#print(pay)

#x = -2.5
#if x < 2 :
#   print('Below 2')
#elif x >= 2 :
#    print('Two or more')
#else :
#    print('Something else')

score = float(input("Enter Score: "))
s = float(score)


      
try:        
    if s >= 0.9:
        print (str("A"))
    elif s >= 0.8:
        print (str("B"))
    elif s >= 0.7:
        print (str("C"))
    elif s >= 0.6:
        print (str("D"))
    elif s < 0.6:
        print (str("F"))
        
except:
    if s < 0.0:
        print ("Score Cannot be Lower than 0.0")
    if s > 1.0:
        print ("Score Cannot be Higher than 1.0")
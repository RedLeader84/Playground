
score = float(input("Enter Score: "))
s = float(score)

def grades():
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
try:        
    grades()

except:
    s > 1.0
    print ("Score Cannot be Higher than 1.0")  
    
    #Hello
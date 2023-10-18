def getIncomeTax(salary):
    allowance = 11850
    total = salary - allowance
    if 150000 <= salary :
        tax = (total * 0.45)
        print(tax)
        
    elif 150000 >= salary >= 34501:
        tax = (total * 0.40)
        print(tax)
      
    elif 34500 >= salary >= 0:
        tax = (total * 0.20)
        print(tax)
        
    else:
        print("no tax payment")
    
getIncomeTax(int (input ("how much do you earn: £")))

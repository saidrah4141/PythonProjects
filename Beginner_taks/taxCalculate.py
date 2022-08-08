'''
Created on Aug. 8, 2022

* tax on first 10k is 0 next 10k is 10% after that its 20% on the remaing income after first 2 10k 

@author: Said
'''



def tax_cal(income):
    if income <= 10000:
        tax = 0;
    elif income <= 20000:
        tax = 1000
    elif income > 20000:
        tax = (income - 20000) * .2 + 1000
    print(tax)
    
tax_cal(10000)
tax_cal(20000)
tax_cal(45000)
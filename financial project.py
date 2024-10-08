
    
def opening ():
    print('#####################################')
    print('Welcome to the investment quote system')
    print('') #indent was fixed
    print('Please enter your name')#indent was fixed
    opening.name = input()
    
    print('Please enter your Address')
    opening.address = input()
    
    print ('Please enter your telephone number') # spelling
    opening.phone = input()
    
    print ('How much would you like to invest per month (£)?')
    opening.investSum = input()
    while opening.investSum.isnumeric() == False:
        opening.investSum = input('How much would you like to invest per month (£)? it must be a Number \n')

def options ():
    print('#####################################')
    print('There are two types of investment available:')
    print('Option 1 - Savings plan')
    print('Option 2 - Managed stock investment')
    print('Please select an option (press 1 or 2 followed by enter)')
    print('#####################################')
    
    option = input()
          
      
    while option != '1' and option != '2':
        print('Please select an option (press 1 or 2 followed by enter)')
        
        option = input()
        
    if option == '1':
        savingsMain()
    else: #added and s at the end to make it the same as the fuction
        stocksMain()
        

def savingsMain():
    savingsMain.monthlyInvest = float(opening.investSum)#added float to stop a repeat
    savingsMain.yearlyInvest = int(savingsMain.monthlyInvest * 12) #added and int so it store it as a intger not a string
    
    while savingsMain.yearlyInvest > 20000: #changed the less than sign to a greater sign
        print('The the initial monthly amount is too high for this type of plan' )
        print ('How much would you like to invest per month (£)?')
        savingsMain.monthlyInvest = float(input())
        savingsMain.yearlyInvest = savingsMain.monthlyInvest * 12
    
    savingsPrint()
    
    

def savingsMin():
    predictReturns = 0.012
    yearlyFees = 0.0025 * 12
    savingsMin.total = savingsMain.yearlyInvest
    print('#####################################')   
    print('Forecasted perfromance of this plan at the lowest rate of return:')
    
    for i in range(10):
        savingsMin.total = (savingsMin.total +(savingsMin.total * predictReturns)) - yearlyFees
        
        
        if i == 0 or i == 4 or i == 9: # cause the for loop starts on 0
            print('At the end of year', str(i+1))
            print('Yourinvestment will be worth:')
            print('£'"{0:.2f}".format(savingsMin.total))# added formatting
            print('')
            print('Total fees paid in this period:')
            print("£{0:.2f}".format(yearlyFees * (i+1)))# added formatting
            print('')
            print('Total profit in this period:')
            print("£{0:.2f}".format(savingsMin.total - (yearlyFees * (i+1)))) # added formatting
            print('')
    print('#####################################')
    print('')
 
def savingsMax():
    predictReturns = 0.024
    yearlyFees = 0.0025 * 12
    savingsMax.total = savingsMain.yearlyInvest
    print('#####################################')
    print('Forecasted perfromance of this plan at the highest rate of return::')
    
    for i in range(10):
        savingsMax.total = (savingsMax.total + (savingsMax.total * predictReturns)) - yearlyFees
        
         
        if i == 0 or i == 4 or i == 9:
            print('At the end of year', str(i+1))
            print('Your investment will be worth:')
            print('£'"{0:.2f}".format(savingsMax.total))#added formating
            print('')
            print('Total fees paid in this period:',
            print("£{0:.2f}".format(yearlyFees * (i+1))))#added formanting
            print('')
            print('Total profit in this period:')
            print("£{0:.2f}".format(savingsMax.total - (yearlyFees * (i+1))))#added formating
            print('')
    print('#####################################')  
    print('')

     
def stocksMain():
    stocksMain.monthlyInvest = int(opening.investSum)
    stocksMain.yearlyInvest = stocksMain.monthlyInvest * 12
    
    stocksPrint()
    
def stocksMin():
    predictReturns = 0.04
    yearlyFees = 0.13 * 12
    stocksMin.total = int(stocksMain.yearlyInvest)
    print('#####################################')   
    print('Forecasted perfromance of this plan at the lowest rate of return:')
    
    for i in range(10):
        stocksMin.total = stocksMin.total + stocksMin.total * predictReturns - yearlyFees
        
        if stocksMin.total >= 40000:
            taxRate = 0.2
        elif stocksMin.total >= 12000:
            taxRate = 0.1
        else:
            taxRate = 0
        
        taxPayable = stocksMin.total * taxRate
        postTax = stocksMin.total - taxPayable
        
              
        if i == 0 or i == 4 or i == 9:
            print('At the end of year', str(i+1))
            print('Your investment will be worth:')
            print('£'"{0:.2f}".format( postTax))
            print('')
            print('Total fees paid in this period:')
            print("£{0:.2f}".format(yearlyFees * (i+1)))
            print('')
            print('Total profit in this period:')
            print("£{0:.2f}".format(postTax - (yearlyFees * (i+1))))
            print('')
            print('Total tax due in this period:')
            print("£{0:.2f}".format(taxPayable))
            print('')
    print('#####################################')
    print('') 

def stocksMax():
    predictReturns = 0.23
    yearlyFees = 0.13 * 12
    stocksMax.total = int(stocksMain.yearlyInvest)# added a int statment to define it as a number not a string allowing the float to be times with it
    print('#####################################')   
    print('Forecasted perfromance of this plan at the higher rate of return:')
    
    for i in range(10):
        stocksMax.total = (stocksMax.total + (stocksMax.total) * predictReturns) - yearlyFees
        
        if stocksMax.total >= 40000:
            taxRate = 0.2
        elif stocksMax.total >= 12000:
            taxRate = 0.1
        else:
            taxRate = 0
        
        taxPayable = stocksMin.total * taxRate
        postTax = stocksMin.total - taxPayable
        
              
        if i == 0 or i == 4 or i == 9:
            print('At the end of year', str(i+1))
            print('Your investment will be worth:')
            print("£{0:.2f}".format (postTax))
            print('')
            print('Total fees paid in this period:')
            print("{0:.2f}".format(yearlyFees * (i+1)))
            print('')
            print('Total profit in this period:')
            print("{0:.2f}".format(postTax - (yearlyFees * (i+1))))
            print('')
            print('Total tax due in this period:')
            print("£{0:.2f}".format(taxPayable,2))
            print('')
    print('#####################################')
    print('') 


def savingsPrint ():
    print('--------------------------------------------------------')
    print('Personal Investment Quote for:')
    print('Name: ', opening.name)
    print('')
    print('Telephone Number: ', opening.phone)
    print('--------------------------------------------------------')
    print('')
    print('You selected a savings plan')
    savingsMin()
    savingsMax()

def stocksPrint ():
    print('--------------------------------------------------------')
    print('Personal Investment Quote for:')
    print('Name: ', opening.name)
    print('')
    print('Telephone Number: ', opening.phone)
    print('--------------------------------------------------------')
    print('')
    print('You chose a Managed Stock Investment plan')
    stocksMin()
    stocksMax()


opening()
options()

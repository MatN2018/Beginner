##Problem Set 1a
##Name: Naftal Mautia
##Time Spent: ????
##http://stackoverflow.com/questions/15484917/computing-the-lowest-monthly-payment-using-bisection-search-in-python

##convert the user's inputs to variables
balance = float(raw_input ( 'Give the balance: ' ))
annRate = float(raw_input ( 'Give the annual interest rate in decimals: '))

##bisection search parameters
monthRate = annRate/12
monthLow = balance/12
monthUpper = (balance*(1 + monthRate)**12) / 12
epsilon = 0.01

#initiliaze state variables
months = 0
startBalance = balance

while abs(balance) > epsilon:
    balance = startBalance
    monthPay = (monthLow + monthUpper)/2
    for months in range (0,12):
        balance = (balance - monthPay)*(1 + monthRate)
        ##balance -= monthPay
        ##balance *= 1 + monthRate
        months += 1
    if balance > 0:
        monthLow = monthPay
    else:
        monthUpper = monthPay
    break
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year:', '$' + str(monthPay)
print 'Number of months needed:', months
print 'Balance:', '$' + str(balance)

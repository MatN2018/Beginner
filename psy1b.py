##Problem Set 1a
##Name: Naftal Mautia
##Time Spent: ????

##convert the user's inputs to variables
startBalance = float(raw_input ( 'Give the balance: ' ))
annRate = float(raw_input ( 'Give the annual interest rate in decimals: ' ))

##calculate monthly interest rate in decimals
monthRate = annRate/12

##initialize the state variables
monthPayment = 10
balance = startBalance

while balance > 0:
    balance = startBalance
    monthPayment += 10
    months = 0
    while months < 12 and balance > 0:
        balance = balance*(1 + monthRate) - monthPayment
        months += 1

print 'RESULT'
print 'Monthly payment to pay off debt in 1 year:', '$' + str(monthPayment)
print 'Number of months needed:', months
print 'Balance:', '$' + str(balance)

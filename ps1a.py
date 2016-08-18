##Problem Set 1a
#Name: Naftal Mautia
#Time Spent: ????

##convert the user's inputs to variables
balance = float(raw_input ( 'Give the balance at the start of the month: ' ))
annual_rate = float(raw_input ( 'Give the annual interest rate in decimals: ' ))
min_pay_rate = float(raw_input ( 'Give the minimum monthly payment rate in decimals: ' ))


##calculate monthly interest rate in decimals
month_rate = annual_rate/12

##define the starting variables that'll be used in the while loop
total_paid = 0
months = 1

while (months <= 12):
    print 'Month', months

    min_pay_amount = round((balance*min_pay_rate), 2)
    month_rate_amount = round((balance*month_rate), 2)
    principle_paid = min_pay_amount - month_rate_amount
    
    print "Minimum monthly payment:", "$" + str(min_pay_amount)
    print "Principle paid:", "$" + str(principle_paid)

    balance = balance - principle_paid

    ##no need to create new variable "remaining_balance" when you can use the existing varaible "balance",
    ##otherwise the balance won't change when using ^ that line of code up there 
    print "Remaining balance:", "$" + str(balance)

    total_paid += min_pay_amount
    months += 1

print 'RESULT'
print 'Total amount paid:', "$" + str(total_paid)
print 'Remaining balance:', "$" + str(balance)

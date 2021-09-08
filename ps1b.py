#Navinder Kour
#ProblemSer 1b
#Time Spend : 6 hours


balance= float(input("Enter the outstanding balance on your credit card: "))
annualInterestRate= float(input("Enter the annual credit card interest rate as a decimal:"))

monthlypayment=500
monthlyinterestrate =annualInterestRate/12
bal=balance
lowerBound = balance / 12
higherBound = (balance *(1+monthlyinterestrate)**12)/12.0
month = 0

while balance != 0:     
    i = ((lowerBound + higherBound) / 2)
    balance = bal
    while month < 12:
        month +=1
        balance = balance - i
        interest = balance * (annualInterestRate / 12)
        balance = balance + interest
    month = 0
    if balance <= 0:
        higherBound = i
    elif balance >= 0:
        lowerBound = i
    balance = float("%.2f" % balance)


print("result")
print("Monthly payment to pay off debt in 1 year:" + str("%.2f" % i))
print("Number of months needed: ",month)
print("Balance:",balance)
#error in nimber of months and balance
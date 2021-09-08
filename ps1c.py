#Navinder Kour
#ProblemSer 1c
#Time Spend : 8 hours


balance= float(input("Enter the outstanding balance on your credit card: "))
annualInterestRate= float(input("Enter the annual credit card interest rate as a decimal:"))


monthlyinterestrate =annualInterestRate/12
bal=balance
lowerBound = balance / 12
higherBound = (balance *(1+monthlyinterestrate)**12)/12.0
month = 0
epsilon = 0.01
mid = ((lowerBound + higherBound) / 2)
min_pay = mid
while abs(balance) >=epsilon: 
    balance = bal
    while month < 12:
        month +=1
        balance = balance - i
        interest = balance * (annualInterestRate / 12)
        balance = balance + interest
    month = 0
    if balance > 0:
        lowerBound = mid
    else:
        higherBound = mid
    mid = (lowerBound + higherBound)/2


print("result")
print("Monthly payment to pay off debt in 1 year:" + str("%.2f" % i))
print("Number of months needed: ",month)
print("Balance:",balance)
#error in nimber of months and balance
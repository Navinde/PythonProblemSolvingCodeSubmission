# Problem Set 1a
# Name: Navinder kour
# Time Spent: 1 hour


balance= float(input("Enter the outstanding balance on your credit card: "))
ann_interest= float(input("Enter the annual credit card interest rate as a decimal:"))
mon_pay_interest= float(input("Enter the minimum monthly payment rate as a decimal: "))
bal=balance
result=0
for i in range(1,13):
    min_monthly_payment=bal*mon_pay_interest
    int_paid=ann_interest/12*bal
    principal_pay=min_monthly_payment-int_paid
    remain_bal=bal-principal_pay
    print("month",i)
    print("minimum monthly payment:",min_monthly_payment)
    print("principal_paid:",principal_pay)
    print("remaining balance",remain_bal)
    result=result + min_monthly_payment
    bal=remain_bal
print("result:")
print("Total amount paid the year:",result)
print("Balance:",bal)
    

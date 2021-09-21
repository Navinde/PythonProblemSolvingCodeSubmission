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
#error in nimber of months and balance3?




#Navinder Kour
#problem set 2
#Time Spend : 8 hours

def evaluate_poly(poly, x):
    result=0
    for i in range(0, len(poly)):
        result += poly[i] * x**i
    return result
poly = (0.0, 0.0, 5.0, 9.3, 7.0) 
x = -13
print(evaluate_poly(poly, x))
    


def compute_deriv(poly):
    result = ()
    for i in range(1, len(poly)):
        result += (poly[i]*(i),)
    return result
    
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    
print(compute_deriv(poly))    


 
def compute_root(poly, x_0, epsilon):
    
    x_n = x_0
    count = 1
    while(abs(evaluate_poly(poly,x_n))>epsilon):
        y = evaluate_poly(poly, x_n)
        z = evaluate_poly(compute_deriv(poly), x_n)
        x_n= (x_n - y/z) 
        count = count + 1 
    return (x_n,count)
    
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    
x_0 = 0.1
epsilon = .0001
print(compute_root(poly, x_0, epsilon))
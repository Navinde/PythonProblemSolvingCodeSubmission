#  problem set=2
#  name:navinder kour
#  time spent:8 hours




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
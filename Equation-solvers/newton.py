import numpy as np
func = lambda x: (x - 1)**3 
der_func = lambda x: 3 * (x - 1)**2
x0  = float(input("x0: "))
eps = float(input("epsilon: "))
xn=0
prev=x0
iterations=0
prev_prev=0
p=0
xs=[]
while abs(xn-prev)>eps:
    prev_prev=prev
    prev=x0
    xn=-func(x0)/der_func(x0)+x0
    xs.append(xn)
    if iterations>=2:
        q=(xn-prev)/(prev-prev_prev)
        p=1/(1-q) # порядок корня при числе итераций стремящемся к бесконечности
    x0=xn
    
    iterations+=1
print("Solution ", xn)
print("Multiplicity", p)

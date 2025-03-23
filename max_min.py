import sympy as sp;

x=sp.Symbol('x')
f=(x*3)- (3*x*2) + 4

f_deri=sp.diff(f,x) #diff for diffferentation
f_double=sp.diff(f_deri,x)
sol=sp.solve(f,x)  # solve for finding solution
for i in sol:
    if(f_double.subs(x,i)>0):
        nature= "minimum"
    elif(f_double.subs(x,i)<0):
        nature="maximum"
    else:
        nature="critical point"

    
    print(f"point: x = {i}")
    print(f"Nature: {nature}\n")
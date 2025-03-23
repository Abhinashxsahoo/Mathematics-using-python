
import sympy as sp
x= sp.symbols('x')
f= x**2 + 3*x + 5
f_derivative= sp.diff(f,x)

result = f_derivative.subs(x, 2)

print("Function:=", f)
print("Derivative:", f_derivative)
print("Value of derivative at x=2:", result)
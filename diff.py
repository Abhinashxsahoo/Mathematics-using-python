import sympy as sp

x = sp.Symbol('x')
f = x**3 + 2*x
f_derivative = sp.diff(f, x)

f_double_derivative = sp.diff(f_derivative, x)
print("Function: f(x) =", f)
print("First derivative: f'(x) =", f_derivative)
print("Second derivative: f''(x) =", f_double_derivative)

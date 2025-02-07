def solve_linear_solution():
    #coefficients for linear equations
    print("coefficients of two linear equations")
    a1 = int(input("Enter a1: "))
    b1 = int(input("Enter b1: "))
    c1 = int(input("Enter c1: "))
    a2 = int(input("Enter a2: "))
    b2 = int(input("Enter b2: "))
    c2 = int(input("Enter c2: "))

    #Cramers rule
     
    x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
    y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)
    print("x = ", x)
    print("y = ", y)
    

    print("Determinant is 0")
linear_solution = solve_linear_solution()



def solve_lin_eqsol(a1,a2,b1,b2,c1,c2):
    determinant= a1*b2-a2*b1
    
    if determinant==0:
        return "system of linear equations have no solution"
    inverse_a= [[ b2/determinant, -b1/determinant],[-a2/determinant, a1/determinant]]
    B= [c1, c2]
    x= inverse_a[0][0]* B[0] +inverse_a[0][1]* B[1]
    y= inverse_a[1][0]* B[0] +inverse_a[1][1]* B[1]
    return x,y

a1,b1,c1=1,1,3
a2,b2,c2=1,-1,1
solution= solve_lin_eqsol(a1,a2,b1,b2,c1,c2)
print("Solution:", solution)

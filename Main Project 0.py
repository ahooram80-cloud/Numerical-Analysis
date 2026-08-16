import time as time
import sys
from math import *
import math as math
import numpy as np
from sympy import *
from numpy.linalg import *
import os
from scipy import integrate
pi=math.pi
pi=float(pi)
print(pi)
# Notes Section. not part of nor related to the program
"""
from scipy.misc import derivative
import scipy as sp
def Derive(y,x)
    x=symbols('x', real=True)
    def function(x):
        return eval(y)
    dfdx=diff(f(x),x)
    return dfdx
#or something like that...
"""
# Functions used in the Program:

def jacobi(A, b, x_init, epsilon, max_iterations):
    D = np.diag(np.diag(A)) #Get The Diagonal Values
    print("This Shows The Matrix With Diagonal Values\n", D)
    LU = A - D #Get The Matrix Where Diagonal Values = 0
    print("\nThis Shows The Matrix Where Diagonal Values = 0\n", LU)
    print("\n")
    #Forming the inverse matrix of the Diagonal matrix which soon will be multiplied into the numerator
    D_inv = np.diag(1 / np.diag(D))
    print("n".center(10), "Old x1".center(15), "Old x2".center(15), "Old x3".center(15), "New x1".center(20), "New x2".center(20), "New x3".center(20), "Norm Of Matrix xNew-xOld".center(25))
    print("="*155)
    x = x_init #Initial values
    for i in range(max_iterations):
        x_new = np.dot(D_inv, b - np.dot(LU, x))
        print(str(i+1).center(10),
              str(format(x[0], '.'+ str(dp) + 'f').center(15)), str(format(x[1], '.'+ str(dp) + 'f')).center(15), str(format(x[2], '.'+ str(dp) + 'f')).center(15),
               str(format(x_new[0], '.'+ str(dp) + 'f')).center(20),str(format(x_new[1], '.'+ str(dp) + 'f')).center(20),str(format(x_new[2], '.'+ str(dp) + 'f')).center(20),
               str(format(np.linalg.norm(x_new - x)).center(25)))
        if np.linalg.norm(x_new - x) < epsilon:
            print("\nThe Jacobi Method Succeeded After " + str(i+1) + " Iterations")
            return x_new
    if (i+1 == max_iterations)and np.linalg.norm(x_new - x) > epsilon:
        print("\nThe Jacobi Method Has Failed After " + str(max_iterations) + " Iterations")
    return x

def R(T):
    temp=abs(log(tol,10))
    temp=int(round(temp,0))
    return (round(T,temp+1))

def string_to_function(expression):
    def function(x):
        return eval(expression)
    return function

# Derivation function
#current issue: since I couldn't implement derivation precisely the returned values aren'taccurate.
def Fpp(x):
    h=0.000000000000001
    dydx=(F(x+h)-F(x))/h
    return dydx

Fp=string_to_function(str("sin(x)+x*cos(x)"))


def Pause(text):
    for char in text:
        sys.stdout.write(char)
        time.sleep(0.5)

def Finished():
    print("The program finished successfully")
    retry=str(input("Would you like to run another program?"))
    while True:
        if retry=="0" or retry=="n" or retry=="no" :
            return(True)
        elif retry=="1" or retry=="y" or retry=="yes" :
            return(False)
        else:
            print("try again")

def Sign(n,m):
    if n*m>0:
        return("+")
    elif n*m<0:
        return("-")
    else:
        return("0")
    
# Section dedicated for saving custom equations instead of entering them by hand via the string_to_function() tool:
    #still hasn't been implemented
    
    
    
    
# Start of the actual program

print("Welcome to the app Numerical Analysis!\nin this program the methods mentioned in the book have been programmed in one single package for ease.\nby selecting the respective number to the provided method you may solve the equasions or integrations")
Pause("......")
done=bool(False)
while True:
    if done==True:
        print("program finished.")
        break
    print("\nPlease enter the number of the wanted method to run:\n(enter 0 to exit)")
    program_list=["1. Bisection", "2. Fixed-Point Iteration", "3. Newton-Raphson", "4. Gaussian Elimination", "5. Gaussian Elimination with Partial Pivoting", "6. Jacobi iterative method" , "7. Gauss-Seidel iterative technique", "8. Newton’s Divided-Difference Formula", "9. Newton Forward-Difference Formula", "10. Trapezoidal Rule", "11. Midpoint rule", "12. Simpson’s Rule", "13. Romberg Integration", "14. Euler’s method", "15. Euler’s method (Revanced)", "16. Runge-Kutta method of Order Two", "17. Runge-Kutta Order Four", "18. Finite Difference Method"]
    for i in range(len(program_list)) :
        print(program_list[i])
    try: 
        program=int(input("\nSelect Program: "))
    except ValueError:
        print("incorrect input, please try again")
        Pause("...")
        continue
    try:
        if program==0:
            done=True
            continue
        else:
            print(f"selected: {program_list[program-1]}")
    except IndexError:
        print("incorrect input, please try again")
        Pause("...")
        continue
    
    
    if program==1:
        F=string_to_function(str(input("Please write your function:")))
        # use ** for "x power y", * for multiplication and 
        a=float(input("please select a range from a to b: \n a: "))
        b=float(input("b: "))
        tol=float(input("tolerance:"))
        ave=float(1.0)
        n=0
        print("n\t\t\t\ta\t\t\t\tb\t\t\t\tave\t\t\t\tf(a)f(x)")
        while True: 
            n+=1
            ave=(a+b)/2
            Fa=F(a)
            Fx=F(ave)
            num = float(Fa*Fx)
            if num > 0:
                temp=a
                a=ave
                print(f"{n}\t\t\t\t{a}\t\t\t\t{b}\t\t\t\t{ave}\t\t\t\t+")
            elif num == 0:
               print(f"{n}\t\t\t\t{a}\t\t\t\t{b}\t\t\t\t{ave}\t\t\t\tanswer")
               break
            else:
               temp=b
               b=ave
               print(f"{n}\t\t\t\t{a}\t\t\t\t{b}\t\t\t\t{ave}\t\t\t\t-")
            if (abs(a-b)<tol):
                print(f"{n}\t\t\t\t{a}\t\t\t\t{b}\t\t\t\t{ave}\t\t\t\tanswer")
                break 
        done=Finished()
        
        
    elif program==2:
        F=string_to_function(str(input("Please write your function:")))
        # use ** for "x power y", * for multiplication and 
        a=float(input("please select a range from a to b: \n a: "))
        b=float(input("b: "))
        tol=float(input("tolerance:"))
        x=(a*F(b)-b*F(a))/(F(b)-F(a))
        n=1
        print(f"{'n':<10}{'a':<10}{'b':<10}{'f(a)':<10}{'f(x)':<10}{'f(a)f(x)':<10}")
        print("-" * 60)
        while abs(F(x))>tol :
            print(f"{R(n):<10}{R(a):<10}{R(b):<10}{R(F(a)):<10}{R(F(x)):<10}{Sign(F(a),F(x)):<10}")
            if F(x)*F(a)>0:
                a=x
            else:
                b=x
            x=(a*F(b)-b*F(a))/(F(b)-F(a))
            n=n+1
        print(f"ROOT= {x}")
        print(f"ITERATION= {n}")
        done=Finished()
        
#current issue: look at Fp() function.
    elif program==3:
        F=string_to_function(str(input("Please write your function:")))
        # use ** for "x power y", * for multiplication and 
        x=float(input("x0="))
        x=x - F(x)/Fp(x)
        print(x)
        n=1
        tol=float(input("tolerance:"))
        print(f"{'n':<10}{'x':<10}{'x+1':<10}{'dx':<10}")
        print("-" * 40)
        while abs(F(x))>tol:
            x1=x
            x=x - F(x)/Fp(x)
            n=n+1
            print(f"{n-1:<10}{R(x1):<10}{R(x):<10}{R(x-x1):<10}")
        print(f"ROOT= {x}")
        print(f"ITERATION= {n}")
        done=Finished()

#current issue: not correct root of the last step
    elif program==4:
        rows=int(input("please enter number of the rows (how many equations?)...\nrows:"))
        col=int(input("and columns (number of coefficients+standalone number after the =)\ncolumns:"))
        matrix=[]
        for i in range(rows):   
            row = []
            for j in range(col):
                row.append(float(input(f"a[{i},{j}]=")))    # user input for rows
            matrix.append(row)  # adding rows to the matrix
        print("\n2D matrix is:")
        for i in range(rows):
            for j in range(col):
                print(matrix[i][j], end="  \t")
            print()
        m=rows-1
        i=0
        j=0
        _=0
        for _ in range(m):
            I=[]
            matrix0=matrix
            for o in range (m-_):
                I.append(float(-1*matrix0[o+_+1][_]/matrix0[_][_]))
            for i in range(rows-1-_):
                for j in range(col):
                    matrix[i+1+_][j]=matrix0[_][j]*I[i]+matrix0[i+_+1][j]         
            print(f"\n matrix after step {_+1}:")
            for i in range(rows):
                for j in range(col):
                    print(matrix[i][j], end="  \t")
                print()
        c=[]
        for k in range(col-1):
            s=0
            for l in range(col):
                if (col-2-k)==l:
                    continue
                elif l==col-1:
                    s=s+matrix[-k-1][l]
                else:
                    #a mistake us hapenning here at the k=2 (col=4) and I have no idea why the sum isn't correct
                    s=s-matrix[-k-1][l]
            c_temp=s/matrix[-k-1][-k-2]
            print(s, matrix[-k-1][-k-2])
            for u in range(col-k-2):
                matrix[-2-u][-k-2]=matrix[-2-u][-k-2]*c_temp
                print(matrix[-2-u][-k-2])
            c.append(c_temp)          
            print(f"c{col-k-1}={c[k]}")

    elif program==5:
        #
        continue
    
    elif program==6:
        converge = False
        cont = 'N'
        diagonal_zero = False
        while converge == False:
            A = eval(input("Enter your square matrix (n x n) in 2D array form, eg [[1,2,3],[2,3,1],[1,2,3]]: "))
            A = np.array(A)
            num_rows, num_cols = A.shape #Dimension
            k = 0
            for i in range (num_rows):
                if (A[i][k] == 0):
                    print("\nWARNING! 0 Is Detected In Diagonal Of The Position Of Row Number", i+1, "and Column Number", k+1, "Please Enter A New Matrix\n")
                    diagonal_zero = True
                    break
                else:
                    k = k + 1
                    diagonal_zero = False
            if diagonal_zero == False:
                D = np.diag(np.abs(A)) # Find diagonal coefficients
                S = np.sum(np.abs(A), axis=1) - D # Find row sum without diagonal
                if np.all(D > S):
                    print ('Matrix is diagonally dominant')
                else:
                    print ('Matrix is NOT diagonally dominant')
                D = np.diag(np.diag(A))
                D_inv = np.diag(1 / np.diag(D))
                LU = A - D
                norm = np.linalg.norm(np.dot(D_inv,LU))
                if norm >= 1:
                    print("WARNING! This Iteration MAY NOT Converge, The Frobenius Norm of ||D^-1 times M|| Is " + str(norm) + " " + u"\u2265 1\n")
                    cont = input("Do you want to proceed with the iteration? Y for Yes, N for No and Enter New 2D Array: " )
                    print("")
                    cont = cont.upper()
                    if cont == 'Y':
                        converge = True
                else:
                    print("This Iteration Will Converge, The Frobenius Norm of ||D^-1 times M|| Is ", norm,  " < 1\n")
                    converge = True
        b = eval(input("Enter your value of b in 1D array form, eg [1,2,3]: "))
        b = np.array(b)
        x_init = eval(input("Enter your initial guess in 1D array form, eg [2,4,6]: "))
        x_init = np.array(x_init)
        epsilon = eval(input("Enter TOL: "))
        dp = str(epsilon)[::-1].find('.')
        dp = dp + 1
        np.set_printoptions(precision=dp)
        max_iterations = eval(input("Enter Number Of Maximum Iterations: "))
        x = jacobi(A, b, x_init, epsilon, max_iterations)
        print('\nx:', x)
        print('Computed b by substituting the computed x value:', np.dot(A, x))
        print('Real b values:', b)
        print('Actual Solution from built-in functions = %s' % solve(A, b))
        # os.system("pause")
        done=Finished()

    elif program==7:
        continue
    elif program==8:
        continue
    
# not ready. work in progress...
    elif program==9:
        """
        F=string_to_function(str(input("Please write your function:")))
        # please use ** for "x power y", * for multiplication and exp(x) for "e^x"
        a=float(input("please select a range from a to b: \n a: "))
        b=float(input("b: "))
        tol=float(input("tolerance:"))
        ave=float(1.0)
        n=0
        list=[[a,b,c],2,3]
        x=[]
        f=[]
        xx=[]
        xy=[]
        Sx=float(0)
        Sy=float(0)
        Sxx=float(0)
        Sxy=float(0)
        i=int(0)
        j=int(0)
        k=int(0)
        n=int(input("n="))
        for i in range(n):
            x.append(float(input(f"x{i+1}= ")))
            f.append(float(input(f"f{i+1}= ")))
        _=0
        df=[]
        temp=[]
        print(f"i={i}")
        for _ in range (i) :
        	temp.append(float(f[_+1]-f[_]))
        	print(temp)
        df.append(temp)
        print(df)
        for j in range (i) :
        	if j == 0:
        		continue
        	else:
        		for _ in range (i-j) :
        			df.append([j,flo at(df[j[_]]-df[j[_+1]])])
        print(df)
        #for o in range(0, len(x)):
        #    xx.append(x[o] * x[o])
        #    xy.append(x[o] * y[o])
        #for j in range(n):
        #    Sx=sum(x)
        #    Sy=sum(y)
        #    Sxx=sum(xx)
        #    Sxy=sum(xy)
        #for k in range(n):
        #    # print(f"x{k+1}= {x[k]}")
        #    # print(f"y{k+1}= {y[k]}")
        #    print(f"xx{k+1}= {xx[k]}")
        #    print(f"xy{k+1}= {xy[k]}")
        #textx='['"x"']'
        #texty='['"y"']'
        #textxx='['"xx"']'
        #textxy='['"xy"']'
        #print(textx+f"={Sx}")
        #print(texty+f"={Sy}")
        #print(textxx+f"={Sxx}")
        #print(textxy+f"={Sxy}")
        #a=float(((n*Sxy)-(Sx*Sy))/((n*Sxx)-(Sx*Sx)))
        #b=float(((Sy*Sxx)-(Sx*Sxy))/((n*Sxx)-(Sx*Sx)))
        #print(f"Y={a}X+{b}")
        #print(f"a={a}\nb={b}")
        """
    elif program==10:
        F=string_to_function(str(input("Please write your function:")))
        # use ** for "x power y", * for multiplication and 
        a=float(input("please select a range from a to b: \n a: "))
        b=float(pi)
        n=int(input("n: "))
        s= (F(a) + F(b))/2
        h= (b-a)/n
        print (f"h={h}")
        for i in range(1,n) :
            print(f"i={i}")
            s = s + F(a + i*h)
            print (f"s={s}")
        s=s*h
        print(f"s*h={s}")
        done=Finished()
    elif program==11:
        F=string_to_function(str(input("Please write your function:")))
        # use ** for "x power y", * for multiplication and 
        a=float(input("please select a range from a to b: \n a: "))
        b=float(input("b: "))
        n=int(input("n: "))
        s= 0
        h= (b-a)/n
        print (f"h={h}")
        for i in range(n) :
            print(f"i={i}")
            s = s + F(a + h/2+ i*h)
            print (f"s={s}")
        s =s*h
        print(f"s*h={s}")
        done=Finished()
    elif program==12:
        F=string_to_function(str(input("Please write your function:")))
        # use ** for "x power y", * for multiplication and 
        a=float(input("please select a range from a to b: \n a: "))
        b=float(pi/2)
        n=int(input("n: "))
        s= 0
        h= (b-a)/n
        h2= h/2
        h3=F(a+h2)
        print (f"h={h}")
        for i in range(1,n) :
            print(f"i={i}")
            s = s + F(a + i*h)
            h3 = h3 +F(a+i*h+h2)
            print (f"s={s}")
        s =(h/6)*(F(a)+4*h3+2*s+F(b))
        print(f"s*h={s}")
        done=Finished()
    elif program==13:
        gfg = lambda x: x*np.ln(x+1)
        # using scipy.integrate.romberg()
        geek = integrate.romberg(gfg, -0.75, 0.75, show = True)
        done=Finished()
        print(geek)
    elif program==14:
        continue
    elif program==15:
        continue
    elif program==16:
        continue
    elif program==17:
        continue
    elif program==18:
        continue
    elif program==0:
            break
    
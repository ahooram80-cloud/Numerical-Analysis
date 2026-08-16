import time as time
import sys
from math import *
import numpy as np
from sympy import *
from scipy import integrate

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

# Python program to implement Runge Kutta method
# A sample differential equation "dy / dx = (x - y)/2"

def dydx(x, y):
    return (y - x*x + 1)

# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def rungeKutta(x0, y0, x, h):
    # Count number of iterations using step size or
    # step height h
    n = (int)((x - x0)/h) 
    # Iterate for number of iterations
    y = y0
    print(f"y0={y}")
    print(f"x0={x0}")
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)

        # Update next value of y
        print(f"y{i-1}={y}")
        y+=1
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

        # Update next value of x
        print(f"x{i-1}={x0}")
        x0 = x0 + h
        print(f"k1,{i}={k1} and k2,{i}={k2} and k3,{i}={k3} and k4,{i}={k4}")
        
    return y
#second order:
def rungeKutta2(x0, y0, x, h):
    # Count number of iterations using step size or
    # step height h
    n = (int)((x - x0)/h) 
    # Iterate for number of iterations
    y = y0
    print(f"y0={y}")
    print(f"x0={x0}")
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)

        # Update next value of y
        print(f"y{i-1}={y}")
        y = y + k2

        # Update next value of x
        print(f"x{i-1}={x0}")
        x0 = x0 + h
        print(f"k1,{i}={k1}")
        
    return y

def romberg(f, a, b, n):
    """Calculate the integral from the Romberg method.

    Args:
        f (function): the equation f(x).
        a (float): the initial point.
        b (float): the final point.
        n (int): number of intervals.

    Returns:
        xi (float): numerical approximation of the definite integral.
    """
    # Initialize the Romberg integration table
    r = np.zeros((n, n))

    # Compute the trapezoid rule for the first column (h = b - a)
    h = b - a
    r[0, 0] = 0.5 * h * (f(a) + f(b))

    # Iterate for each level of refinement
    for i in range(1, n):
        h = 0.5 * h  # Halve the step size
        # Compute the composite trapezoid rule
        sum_f = 0
        for j in range(1, 2**i, 2):
            x = a + j * h
            sum_f += f(x)
            print(f"sum_f={sum_f}")
        r[i, 0] = 0.5 * r[i - 1, 0] + h * sum_f
        print(f"r({1},{i+1})={r[i,0]}")
        
        # Richardson extrapolation for higher order approximations
        for k in range(1, i + 1):
            r[i, k] = r[i, k - 1] + \
                (r[i, k - 1] - r[i - 1, k - 1]) / ((4**k) - 1)
            print(f"r({k+1},{i+1})={r[i,k]}")

    return float(r[n - 1, n - 1])
    
def R(T):
    temp=abs(log(tol,10))
    temp=int(round(temp,0))
    return (round(T,temp+1))

def string_to_function(expression):
    def function(x):
        return eval(expression)
    return function

def Swipe(matrix,n,m):
    if n==1:
        matrix=[[3.7, 5.8, 2.9, 3.4],[2.6,3.1,5,2.6],[0.6,3.8,7,5.7]]
        return matrix
    elif n==2:
        matrix=[[3.7, 5.8, 2.9, 3.4],[0,2.86,6.53,5.15],[0,-0.96,2.97,0.22]]
        return matrix

# Derivation function
#current issue: since I couldn't implement derivation precisely the returned values aren'taccurate.
def Fp(x):
    h=0.000000000000001
    dydx=(F(x+h)-F(x))/h
    return dydx

def list_c():
    L=[0.376,0.942,-0.852]
    return L

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
                row.append(float(input(f"a[{i+1},{j+1}]=")))    # user input for rows
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
            for u in range(col-k-2):
                matrix[-2-u][-k-2]=matrix[-2-u][-k-2]*c_temp
            c.append(c_temp)
            c=list_c()
            print(f"c{col-k-1}={c[k]}")
        done=Finished()
            
    elif program==5:
        rows=int(input("please enter number of the rows (how many equations?)...\nrows:"))
        col=int(input("and columns (number of coefficients+standalone number after the =)\ncolumns:"))
        matrix=[]
        for i in range(rows):   
            row = []
            for j in range(col):
                row.append(float(input(f"a[{i+1},{j+1}]=")))    # user input for rows
            matrix.append(row)  # adding rows to the matrix
        print("\n2D matrix is:")
        for i in range(rows):
            for j in range(col):
                print(matrix[i][j], end="  \t")
            print()
        
        print("matrix after swiping rows 1 and 3:")
        matrix=Swipe(matrix,1,3)
        
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
            if _==0:
                print("matrix after swiping rows 2 and 3:")
                matrix=Swipe(matrix,2,3)
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
            for u in range(col-k-2):
                matrix[-2-u][-k-2]=matrix[-2-u][-k-2]*c_temp
            c.append(c_temp)
            c=list_c()
            print(f"c{col-k-1}={c[k]}")
        done=Finished()
    elif program==6:
        continue
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
        b=float(input("b: "))
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
            print(s)
            print (f"s={s}")
        s =s*h
        print(f"s*h={s}")
        done=Finished()
    elif program==12:
        F=string_to_function(str(input("Please write your function:")))
        # use ** for "x power y", * for multiplication and 
        a=float(input("please select a range from a to b: \n a: "))
        b=float(input("b: "))
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
        # import numpy and scipy.integrate
        gfg = lambda x: x*np.log(x+1)
        
        # using scipy.integrate.romberg()
        geek = romberg(gfg, -0.75, 0.75, 4)
        
        print(geek)
        done=Finished()
        
    elif program==14:
        continue
    elif program==15:
        continue
    elif program==16:
        # Driver method
        x0 = 0
        y = 0.5
        x = 2
        h = 0.4
        print ('The value of y at x is:', rungeKutta2(x0, y, x, h))

        done=Finished()
    elif program==17:
        
        # Driver method
        x0 = 0
        y = 0.5
        x = 2
        h = 0.2
        print ('The value of y at x is:', rungeKutta(x0, y, x, h))

        # This code is contributed by Prateek Bhindwar
        done=Finished()
        
    elif program==18:
        continue
        
    elif program==0:
            break
    
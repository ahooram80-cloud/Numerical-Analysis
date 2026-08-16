from math import *
y=2.0
i=0
n=4
print(f"f{i}=\t\t{y}")
# print(f"f*{i}=\t\t-")
ye=((2+(0)*0.25)-2+(2**0.5)*exp(-((2+(0)*0.25)/2)+1))**2
print(f"y({i})=\t\t{ye}")
print(f"f{i}-ye{i}=\t\t{y-ye}")
for i in range(n):
    # y1=y+0.25*(-y+(2+i*(0.25))*(y**(0.5)))
    # print(f"y{i}={-y+(2+i*(0.25))*(y**(0.5))} and {-y1+(2+(i+1)*(0.25))*(y1**(0.5))}")
    y=y+0.25*((-y+(2+i*(0.25))*(y**(0.5))))
    ye=((2+(i+1)*0.25)-2+(2**0.5)*exp(-((2+(i+1)*0.25)/2)+1))**2
    print(f"f{i+1}=\t\t{y}")
    # print(f"f*{i+1}=\t\t{y}")
    print(f"y({i+1})=\t\t{ye}")
    print(f"f{i+1}-ye{i+1}=\t\t{y-ye}")





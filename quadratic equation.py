import math
a=int(input("coefficient of x2"))
b=int(input("coefficient of x"))
c=int(input("constant"))
d=b*b-4*a*c
if(d>=0):
    a1=(-b+math.sqrt(d))/2*a
    a2=(-b-math.sqrt(d))/2*a
    print(f"the solutions are {a1} and {a2}")
else:
    print("solutions does not exist")

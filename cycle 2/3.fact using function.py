def fact(b):
    for i in range(b-1,0,-1):
        b=b*i
    print(b)
a=int(input("enter a number"))
fact(a)

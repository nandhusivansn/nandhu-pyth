n=int(input("enter the limit:"))
a=0
b=1
for _ in range(n):
    print(a,end=" ")
    temp=a
    a=b
    b=temp+b




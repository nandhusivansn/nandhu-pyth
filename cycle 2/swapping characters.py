a=input("the first word")
b=input("the second word")
temp=a
a=a[0:1]+b[1:2]+a[2:]
b=b[0:1]+temp[1:2]+b[2:]
print(a+b)


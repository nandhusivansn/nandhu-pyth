a=int(input("first number"))
b=int(input("second number"))
r=1
for i in range(1,min(a, b) + 1):
    if a%i == 0 and b%i == 0:
       r=i 
print(r)


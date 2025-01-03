a=int(input("enter the first number"))
b=int(input("enter the second number"))
i=1
while i==1:
    op=int(input("enter the operation you want to perform 1.add\n 2.substraction \n 3.multiplication \n 4.division"))
    if(op==1):
        sum=a+b
        print(sum)
    elif(op==2):
        difference=a-b
        print(difference)
    elif(op==3):
        product=a*b
        print(product)
    elif(op==4):
        quotient=a/b
        print(quotient)
    else:
        print("error")
    
    
      

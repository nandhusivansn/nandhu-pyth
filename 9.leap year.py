a=int(input("enter the year"))
if(a%100==0):
    if(a%400==0):
        print("it is a leap year")
    else:
        print("it is not a leap year")
else:
    if(a%4==0):
        print("it is a leap year")
    else:
        print("it is not a leap year")
#largest of three numbers
a=input("enter first number")
b=input("second number")
c=input("third number")
if (a>b):
          if (a>c):
                    print ("a is the largest")
          else:
              print("c is largest")
else:
    if(b>c):
        print("b is the largest")
    else:
        print("c is the largest")

year=int(input("enter current year"))
limit=int(input("enter the limit"))
for i in range(year,limit+1):
    if(i%4==0):
        print(i)
    

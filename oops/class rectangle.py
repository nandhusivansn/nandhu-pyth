class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
       area=self.length*self.breadth
       print(f"area of the rectangle is {area}")
        
    def perimeter(self):
        perimeter=2*(self.length+self.breadth)
        print(f"perimeter of the rectangle  is {perimeter}")

    def compare_area(self,other):
        own=self.area()
        other=other.area()
        if own > other:
            print("area of first rectangle is more")
        elif other > own:
            print("area of second rectangle is more")
        else:
            print("area of two rectangles are equal")
    
    
    
length1=int(input("enter the length of the rectangle 1"))
breadth1=int(input("enter the breadth of the rectangle 1"))
rectangle1=rectangle(length1,breadth1)
length2=int(input("enter the length of the rectangle 1"))
breadth2=int(input("enter the breadth of the rectangle 1"))
rectangle2=rectangle(length2,breadth2)

rectangle1.area()
rectangle1.perimeter()
result=rectangle1.compare_area(rectangle2)
print(result)


    

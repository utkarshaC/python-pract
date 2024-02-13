
def AreaofTriangle():
    Height = int(input("Height is "))
    base = int(input("Base is "))
    Area = 0.5 * Height * base
    return Area


def AreaofRectangle():
    l = int(input("Length is "))
    b = int(input("Breadth is "))
    A = l * b
    return A


def AreaofCircle():
    r = int(input("Radius is "))
    Circle = 3.14 * r * r
    return Circle


while True:
    print("Enter 1 for Area of Triangle")
    print("Enter 2 for Area of Rectangle")
    print("Enter 3 for Area of Circle")
    print("Enter 0 to exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 0:
        break
    elif choice == 1:
        result = AreaofTriangle()
        print(f"The area of the triangle is: {result}")
    elif choice == 2:
        result = AreaofRectangle()
        print(f"The area of the rectangle is: {result}")
    elif choice == 3:
        result = AreaofCircle()
        print(f"The area of the circle is: {result}")
    else:
        print("Invalid Choice")

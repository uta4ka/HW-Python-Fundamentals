import math

def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return 0.5 * a * h

def circle_area(r):
    return math.pi * math.pow(r, 2)

while True:
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        result = rectangle_area(a, b)
        print(f"The area of the rectangle is: {result}")
    elif choice == '2':
        a = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        result = triangle_area(a, h)
        print(f"The area of the triangle is: {result}")
    elif choice == '3':
        r = float(input("Enter the radius of the circle: "))
        result = circle_area(r)
        print(f"The area of the circle is: {result}")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
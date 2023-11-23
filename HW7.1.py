#Task1
def find_largest_number(num1, num2):
    """
    Returns the largest of two numbers.

    Args:
    num1 (float or int): The first number.
    num2 (float or int): The second number.

    Returns:
    float or int: The largest of the two numbers.
    """
    return max(num1, num2)




#Task2import math
def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius**2

choice = input("Enter the shape (rectangle, triangle, or circle): ")

if choice == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")
elif choice == "triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = calculate_triangle_area(base, height)
    print(f"The area of the triangle is: {area}")
elif choice == "circle":
    radius = float(input("Enter the radius: "))
    area = calculate_circle_area(radius)
    print(f"The area of the circle is: {area}")
else:
    print("Invalid choice. Please choose from rectangle, triangle, or circle.")


    

    #Task3
def count_characters(input_string):
    """
    Calculates the number of characters included in the given string.

    Args:
    input_string (str): The input string.

    Returns:
    dict: A dictionary containing character counts.
    """
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

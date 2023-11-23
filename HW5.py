#Task1
integer_list = [1, 2, 3, 4, 5]

float_list = [float(num) for num in integer_list]

print(float_list)

#Task2
n = int(input("Enter a number 'n': "))

a, b = 0, 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b

#Task3
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")
# Q5: Function to find the maximum of three numbers

def maximum_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

print("Maximum number =", maximum_of_three(num1, num2, num3))

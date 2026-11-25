# Q3: Display face values, place values, and reverse a 4-digit number

number = int(input("Enter a 4-digit number: "))

if 1000 <= number <= 9999:
    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    ones = number % 10

    # a. Face value of each digit
    print("Face values:", thousands, hundreds, tens, ones)

    # b. Place value of each digit
    print("Place values:", thousands * 1000, "+",
          hundreds * 100, "+", tens * 10, "+", ones)

    # c. Reverse the digits
    reverse = ones * 1000 + tens * 100 + hundreds * 10 + thousands
    print("Number in reverse order =", reverse)
else:
    print("Please enter a valid 4-digit number.")

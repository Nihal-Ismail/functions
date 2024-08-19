#1

# i = int(7**35)
# a =(str(i))
# print(a [-1:])

#2

# r = 987654321 % 123456789
# print(r)

#4

# a=2 ** (2 - 2) -( 2 / 2)
# print(a)

#5

# a = 0 == 0 < 1 < 2 < 3 > 2 > 1 > 0 == 0
# print(a)

#6


# s = "hello"
# n = len(s)
#
# total_characters = n * n
#
# print("The total number of characters in n * s is:", total_characters)


#7

# x = "Hello"
# y = "World"
#
#
# result = len(x) + len(y) == len(x + y)
# print("The outcome of the expression is:", result)

#10

# var= str(7**100)
#
# x=len(var)
#
# print(x)

#11

# x = str(input("Enter a positive integer: "))
# y=0
# z=x+y
# print(z)

#12

# x=int(input("Enter the length:"))
# y=int(input("Enter the breadth:"))
#
# a=x*y
#
# print(f"The area of Rectangle is:{a}")

#13

# import math
#
#
# x = float(input("Enter a positive real number: "))
#
# greatest_integer = math.floor(x)
#
# print(f"The greatest integer less than or equal to,{x}, is:,{greatest_integer}")

#14

# import math
#
#
# x = float(input("Enter a positive real number: "))
#
# greatest_integer = math.ceil(x)
#
# print(f"The smallest integer greater than or equal to,{x}, is:,{greatest_integer}")


#16


number = int(input("Enter a two-digit number: "))


if 10 <= number <= 99:

    tens = number // 10
    units = number % 10

    digit_sum = tens + units

    print("The sum of the digits is:", digit_sum)
else:
    print("Please enter a valid two-digit number.")


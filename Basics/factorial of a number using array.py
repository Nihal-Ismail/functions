# Factorial Calculation Using an Array (List)

# Prompt the user for a number
number = int(input("Enter a non-negative integer to calculate its factorial: "))

# Initialize an array (list) to store the factorial values
factorial_array = []

# Calculate the factorial
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Initialize the first factorial value
    factorial_array.append(1)  # 0! = 1

    # Calculate factorial using a loop
    for i in range(1, number + 1):
        factorial_array.append(factorial_array[i - 1] * i)

    # The last element in the array is the factorial of the number
    factorial_result = factorial_array[number]

    # Output the result
    print(f"The factorial of {number} is {factorial_result}.")
gvg

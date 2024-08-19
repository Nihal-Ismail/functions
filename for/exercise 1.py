# Program to print the specified pattern

# Set the number of rows for the pattern
rows = 5

# Loop through the range from rows to 0
for i in range(rows, 0, -1):
    # Print numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=' ')
    # Move to the next line after each row
    print()




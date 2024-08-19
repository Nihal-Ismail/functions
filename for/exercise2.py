# Sum of even numbers between 1 and 20 using a for loop
total = 0
for num in range(2, 21, 2):
    total += num
print("Sum of even numbers between 1 and 20 using a for loop:", total)


# Sum of even numbers between 1 and 20 using a while loop
total = 0
num = 2
while num <= 20:
    total += num
    num += 2
print("Sum of even numbers between 1 and 20 using a while loop:", total)
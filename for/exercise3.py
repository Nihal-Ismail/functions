# Given dice results
dice_result = [5, 6, 4, 2, 5, 4, 4, 5, 3, 3, 2, 6, 1, 2, 1, 1, 6, 5]

# Initialize counters
count_6s = 0
count_1s = 0
count_6s_two_in_a_row = 0

# Iterate through the dice results
for i in range(len(dice_result)):
    # Count the number of 6s
    if dice_result[i] == 6:
        count_6s += 1

    # Count the number of 1s
    if dice_result[i] == 1:
        count_1s += 1

    # Count the occurrences of 6s two times in a row
    if i > 0 and dice_result[i] == 6 and dice_result[i - 1] == 6:
        count_6s_two_in_a_row += 1

# Print the results
print("Number of times 6s were rolled:", count_6s)
print("Number of times 1s were rolled:", count_1s)
print("Number of times 6s were rolled two times in a row:", count_6s_two_in_a_row)
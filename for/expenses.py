expenses = [1200, 1500, 1800, 900]

# for exc in expenses:
#     print(exc)
total_expense = 0
# for i in range(len(expenses)):
#     expense = expenses[i]
#     print(f"Month {i+1},Expense:{expense}")
#     total_expense += expense

    #using enumerate another like range
for i,expense in enumerate(expenses):
    print(f"Month {i + 1},Expense:{expense}")
    total_expense += expense


print("Total Expense",total_expense)

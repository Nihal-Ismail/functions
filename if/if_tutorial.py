# n = input("Enter a number:")
# n = int(n)
#
# if n % 2 == 0:
#     print("Number is Even")
# else:
#     print("Number Is odd")
#
# message = "Number is Even" if n % 2 == 0 else "Number is odd"
# print(message)

    #if Condition

indian = ["samosa","vada","chutney"]
chinese = ["egg roll","noodles","fried rice"]
italian = ["pizza","pasta","rizzoto"]

dish = input("Enter a dish name:")

if dish in indian:
    print(f"{dish} is indian")
elif dish in chinese:
    print(f"{dish} is chinese")
elif dish in italian:
    print(f"{dish} is italian")
else:
    print("I dont know which cuisine is this!")

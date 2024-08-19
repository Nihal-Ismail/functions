India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

ff = input("Enter 1st City Name:")
gg = input("Enter 2nd City Name:")

if ff and gg in India:
    print(f"{ff} and {gg} is in India")
elif ff and gg in USA:
    print(f"{ff} and {gg} is in USA")
elif ff and gg in UK:
    print(f"{ff} and {gg} is in UK")
else:
    print("I don't know where these cities are Located!")

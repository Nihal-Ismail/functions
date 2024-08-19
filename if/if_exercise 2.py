India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

ff = input("Enter a city name:")
if ff in India:
    print(f"{ff} is in India")
elif ff in USA:
    print(f"{ff} is in USA")
elif ff in UK:
    print(f"{ff} is in UK")
else:
    print("I don't know where the city is!")

locations = ["chair", "sofa", "table", "wardrobe"]

key_location = "table"

for i in locations:
    if i == key_location:
        print("key is found at",i)
        break
    else:
        print("Key is not found at", i)

total_pushups = 0

while total_pushups < 50:
    for i in range(10):
        print(f"Push-up {total_pushups + i + 1}")

    total_pushups += 10

    if total_pushups >= 50:
        print("Congratulations! You made it")
        break

    tired = input("Are you tired? (yes/no) ").lower()

    if tired in ["yes", "y"]:
        print(f"You did a total of {total_pushups} push-ups")
        break

    remaining_pushups = 50 - total_pushups
    print(f"{remaining_pushups} push-ups remaining")
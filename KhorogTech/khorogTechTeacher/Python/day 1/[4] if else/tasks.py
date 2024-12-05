# 1. Ask user a color and check if it is red, say stop, yellow wait, green go
choice = input("User color: ")

if choice == "green":
    print("Go...")
elif choice == "red":
    print("STOP!!! ")
elif choice == "yellow":
    print("Wait...")
else:
    print("There is not color like that...")
    
# 2. Check the day based on number
user_day = int(input("Type number from 1 to 7"))

if user_day == 1:
    print("Monday")
elif user_day == 2:
    print("Tuesday")
elif user_day == 3:
    print("Wednesday")
elif user_day == 4:
    print("Thursday")
elif user_day == 5:
    print("Friday")
elif user_day == 6 or user_day == 7:
    print("Today is weekend")
else:
    print("There is not day like that...")
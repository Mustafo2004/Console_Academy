import random

# Jerry's initial hiding place
jerry_place = random.randint(1, 5)

print("Tom needs to find Jerry! You have 3 chances.")
print("Jerry is hiding in one of the places numbered 1 to 5.")

# Tom has 3 chances to find Jerry
for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt}: Guess where Jerry is (1-5): "))
    
    if guess == jerry_place:
        print("Tom found Jerry! You win!")
        break
    else:
        print("Jerry is not there!")
        jerry_place = random.randint(1, 5)

if guess != jerry_place:
    print("Tom couldn't find Jerry. You lose!")

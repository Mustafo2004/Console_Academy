# 1. Count from 10 - 100
for i in range(1, 101):
    print(i)
    
# 2. Count from 500 - 700 with 2 step
for i in range(500, 701, 2):
    print(i)

# 3. Count from 50 - 20
for i in range(50, 19, -1):
    print(i)
    
# 4. Count from 100 to 10 with 5 step
for i in range(100, 9, -5):
    print(i)
    
# 5. Print every element in a list with for loop
names = ["Alisher", "Lali", "Umed", "Farahnoz"]

for each in names:
    print(names)
    
# 6. Find the average of the numbers in the following list
nums = [31, 63, 86, 27, 92] 
sum = 0

for each in nums:
    sum = sum + each

print(sum)

# 7. Ask user 5 cars names with for loop and save them in a list
cars = []

for i in range(5):
    new_car = input("New car name:")
    cars.append(new_car)

print(cars)
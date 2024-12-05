# Count from 1 to 50
for i in range(1, 51):
    print(i)
# Count from 200 to 300 with step of 5
for i in range(200, 301, 5):
    print(i)
# Count from 100 to 50
for i in range(100, 49, -1):
    print(i)
# Count from 150 to 50 with step of 10
for i in range(150, 49, -10):
    print(i)
# Print each element in a list with a for loop
fruits = ["Apple", "Banana", "Cherry", "Date"]

for fruit in fruits:
    print(fruit)
#  Find the sum of the numbers in the following list and devide at to 5 and plus it to 8
numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total += number

print(total)

# Ask user for 3 favorite movies and save them in a list
movies = []

for i in range(3):
    movie = input("Enter the name of a favorite movie: ")
    movies.append(movie)

print(movies)
# Count the number of vowels in a given string
string = "Hello, how are you?"
vowels = "aeiou"
count = 0

for char in string:
    if char.lower() in vowels:
        count += 1

print("Number of vowels:", count)
# Print the squares of numbers from 1 to 10
for i in range(1, 11):
    print(i ** 2)

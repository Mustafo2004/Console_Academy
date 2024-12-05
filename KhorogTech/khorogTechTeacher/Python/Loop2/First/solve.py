
# ! 1
n = int(input("Введите число: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(f"{i} - четное")
    else:
        print(f"{i} - нечетное")

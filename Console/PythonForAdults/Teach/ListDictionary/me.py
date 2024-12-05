menu = []

# Добавление первого блюда в menu
first_dish = {
    "na": "Суп Минестроне",
    "price": 250,
    "chied": {
        "name": "Иван Иванов",
        "re": 4.5
    }
}
menu.append(first_dish)

# Добавление второго блюда в меню
second_dish = {
    "na": "Суп Минестроне",
    "price": 250,
    "chied": {
        "name": "Иван Иванов",
        "re": 4.5
    }
}
print(menu)
mwww = menu[0]["na"]
menu.pop(mwww)
print(mwww)
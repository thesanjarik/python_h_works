import random

secret_number = 0
x = random.randint(1, 100)
counter = 0
print(" Попробуй отгадать загаданное число ")
print(" Как тебя зовут: ")
player = input()
print(player)
while secret_number != x:
    secret_number = int(input(str(player) + " Введите число:\n "))
    counter = counter + 1
    if secret_number > x:
        print(" Число должно быть меньше ")
    elif secret_number < x:
        print(" Число должно быть больше ")
    else:
        print(" Вы угадали загаданное число за " + str(counter) + " попыток ")
        break










































































































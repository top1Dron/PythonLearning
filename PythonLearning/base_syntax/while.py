number = 23
running = True
while running:
    guess = int(input('Введите целое число : '))

    if guess == number:
        print('Позравляю, вы угадали')
        running = False
    elif guess < number:
        print('Ваше число чуть меньше загаданного')
    else:
        print('Ваше число чуть больше загаданного')
else:
    print("Завершено")
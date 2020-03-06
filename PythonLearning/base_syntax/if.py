number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('Позравляю, вы угадали')
elif guess < number:
    print('Ваше число чуть меньше загаданного')
else:
    print('Ваше число чуть больше загаданного')
print("Завершено")

flag = True
while flag:
    s = input('Enter something: ')
    if s == 'exit':
        break
    if s == 'Exit':
        flag = False
    print('String lenght:', len(s))
else:
    print("End of while.")
print('End')

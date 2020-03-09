try:
    text = input('Enter something ')
except EOFError:
    print('EOFError')
except KeyboardInterrupt:
    print('Operation cancelled')
else:
    print('You entered {0}'.format(text))

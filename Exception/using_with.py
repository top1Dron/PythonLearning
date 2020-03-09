try:
    with open("poem.txt") as f:
        for line in f:
            print(line, end='')
except FileNotFoundError:
    print('Error 404: File not found!')

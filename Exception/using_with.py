try:
    with open("poem.txt") as f:
        for line in f:
            print(line, end='')
except FileNotFoundError:
    print('Eror 404: File not found!')
import time

try:
    f = None
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('You cancelled reading file')
except FileNotFoundError:
    print('Eror 404: File not found!')
finally:
    if f is not None:
        f.close()
    print('Cleaning: Closing file!')

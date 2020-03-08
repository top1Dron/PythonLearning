poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей веселый тон - 
    используй Python!
'''

f = open('poem.txt', 'w')  # opening for writing

f.write(poem)  # writing poem to file
f.close()  # closing file

f = open('poem.txt')

while True:
    line = f.readline()
    if len(line) == 0:  # empty line means file end
        break
    print(line, end='')
f.close()

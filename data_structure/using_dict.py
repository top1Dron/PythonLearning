ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's address:", ab['Swaroop'])
del ab['Spammer']
print('Address book have {}'.format(len(ab)) + ' contacts')
for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))
ab['Guido'] = 'guido@python.com'

if 'Guido' in ab:
    print("Guido's address is", ab['Guido'])

zoo = ('питон', 'слон', 'пингвин')
print('Количество животных в зоопарке -', len(zoo))
newZoo = ('обезьяна', 'верблюд', zoo)
print('Amount of animals in new zoo - ', len(newZoo))
print('All animals in new zoo', newZoo)
print('All animals from old zoo', newZoo[2])
print('Last animal from the old zoo - ', newZoo[2][2])
print('All amount of animals in new zoo - ', len(newZoo) - 1 + len(newZoo[2]))
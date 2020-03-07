# Это мой список покупок
shopList = ['яблоки', 'манго', 'морковь', 'бананы']
print('Я должен сделать', len(shopList), 'покупок.')
print('Покупки:', end=' ')
for item in shopList:
    print(item, end=' ')
print('\nТакже нужно купить риса.')
shopList.append('рис')
print('Теперь мой список покупок таков:', shopList)
print('Отсортирую-ка я свой список')
shopList.sort()
print('Отсортированный список покупок выглядит так:', shopList)
print('Первое, что мне нужно купить, это', shopList[0])
oldItem = shopLi

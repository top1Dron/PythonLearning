import pickle

# file name where we will save an object
shopListFile = 'shopList.data'

# shop list
shopList = ['apples', 'mango', 'carrot']

# file writing
f = open(shopListFile, 'wb')
pickle.dump(shopList, f)  # throw the object shopList to file
f.close()

del shopList  # deleting shopList

# reading from file
f = open(shopListFile, 'rb')
storedList = pickle.load(f)  # loading object from file
print(storedList)

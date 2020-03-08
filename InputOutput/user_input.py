def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


symbols = (',', '\\', ';', ' ', '+', '-', '=', '?', '!', ':', '(', ')', '[', ']', '...', "'", '/')

something = input('Enter text: ')
formattedString = something[::]
for symbol in symbols:
    formattedString = formattedString.replace(symbol, '')
formattedString = formattedString.lower()

print(formattedString)
if is_palindrome(formattedString):
    print("It's palindrome")
else:
    print("It's not palindrome")

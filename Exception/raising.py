class ShortInputException(Exception):
    """User Exception class"""

    def __init__(self, length, atLeast):
        Exception.__init__(self)
        self.length = length
        self.atLeast = atLeast


try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # some code
except EOFError:
    print("Why are u give me EOF?")
except ShortInputException as ex:
    print('ShortInputException: Length of your string - {}\n'
          'Minimum length - {}'.format(ex.length, ex.atLeast))
else:
    print('Everything OK!')

import sys

print("Command line arguments:")
for i in sys.argv:
    print(i)

print('\n\nVariable PYTHONPATH includes ', sys.path, '\n')

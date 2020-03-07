import os
import time


def docFunction():
    """This program creates restore point for Windows

    """


__version__ = 1.0
print(docFunction.__doc__)
default = 'WMIC /Namespace:\\\\root\\default Path SystemRestore Call CreateRestorePoint "RestorePoint", 100, 7'
os.system(default)

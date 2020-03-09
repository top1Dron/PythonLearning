import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn("For execution this program you need at least the 3rd version of Python",
                  RuntimeWarning)
else:
    print('Ok!')
import os
import time

__version__ = 1.0

# files and packages will be in list
source = ['"D:\\мемы"']

# backup dir
targetDir = '"D:\\BackUpPython"'

# all files parse to zip with date name
target = targetDir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {} {}".format(target, ' '.join(source))

# start creating back up
if os.system(zip_command) == 0:
    print('Backup zip file created in directory:', target)
else:
    print('Backup failed.')

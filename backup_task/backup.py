import os
import time

__version__ = 1.0

# files and packages will be in list
source = ['"D:\\мемы"']

# backup dir
targetDir = 'D:\\BackUpPython'

# current date as subpackage in main package
today = targetDir + os.sep + time.strftime('%Y%m%d')
# current time as a name for zip file
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)  # creating subpackage for keeping backup
    print("Subpackage created!")

# all files parse to zip with datetime name
target = today + os.sep + now + '.zip'

# zip command in command line for creating backup zip file
zip_command = "zip -qr {} {}".format(target, ' '.join(source))

# start creating back up
if os.system(zip_command) == 0:
    print('Backup zip file created in directory:', target)
else:
    print('Backup failed.')

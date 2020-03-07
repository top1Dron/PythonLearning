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

comment = input('Enter comment --> ')

# all files parse to zip with datetime name
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)  # creating subpackage for keeping backup
    print("Subpackage created!")

# zip command in command line for creating backup zip file
zip_command = "zip -qr {} {}".format(target, ' '.join(source))

# start creating back up
if os.system(zip_command) == 0:
    print('Backup zip file created in directory:', target)
else:
    print('Backup failed.')

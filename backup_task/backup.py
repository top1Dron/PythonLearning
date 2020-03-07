import os
import time
import zipfile

__version__ = 4.0

# files and packages will be in list
source = ['D:\\мемы\\', 'D:\\random files\\']

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
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)  # creating subpackage for keeping backup
    print("Subpackage created!")

# creating new zip file
with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as newZip:
    # start creating back up
    for directory in source:
        # list of all files, folders in targetDir folder
        for root, dirs, files in os.walk(directory):
            for file in files:
                newZip.write(os.path.join(root, file))
                print('File ' + file + ' added to zip successfully')
print('Backup zip file created in directory:', target)

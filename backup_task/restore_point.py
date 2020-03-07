import os
import pyriodic


def createRestorePoint():
    """This program creates restore point for Windows

    """
    __version__ = 1.0
    print(createRestorePoint.__doc__)
    default = 'WMIC /Namespace:\\\\root\\default Path SystemRestore Call CreateRestorePoint "RestorePoint", 100, 7'
    os.system(default)


task = pyriodic.Scheduler()
task.add_job(pyriodic.DatetimesJob(
    createRestorePoint,
    when='7:40 pm',
    interval='daily'
))

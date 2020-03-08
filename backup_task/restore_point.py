import os


# from pyriodic import Scheduler, DatetimesJob


def createRestorePoint():
    """This program creates restore point for Windows

    """
    __version__ = 1.0
    print(createRestorePoint.__doc__)
    default = 'WMIC /Namespace:\\\\root\\default Path SystemRestore Call CreateRestorePoint "RestorePoint", 100, 7'
    os.system(default)


createRestorePoint()
# task = Scheduler()
# print(task.add_job(DatetimesJob(
#     createRestorePoint,
#     when='07:00 pm',
#     interval='daily',
#     name='restore point'
# )))
#
# print(task.next_run_times())

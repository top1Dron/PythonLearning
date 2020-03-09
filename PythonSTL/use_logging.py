import os, platform, logging

if platform.platform().startswith('Windows'):
    loggingFile = os.path.join(os.getenv('HOMEDRIVE'),
                               os.getenv('HOMEPATH'),
                               'test.log')
else:
    loggingFile = os.path.join(os.getenv('HOME'), 'test.log')

print("Saving log into", loggingFile)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=loggingFile,
    filemode='w'
)

logging.debug("Program starts")
logging.info("Some things")
logging.warning("Program dies")
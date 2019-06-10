import logging
from time import localtime, strftime

def setuplog(path = 'log.txt'):
    logging.basicConfig(filename=strftime(path, localtime()),level=logging.DEBUG)

def log(message, severity = logging.DEBUG):
    message = strftime("(%Y-%m-%d %H:%M:%S) ", localtime()) + message
    print(message)
    logging.debug(message)

def stopmsg():
    message = strftime("Stopped at (%Y-%m-%d %H:%M) ", localtime())
    print(message)
    logging.debug(message)

    

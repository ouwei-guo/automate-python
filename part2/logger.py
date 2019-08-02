# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:20:51 2019

@author: GuoOu

Don’t Debug with print()!!!

DEBUG log.debug()
INFO log.info()
WARNING log.warning()
ERROR log.error()
CRITICAL log.critical()

"""

import logging

# create logger with 'spam_application'
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('mylog.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


def factorial(n):
    logger.debug('Start of factorial(%s)' % n)
    total = 1
    for i in range(n + 1):
        total *= i
        logger.debug('i is ' + str(i) + ', total is ' + str(total))
    logger.debug('End of factorial(%s)' % n)
    return total

print(factorial(5))
logger.debug('End of program')







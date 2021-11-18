
import logging

#　打印日志级别
def test_logging():
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')

#test_logging()

#　打印日志级别
def test():
    logging.basicConfig(filename="log.log",format="%(pathname)s %(asctime)s %(funcName)s %(message)s",level=logging.DEBUG)
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')
    logging.log(2,'test')

#test()

import object

def main():
    car = object.Car("GO")
    logging.basicConfig(filename='log.log',format="%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p",level=logging.DEBUG)
    logging.info('Started')
    car.GuessCharge()
    logging.info("car.GuessCharge() called")
    logging.info('Finished')

#main()

#config logging 
# create logger
logger = logging.getLogger('python built-in logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
#ch = logging.StreamHandler()
ch = logging.FileHandler("log.log")
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

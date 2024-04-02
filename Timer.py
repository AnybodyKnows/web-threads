from threading import Timer
import logging
from time import sleep


def worker():
    logging.debug('Start!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

    first = Timer(0.5, worker)
    first.name = 'First thread'
    second = Timer(0.7, worker)
    second.name = 'Second thread'
    logging.debug('Start timers')
    first.start()
    second.start()
    sleep(0.6)  # if value more than 0.7 (value in second thread) in would not be executed)
    second.cancel()

    logging.debug('End program')

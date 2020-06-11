import logging
import os
from datetime import datetime

from Util.tool import tool

log_path = os.path.join(tool.getBaseDir(), "log")


class Logger:
    def __init__(self, loggername):
        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(logging.DEBUG)

        logname = log_path + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + "out.log"
        fh = logging.FileHandler(logname, encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger

    def setDebugLog(self, msg):
        self.logger.debug(msg)

    def setInfoLog(self, msg):
        self.logger.info(msg)

    def setCriticalLog(self, msg):
        self.logger.critical(msg)



# if __name__ == '__main__':
#     log = Logger(__name__).setCriticalLog("ffffff")

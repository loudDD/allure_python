import logging
import os
from datetime import datetime

from Util.tool import tool

log_path = os.path.join(tool.getBaseDir(), "log")


class logger:

    def __init__(self, loglevel=logging.DEBUG):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logLevel = loglevel

        logfilename = log_path + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + "out.log"
        fh = logging.FileHandler(logfilename, encoding="utf-8")
        fh.setLevel(self.logLevel)

        ch = logging.StreamHandler()
        ch.setLevel(self.logLevel)

        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setStream(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def setDebugLog(self, msg):
        self.logger.debug(msg)

    def setInfoLog(self, msg):
        self.logger.info(msg)

    def setCriticalLog(self, msg):
        self.logger.critical(msg)

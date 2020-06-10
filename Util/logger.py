import logging
import os

from Util.tool import tool

log_path = os.path.join(tool.getBaseDir(), "log")

class logger:

    def __init__(self,loggerName):
        self.logger = logging.getLogger(loggerName)


import os


class tool:

    @staticmethod
    def getBaseDir():
        return os.path.dirname(os.getcwd())
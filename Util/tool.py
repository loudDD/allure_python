import os


class tool:

    @staticmethod
    def getBaseDir(self):
        return os.path.dirname(os.getcwd())

import platform

class SystemUtil:

    @staticmethod
    def fetchOS():
        if (platform.system()== 'Linux'):
            return 'L'
        elif (platform.system()== 'Windows'):
            return 'W'
        else:
            return 'M'


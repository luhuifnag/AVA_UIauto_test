import unittest

class Status(unittest.TestCase):


    # status = 136 #当值为0时设备为云台设备，当值为1时，设备为云镜设备

    def test_get_status(self):
        status = 0
        if "你好"=="dada":
            return (status = 0)
        else:
            print("断言错误")
            status = 1
    print (status)


        


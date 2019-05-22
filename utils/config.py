"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import os
from utils.file_reader import YamlReader

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # os.path.dirname(os.path.abspath(__file__) 这里首先得到文件所处的绝对路径，然后得到前面的目录；
                                                                          # 照路径将文件名和路径分割开os.path.split('PATH')
                                                                          # 1.PATH指一个文件的全路径作为参数：
                                                                          # 2.如果给出的是一个目录和文件名，则输出路径和文件名
                                                                          # 3.如果给出的是一个目录名，则输出路径和为空文件名
DATA_PATH = os.path.join(BASE_PATH, 'data')               # 连接两个或更多的路径名组件
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')


class Config:
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)


if __name__ == '__main__':
    c = Config()
    print(c.get('URL'))
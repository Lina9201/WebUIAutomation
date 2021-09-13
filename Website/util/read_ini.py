import os
import configparser
class ReadIni(object):
    def get_value(self, key):
        curpath = os.path.abspath(os.path.join(os.getcwd(), "../../config"))
        cfgpath = os.path.join(curpath, 'LocalElement.ini')
        print(cfgpath)
        # 创建管理对象
        conf = configparser.ConfigParser()

        # 读ini文件
        conf.read(cfgpath)

        # 获取所有的section
        sections = conf.sections()

        print(sections)



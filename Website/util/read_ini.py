import os
import configparser


class ReadIni:

    def get_value(self, section, key):
        curpath = os.path.abspath(os.path.join(os.getcwd(), "../config"))
        cfgpath = os.path.join(curpath, 'LocalElement.ini')
        # 创建管理对象
        conf = configparser.ConfigParser()

        # 读ini文件
        conf.read(cfgpath)

        # 获取所有的section
        sections = conf.sections()
        print(sections)

        # 获取指定section下面的key/value值
        # items = conf.items('LoginElement')
        value = conf[section][key]
        return value


ri = ReadIni()
ReadIni.get_value(ri, 'LoginElement', 'username')

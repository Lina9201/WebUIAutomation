from Website.util.read_ini import ReadIni


class FindElement(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, section, key):
        read_ini = ReadIni()
        data = read_ini.get_value(section, key)
        by = data.split('>')
        print(by)

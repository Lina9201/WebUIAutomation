# -*- encoding: utf-8 -*-
#@Time    :2020/3/6 10:53
#@Author  :shenfeifei

import unittest
from driver.driver import *

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

# -*- encoding: utf-8 -*-
#@Time    :2020/3/26 9:52
#@Author  :shenfeifei

import unittest
from BSTestRunner import BSTestRunner
import time

test_dir = './test_case'

discover = unittest.defaultTestLoader.discover(test_dir , pattern= "test*.py")

if __name__ == '__main__':
    report_dir = './test_report'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir + '/' + now + 'result.html'

    with open(report_name , 'wb') as f:
        runner = BSTestRunner(stream=f , title="Test Report", description="TCRC test" )
        runner.run(discover)

    f.close()




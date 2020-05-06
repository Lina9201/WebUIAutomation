# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 15:04
# @Author  : zhuxuefei
from Website.test_case.page_object.TenantPage import *
from Website.test_case.model import function,myunit
import unittest
from time import sleep

class CreateTenant(myunit.StartEnd):
    def test_createTenant_normal(self):
        print("test_createTenant_normal is start test")
        po = TenantPage(self.driver)
        po.create_Tenant("zuhu")
        self.assertEqual(po.type_createTenPass_hint(), '创建成功')
        function.insert_img(self.driver, "createTenantPass.jpg")
        print("test_createTenant_normal test end!")

if __name__ == '__main__':
    unittest.main()
# -*- encoding: utf-8 -*-
#@Time    :2020/3/23 9:36
#@Author  :shenfeifei

from Website.pagemanager.UsersPage import *
from Website.test_case.model import function,myunit
import unittest
from time import sleep

class CreateOrganization(myunit.StartEnd):
    def test_createOrg_normal(self):
        print("test_createOrg_normal is start test")
        po = UsersPage(self.driver)
        po.create_organization("test_org21")
        sleep(1)
        self.assertEqual(po.type_createOrgPass_hint(), '添加成功')
        function.insert_img(self.driver , "createOrgPass.jpg")
        print("test_createOrg_normal test end!")

    def test_createOrg_repeat(self):
        print("test_createOrg_repeat is start test")
        po = UsersPage(self.driver)
        po.create_organization("test_org21")
        sleep(1)
        self.assertEqual(po.type_createOrgRepeat_hint(),"组织名称不能重复")
        function.insert_img(self.driver , "createOrgRepeat.jpg")
        print("test_createOrg_repeat test end!")

    def test_createOrg_ver(self):
        print("test_createOrg_ver is start test")
        po = UsersPage(self.driver)
        po.create_organization("_@")
        self.assertEqual(po.type_createOrgVer_hint(),'由40个字母、数字、中文、下划线、横线组成（且不能以下划线、横线开头')
        function.insert_img(self.driver , "createOrgVer.jpg")
        print("test_createOrg_ver test end!")




if __name__ == '__main__':
    unittest.main()
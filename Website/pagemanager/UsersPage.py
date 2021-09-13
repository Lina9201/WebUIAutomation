# -*- encoding: utf-8 -*-
#@Time    :2020/3/20 16:01
#@Author  :shenfeifei

from Website.pagemanager.BasePage import *
from selenium.webdriver.common.by import By

class UsersPage(Page):
    url = "/setting/userManage/organizations/"

    #定位器
    rootBtn_loc = (By.XPATH , '//a[@class="rootBtn"]')
    organizationName_loc = (By.XPATH , '//*[@class ="el-input" ]/input[@class= "el-input__inner"]')
    organizationSubmiit_loc = (By.XPATH , '//button[@class="el-button el-button--default el-button--small el-button--primary "]')


    def type_rootBton(self):
        self.find_element(*self.rootBtn_loc).click()

    def type_organizationName(self , organizationname):
        self.find_element(*self.organizationName_loc).clear()
        self.find_element(*self.organizationName_loc).send_keys(organizationname)

    def type_organizationSubmiit(self):
        self.find_element(*self.organizationSubmiit_loc).click()

    def create_organization(self, organizationname):
        self.open()
        self.type_rootBton()
        self.type_organizationName(organizationname)
        self.type_organizationSubmiit()

    createOrgPass_loc = (By.XPATH , '//p[contains(text(),"添加成功")]')
    createOrgRepeat_loc = (By.XPATH , '//p[contains(text(),"组织名称不能重复")]')
    createOrgVer_loc = (By.XPATH , '//div[contains(text(),"由40个字母、数字、中文、下划线、横线组成")]')

    def type_createOrgPass_hint(self):
        return self.find_element(*self.createOrgPass_loc).text

    def type_createOrgRepeat_hint(self):
        return self.find_element(*self.createOrgRepeat_loc).text

    def type_createOrgVer_hint(self):
        return self.find_element(*self.createOrgVer_loc).text





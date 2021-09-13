# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 13:42
# @Author  : zhuxuefei

from Website.pagemanager.BasePage import *
from selenium.webdriver.common.by import By

class TenantPage(Page):
    url = "/tenant/tenant/tenantManage/list"
    createBtn_loc = (By.XPATH, '//*[@class="el-button el-button--primary el-button--mini"]')
    tenantName_loc = (By.XPATH, '//*[@class="el-input__inner"]')
    tenantSubmit_loc = (By.XPATH, '//*[@class="el-button el-button--primary el-button--mini"]')

    def type_rootBton(self):
        self.find_element(*self.createBtn_loc).click()

    def type_tenantName(self, tenantName):
        self.find_element(*self.tenantName_loc).clear()
        self.find_element(*self.tenantName_loc).send_keys(tenantName)

    def type_tenantSubmit(self):
        self.find_element(*self.tenantSubmit_loc).click()

    def create_Tenant(self, tenantName):
        self.open()
        self.type_rootBton()
        self.type_tenantName(tenantName)
        self.type_tenantSubmit()

    createTenPass_loc = (By.XPATH, '//p[contains(text(),"创建成功")]')

    def type_createTenPass_hint(self):
        return self.find_element(*self.createTenPass_loc).text


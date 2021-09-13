from selenium import webdriver
from Website.pagemanager.base_page.find_element import FindElement


class LoginPage(object):

    def __init__(self, driver):
        self.fd = FindElement(driver)

    def get_username_element(self):
        return self.fd.get_element("username")

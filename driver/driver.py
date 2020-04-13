# -*- encoding: utf-8 -*-
#@Time    :2020/3/6 10:02
#@Author  :shenfeifei

from selenium import webdriver

def browser():
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    #driver = webdriver.Ie()

    #driver.get("http://172.23.1.2/console")

    return driver

if __name__ == '__main__':
    browser()
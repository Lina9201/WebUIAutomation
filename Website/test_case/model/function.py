# -*- encoding: utf-8 -*-
#@Time    :2020/3/6 13:59
#@Author  :shenfeifei
import os
from selenium import webdriver
import time

def insert_img(driver , filename):
    func_path = os.path.dirname(__file__)

    base_dir = os.path.dirname(func_path)

    base_dir = str(base_dir)
    base_dir = base_dir.replace("\\" , "/")
    base = base_dir.split('/Website')[0]

    filepath = base + "/Website/test_report/screenshot/" + filename
    driver.get_screenshot_as_file(filepath)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://172.23.1.2/console#/login")
    time.sleep(5)
    insert_img(driver , "TCRC.jpg")
    driver.quit()



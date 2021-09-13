# -*- encoding: utf-8 -*-
#@Time    :2020/3/13 11:07
#@Author  :shenfeifei

from Website.pagemanager.BasePage import *
from driver.driver import browser

def get_token():
    url = "http://172.23.1.2/api/v1/tokens"
    token_param = {
            "authType": "password",
            "params": {
                "username": "zhon",
                "password": "jixlb2tIrjF5t/bYQTXz4Q=="
            }
    }
    header = {"User-Agent": "automation",
               "content-type": "application/json;charset=UTF-8"
               }
    token_response = requests.post(url,json=token_param, headers = header).json()
    return token_response['data']['key']


def login():
    global driver
    driver = browser()
    url = "/home/ops"
    web_open = Page(driver)
    web_open._open(url)

    token = get_token()
    js = 'sessionStorage.setItem("T-AUTH-USER", "6dd3d4e7-1ecb-4f99-93d4-e71ecbcf9990");' \
         'sessionStorage.setItem("x-token", "%s");' \
         'sessionStorage.setItem("T-AUTH-ACCOUNT", "zhon");' \
         'sessionStorage.setItem("T-AUTH-NAME", "zhon");' % token
    driver.execute_script(js)

    web_open._open(url)



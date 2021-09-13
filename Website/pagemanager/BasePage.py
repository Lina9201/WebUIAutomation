# -*- encoding: utf-8 -*-
#@Time    :2020/3/6 17:06
#@Author  :shenfeifei

from time import sleep
import requests
class Page():
    def __init__(self , driver):
        self.driver = driver
        self.base_url = "http://172.23.1.2/console#"
        self.timeout = 10

    def get_token(self):
        api_url = "http://172.23.1.2/api/v1/tokens"
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
        token_response = requests.post(api_url, json=token_param, headers=header).json()
        return token_response['data']['key']

    def _open(self,url):
        url_ = self.base_url + url
        print("Test page is %s" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(10)
        #assert self.driver.current_url == url_ , 'Did not land on %s' %url_

    def open(self):
        self._open(self.url)
        token = self.get_token()
        js = 'sessionStorage.setItem("T-AUTH-USER", "6dd3d4e7-1ecb-4f99-93d4-e71ecbcf9990");' \
             'sessionStorage.setItem("x-token", "%s");' \
             'sessionStorage.setItem("T-AUTH-ACCOUNT", "zhon");' \
             'sessionStorage.setItem("T-AUTH-NAME", "zhon");' % token
        self.driver.execute_script(js)
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
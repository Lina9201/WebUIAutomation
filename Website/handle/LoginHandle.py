from Website.pagemanager.operation_page import LoginPage


class LoginHandle(object):
    def __init__(self, driver):
        self.login_p = LoginPage(driver)

    def send_user_name(self, username):
        self.login_p.get_username_element()

    def send_user_pwd(self):
        pass


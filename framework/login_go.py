# coding= utf-8
import time
from pageobjects.jianshu_loginpge import LoginPage


class LoginGo():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, psw):
        loginpage = LoginPage(self.driver)
        loginpage.type_username(username)
        time.sleep(1)
        loginpage.type_password(psw)
        time.sleep(1)
        loginpage.send_login_btn()
        time.sleep(1)
        loginpage.close_pic()
        time.sleep(1)

    def is_login_success(self):
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print text
            return True
        except:
            return False
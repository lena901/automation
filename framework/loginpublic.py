# coding= utf-8
import time
from pageobjects.jianshu_loginpge import LoginPage


class Login():

    def login(self, username, psw):
        loginpage = LoginPage(self.driver)
        loginpage.type_username(username)
        loginpage.type_password(psw)
        loginpage.send_login_btn()
        time.sleep(2)

    def is_login_success(self):
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print text
            return True
        except:
            return False
# coding=utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):

    username = "id=>session_email_or_mobile_number"
    pw = "id=>session_password"
    login_btn = "class_name=>sign-in-button"
    checkbox_btn = "css_selector=>#session_remember_me"

    def type_username(self, text):
        self.type(self.username, text)

    def type_password(self, text):
        self.type(self.pw, text)

    def send_login_btn(self):
        self.click(self.login_btn)

    def remember_checkbox(self):
        self.click(self.checkbox_btn)

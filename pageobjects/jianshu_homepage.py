
# coding=utf-8
from framework.base_page import BasePage


class HomePage(BasePage):

    input_box = "id=>q"
    search_submit_btn = "class_name=>search-btn"
    # 登录入口
    new_link = "xpath=>/html/body/nav/div/a[4]"

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_login(self):
        self.click(self.new_link)
        self.sleep(2)
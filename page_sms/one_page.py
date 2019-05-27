import sys, os

sys.path.append(os.getcwd())


from base_sms.base_sms import Base
from page_sms.elements_page import Elements


class HomePage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_new_sms_btn(self):
        """点击新建短信"""
        self.click_element(Elements.new_sms_btn_id)

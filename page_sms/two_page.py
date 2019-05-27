import sys, os

sys.path.append(os.getcwd())


from base_sms.base_sms import Base

from base_sms.base_sms import Base
from page_sms.elements_page import Elements


class NewPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def input_rec_phone(self, phone):
        """输入收信人手机号"""
        self.send_element(Elements.rec_phone_id, phone)

    def input_sms_text(self, text):
        self.send_element(Elements.send_text_mes, text)

    def click_send_btn(self):
        self.click_element(Elements.send_btn)
    def get_res(self):
        res = self.get_elements(Elements.send_result_ids)
        return [i.text for i in res]
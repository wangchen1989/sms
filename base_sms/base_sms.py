import sys, os

sys.path.append(os.getcwd())


from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=10, poll_frequency=1.0):
        """定位单个元素"""
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=10, poll_frequency=1.0):
        """定位一组元素"""

        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=20, poll_frequency=1.0):
        """点击元素"""
        self.get_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=20, poll_frequency=1.0):
        """输入文本内容"""
        input_text = self.get_element(loc, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)

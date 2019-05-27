# 作业3：
# 工厂函数
# 返回三条数据[123,hello,word]
# 工厂函数
# 新建短信
# 输入收件人

# 连续发三条 123   hello   world
#
# 断言三条是否都发送成功,,使用的是fixture
import sys, os

sys.path.append(os.getcwd())




import pytest


from base_sms.sms_driver import get_driver
from page_sms.page import Page


@pytest.fixture(params=["123", "hello", "word"])
def get_data(request):
    return request.param


class TestSendMessage:
    driver = None

    def setup_class(self):
        # 驱动浏览器
        self.driver = get_driver('com.android.mms', '.ui.ConversationList')
        self.page = Page(self.driver)
    def teardown_class(self):
        #  退出浏览器
        self.driver.quit()


    @pytest.fixture(scope="class", autouse=True)
    def before_message_page(self):
        # 点击左下角新建按钮进入发短信页面
        self.page.get_home_page_obj().click_new_sms_btn()
        # 输入收信人
        self.page.get_new_page().input_rec_phone("18622221111")
    def test_send_message(self,get_data):
        #  发送内容
        self.page.get_new_page().input_sms_text(get_data)
        #点击发送
        self.page.get_new_page().click_send_btn()
        # 获取发生内容列表

        send_data_list = self.page.get_new_page().get_res()
        # 断言
        assert get_data in send_data_list

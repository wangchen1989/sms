import sys, os

sys.path.append(os.getcwd())


from selenium.webdriver.common.by import By


class Elements:
    """返回所有页面元素"""
    """ 短信首页"""
    # 点击新建短信按钮
    new_sms_btn_id = (By.ID, "com.android.mms:id/action_compose_new")

    """短信编辑页面"""
    # 输入收信人手机号
    rec_phone_id = (By.ID, "com.android.mms:id/recipients_editor")

    # 输入发送内容文本框：
    send_text_mes = (By.ID, "com.android.mms:id/embedded_text_editor")

    # 发送按钮
    send_btn = (By.ID, "com.android.mms:id/send_button_sms")
    # 获取发送内容
    send_result_ids = (By.ID, "com.android.mms:id/text_view")

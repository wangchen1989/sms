import sys, os

sys.path.append(os.getcwd())


from appium import webdriver


def get_driver(pac, act):
    desired_caps = {}
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['platformName'] = "Android"
    desired_caps['platformVersion'] = "5.1"
    desired_caps['deviceName'] = '192.168.140.101:5555'
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 全局

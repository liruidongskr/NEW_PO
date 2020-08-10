from appium import webdriver

# 封装前置代码
def init_driver():
    # server启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.175.101:5555'
    # app信息
    # 包名
    desired_caps['appPackage'] = 'com.android.settings'
    # 启动名
    desired_caps['appActivity'] = '.Settings'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
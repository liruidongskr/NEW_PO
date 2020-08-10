# 导包
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NetworkPage(BaseAction):

    more_button = By.XPATH, "text,更多"
    moveNetwork_button = By.XPATH, "text,移动网络"
    typeNetwork_button = By.XPATH, "text,首选网络类型"
    work2G_button = By.XPATH, "text,2G"
    work3G_button = By.XPATH, "text,3G"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.click_more()

    # 网络设置点击更多
    def click_more(self):
        self.click(self.more_button)

    # 点击移动网络
    def click_move(self):
        self.click(self.moveNetwork_button)

    # 点击首选网络类型
    def click_typeNet(self):
        self.click(self.typeNetwork_button)

    # 点击2G
    def click_2G(self):
        self.click(self.work2G_button)

    # 点击3G
    def click_3G(self):
        self.click(self.work3G_button)
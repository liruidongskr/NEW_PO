# 封装动作- 处理xpath等操作
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def find_element(self, loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(by, value))

    def find_elements(self, loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(by, value))

    # 处理xpath
    def make_xpath_with_unit_feature(self, loc):
        key_index = 0
        value_index = 1
        option_index = 2
        # 接收字符串，并分割
        args = loc.split(",")
        # 判断分割后有几个元素 从1开始
        if len(args) == 2:
            # //*[contains(@text, '设置')] 包含查询
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + " and "
        elif len(args) == 3:
            # 判断第三个元素是否为1 或者0 1表示精准查询 0表示多条件查询
            if args[option_index] == "1":
                # //*[@text='设']
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + " and "
            elif args[option_index] == "0":
                # 多条件查询 //*[@text='设' and contains(@text, '设')] 多个条件
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + " and "
        return feature

    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        # 判断是否是字符串
        if isinstance(loc, str):
            # 判断是否以//开头
            if loc.startswith("//"):
                return loc
            # 调用处理后的xpath(拼接)
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)
        feature = feature.rstrip(" and ")
        loc = feature_start + feature + feature_end
        return loc

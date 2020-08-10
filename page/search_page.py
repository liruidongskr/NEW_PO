from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class SearchPage(BaseAction):

    search_button = By.ID, "com.android.settings:id/search"
    search_text = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_search(self):
        self.click(self.search_button)

    def input_search_text(self, text):
        self.input_text(self.search_text, text)

    def click_back(self):
        self.click(self.back_button)

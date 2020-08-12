import os, sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.network_page import NetworkPage

class TestNetwork:

    def setup(self):
        self.driver = init_driver()
        self.network_page = NetworkPage(self.driver)

    def test_network_2g(self):
        self.network_page.click_move()
        self.network_page.click_typeNet()
        self.network_page.click_2G()

    def test_neteork_3g(self):
        self.network_page.click_move()
        self.network_page.click_typeNet()
        self.network_page.click_3G()

    def test_neteork_4g(self):
        self.network_page.click_move()
        self.network_page.click_typeNet()
        self.network_page.click_3G()

import time

from selenium import webdriver
from pom.Pages.Impersonation import Impersonation
from pom.Pages.LoginPage import LoginPage
import pytest
import unittest


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.delete_all_cookies()
        cls.driver.set_page_load_timeout(30)
        cls.driver.implicitly_wait(30)
        cls.driver.set_window_size(1920, 1080)

    def test_login_sso(self):
        driver = self.driver
        login = LoginPage(driver)
        # login.login_to_impersonations_string()
        login.login_to_impersonations_by()
        # login.login_to_impersonations_javascript()

        # line below used to wait for page to load before asserting
        driver.find_element_by_xpath('//input[@value="Impersonate"]')

        # imp = Impersonation()
        imp = Impersonation(driver)

        imp.select_application_name('betaadminapps.utep.edu/1098tAcknowledgement')
        imp.select_user()
        # imp.select_user1('(psguajardo)')

    #     time.sleep(2)
    #     # title = driver.title
    #     # assert title == 'SSO-Impersonation'
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()


# used so file can be called from cmd line
if __name__ == '__main__':
    unittest.main()

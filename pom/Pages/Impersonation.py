import time

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException

from pom.Pages.Base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Impersonation(BasePage):

    # def __init__(self):
    #     self.driver = webdriver.Chrome()

    def __init__(self, driver):
        self.driver = driver

    def select_application_name(self, app_name):
        # betamy.utep.edu / personalprofilemanager
        driver = self.driver
        select = Select(driver.find_element_by_id('ApplicationId'))
        # select.select_by_value('253711')
        select.select_by_visible_text(app_name)

    def select_user1(self, imp_user):
        driver = self.driver

        # select = Select(driver.find_element_by_id('Impersonatee'))
        # select.select_by_value('253711')

        # explicit wait for user drop down populates
        WebDriverWait(driver, 10, poll_frequency=1).until(EC.presence_of_element_located((By.ID, 'Impersonatee')))
        # element = WebDriverWait(driver, 10, poll_frequency=1)
        # element.until(EC.presence_of_element_located(driver.find_element_by_id('Impersonatee')))
        # .element_to_be_selected(select.select_by_visible_text(imp_user)))
        # .presence_of_element_located(imp))
        # select.select_by_visible_text(imp_user)
        # time.sleep(2)
        select1 = Select(driver.find_element_by_id('Impersonatee'))
        select1.select_by_visible_text(imp_user)

        # driver.find_element_by_xpath('//input[@value="Impersonate"]').click()

    def select_user(self):
        # betamy.utep.edu / personalprofilemanager
        driver = self.driver
        select = Select(driver.find_element_by_id('Impersonatee'))
        # select.select_by_value('253711')

        # explicit wait for user drop down populates
        i = 3
        while i >= 0:
            # element = WebDriverWait(driver, 10, poll_frequency=1,
            #                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
            element = WebDriverWait(driver, 10, poll_frequency=1)
            element.until(EC.presence_of_element_located((By.ID, 'Impersonatee')))
            select = Select(driver.find_element_by_id('Impersonatee'))
            select.select_by_visible_text('(mpolague)')
            i -= 1

        print('\npost\n')
        # select = Select(driver.find_element_by_id('Impersonatee'))
        # select.select_by_visible_text('(mpolague)')

        # while not select.first_selected_option == '(mpolague)':
        #     print('\nIN\n')
        #     select = Select(driver.find_element_by_id('Impersonatee'))
        #     select.select_by_visible_text('(mpolague)')

        # if select.first_selected_option ==
        # driver.find_element_by_xpath('//input[@value="Impersonate"]').click()

    def select_app_and_user(self):
        driver = self.driver
        select = Select(driver.find_element_by_id('Impersonatee'))
        select.select_by_value('253711')
        select.select_by_visible_text('(psguajardo)')
        driver.find_element_by_xpath('//input[@value="Impersonate"]').click()

    def impersonation_submit(self):
        driver = self.driver
        driver.find_element_by_xpath('//input[@value="Impersonate"]').click()

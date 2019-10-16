from _pytest import unittest

from selenium import webdriver
from selenium.webdriver.support.select import Select
from LoginTest.Base import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class FFbrowser(BasePage):
    start = time.time()
    driver = webdriver.Firefox(executable_path='geckodriver.exe')
    # driver = webdriver.Remote(
    #     command_executor="http:localhost:4444/wd/hub",
    #     desired_capabilities={
    #         "browserName": "firefox",
    #     }
    # )
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    driver.delete_all_cookies()
    driver.get('https://betaadminapps.utep.edu/impersonation/')
    driver.find_element_by_css_selector('.cui-button.cui-button-medium.cui-button-type-default').click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, 'usernameTextbox')))
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.presence_of_element_located((By.ID, 'usernameTextbox')))

    un = driver.find_element_by_id('usernameTextbox').send_keys(BasePage.username)
    # un.send_keys(BasePage.username)
    pw = driver.find_element_by_name('passwordTextbox')
    pw.send_keys(BasePage.creds)
    driver.find_element_by_id('loginSubmitButton').submit()

    # driver.execute_script("var u = document.getElementById('usernameTextbox'); u.value='" + BasePage.username + "';")
    # driver.execute_script("var p = document.getElementById('passwordTextbox'); p.value='" + BasePage.creds + "';")
    # driver.execute_script("document.getElementById('loginSubmitButton').click()")

    select = Select(driver.find_element_by_id('Impersonatee'))
    select.select_by_value('253711')
    # select.select_by_visible_text('(psguajardo)')
    driver.find_element_by_xpath('//input[@value="Impersonate"]').click()
    driver.quit()
    end = time.time()
    print('FF '+str(end - start))


# if __name__ == '__main__':
#     unittest.main()

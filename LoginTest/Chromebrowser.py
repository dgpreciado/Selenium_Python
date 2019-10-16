import time

from _pytest import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from LoginTest.Base import BasePage


class Chromebrowser(BasePage):
    start = time.time()
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    # driver = webdriver.Remote(
    #     command_executor="http:localhost:4444/wd/hub",
    #     desired_capabilities={
    #         "browserName": "chrome",
    #     }
    # )
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    driver.get('https://betaadminapps.utep.edu/impersonation/')
    driver.find_element_by_css_selector('.cui-button.cui-button-medium.cui-button-type-default').click()
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, 'usernameTextbox')))
    ut = driver.find_element_by_name('usernameTextbox')
    driver.execute_script("var u = document.getElementById('usernameTextbox'); u.value='" + BasePage.username + "';")
    driver.execute_script("var p = document.getElementById('passwordTextbox'); p.value='" + BasePage.creds + "';")
    driver.execute_script("document.getElementById('loginSubmitButton').click()")
    select = Select(driver.find_element_by_id('Impersonatee'))
    select.select_by_value('337378')
    # select.select_by_visible_text('(mpolague)')
    driver.find_element_by_xpath('//input[@value="Impersonate"]').click()
    driver.quit()
    end = time.time()
    print('chrome ' + str(end - start))


# if __name__ == '__main__':
#     unittest.main()

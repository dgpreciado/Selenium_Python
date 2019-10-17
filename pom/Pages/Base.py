from selenium import webdriver


class BasePage(object):
    # self.driver = driver
    username = ''
    creds = ''
    # driver = webdriver.Chrome('chromedriver.exe')
    # # self.driver = driver
    # self.driver.set_page_load_timeout(30)
    # self.driver.implicitly_wait(30)
    if not creds:
        print('enter the creds')
        creds = input()

from pom.Pages.Base import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # test SSO button
    test_sso_button_css = '.cui-button.cui-button-medium.cui-button-type-default'

    # username for SSO
    enter_username_id = 'usernameTextbox'

    # password for SSO
    enter_credentials_id = 'passwordTextbox'

    # login submit button
    login_submit_button_id = 'loginSubmitButton'

    # def __init__(self):
    #     self.driver = webdriver.Chrome()

    def __init__(self, driver):
        self.driver = driver
        # super()
        # # test SSO button
        # self.test_sso_button_css = '.cui-button.cui-button-medium.cui-button-type-default'
        #
        # # username for SSO
        # self.enter_username_id = 'usernameTextbox'
        #
        # # password for SSO
        # self.enter_credentials_id = 'passwordTextbox'
        #
        # # login submit button
        # self.login_submit_button_id = 'loginSubmitButton'

    def login_to_impersonations_javascript(self):
        self.driver.get('https://betaadminapps.utep.edu/impersonation/')
        self.driver.find_element_by_css_selector('.cui-button.cui-button-medium.cui-button-type-default').click()
        self.driver.execute_script(
            "var u = document.getElementById('usernameTextbox'); u.value='" + BasePage.username + "';")
        self.driver.execute_script(
            "var p = document.getElementById('passwordTextbox'); p.value='" + BasePage.creds + "';")
        self.driver.execute_script("document.getElementById('loginSubmitButton').click()")

    def login_to_impersonations_string(self):
        self.driver.get('https://betaadminapps.utep.edu/impersonation/')
        self.driver.find_element_by_css_selector(self.test_sso_button_css).click()
        enter_user = self.driver.find_element_by_id(self.enter_username_id)
        enter_user.send_keys(BasePage.username)
        enter_creds = self.driver.find_element_by_id(self.enter_credentials_id)
        enter_creds.send_keys(BasePage.creds)
        login_submit = self.driver.find_element_by_id(self.login_submit_button_id)
        login_submit.click()

    def login_to_impersonations_by(self):
        self.driver.get('https://betaadminapps.utep.edu/impersonation/')
        test_sso_button = self.driver.find_element(By.CSS_SELECTOR, self.test_sso_button_css)
        test_sso_button.click()
        enter_user = self.driver.find_element(By.ID, self.enter_username_id)
        enter_user.send_keys(BasePage.username)
        enter_creds = self.driver.find_element(By.ID, self.enter_credentials_id)
        enter_creds.send_keys(BasePage.creds)
        login_submit = self.driver.find_element(By.ID, self.login_submit_button_id)
        login_submit.click()


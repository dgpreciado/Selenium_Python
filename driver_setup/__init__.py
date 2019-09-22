from selenium import webdriver

driverC = webdriver.Chrome("drivers/chromedriver.exe")
#driverC.get("http://www.utep.edu")
#driverC.find_element_by_link_text("ACCOLADES").click()
#driverC.quit()

#driverf = webdriver.Firefox(executable_path="drivers/geckodriver.exe")
#driverf.get("http://www.utep.edu")
#driverf.find_element_by_link_text("ACCOLADES").click()
#driverf.quit()

driverC.set_page_load_timeout(30)
driverC.implicitly_wait(30)

driverC.delete_all_cookies()
driverC.get("https://ui.freecrm.com/")
driverC.maximize_window()

driverC.find_element_by_css_selector(".fluid").click()

driverC.find_element_by_link_text("Contacts").click()
driverC.find_element_by_css_selector("a[href='/contacts/new']").click()


#driverC.get("https://ui.freecrm.com/contacts")
# driverC.find_element_by_xpath('//td[contains(text(),"mname")]//parent::tr//preceding-sibling::td/div').click()
# try:
#     print(driverC.find_element_by_xpath('//td[contains(text(),"first middle last")]//parent::tr'
#                                     + '//preceding-sibling::td/div/input').is_selected())
# except:
#     print("error")
#
# print(driverC.find_element_by_xpath('//td[contains(text(),"fname")]//parent::tr'
#                                     + '//preceding-sibling::td/div/input').is_selected())

# driverC.quit()
driverC.delete_all_cookies()

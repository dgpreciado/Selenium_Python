from selenium import webdriver

driverC = webdriver.Chrome("drivers/chromedriver.exe")
driverC.get("http://www.utep.edu")
driverC.find_element_by_link_text("ACCOLADES").click()
driverC.quit()

driverf = webdriver.Firefox(executable_path="drivers/geckodriver.exe")
driverf.get("http://www.utep.edu")
driverf.find_element_by_link_text("ACCOLADES").click()
driverf.quit()

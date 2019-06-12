from selenium import webdriver
import selenium
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("C:/Users/owner/Desktop/Drop_Down.html")

drop_menu1 = driver.find_element_by_xpath("//select[@id ='fruits01']")
drop_menu1.click()
time.sleep(2)

drop_menu1.send_keys('Mango')

time.sleep(2)

driver.close()




from selenium import webdriver
from time import sleep
import time

driver = webdriver.Chrome()
driver.maximize_window()

location_of_html = "file://C://Users//owner//Desktop//createalert.html"
driver.get(location_of_html)

alert_button = driver.find_element_by_name('alert')
alert_button.click()

obj = driver.switch_to.alert

msg = obj.text

print("Alert bos shows follwoing message" + msg)

time.sleep(2)
driver.implicitly_wait(3)

obj.accept()

print("clicked on alert box OK")

driver.close()


from selenium import webdriver
from time import sleep
import time

driver = webdriver.Chrome()
driver.maximize_window()

location_confirm_alert = "C:/Users/owner/Desktop/createalert.html"

driver.get(location_confirm_alert)

name_element_button = driver.find_element_by_name('alert')

name_element_button.click()
time.sleep(2)

obj = driver.switch_to.alert

print("The test is now this"+(obj.text))

time.sleep(2)
obj.accept()

back_obj = driver.switch_to.active_element
time.sleep(2)

name_element_button2 = driver.find_element_by_name('alert')
name_element_button2.click()

time.sleep(2)
obj = driver.switch_to.alert

print("The test is now this"+(obj.text))

time.sleep(2)

obj.accept()

time.sleep(3)

driver.close()
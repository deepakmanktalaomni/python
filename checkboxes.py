from selenium import webdriver
from time import sleep
import time

driver = webdriver.Chrome()
driver.maximize_window()

time.sleep(2)

driver.get(("C:/Users/owner/Desktop/Confirmation_alert.html"))

time.sleep(2)

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(checkboxes[:])

checkbox_list = []

for check in checkboxes:
    checkbox_list.append(check.get_attribute('value'))
    print("************************************")
    print(check, checkbox_list)
    print( "************************************" )
for checkbox in checkboxes:
    print(checkbox)
    if not checkbox.is_selected():
        time.sleep(2)
        checkbox.click()

checkboxes_deselect = driver.find_elements_by_xpath("//input[@type='checkbox']")
for i in checkboxes_deselect:
    if i.is_selected():
        time.sleep(2)
        i.click()

time.sleep(2)
driver.close()

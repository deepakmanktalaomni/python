from selenium import webdriver
from time import sleep
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

driver.get("C:/Users/owner/Desktop/prompt_alert.html")

continue_button = driver.find_element_by_name('employeeLogin')

continue_button.click()

time.sleep(2)

obj_prompt = driver.switch_to.alert
time.sleep(2)
obj_prompt.send_keys("Deepak Manktala")
time.sleep(2)
obj_prompt.accept()
time.sleep(2)
obj_prompt.accept()

back = driver.switch_to.active_element

continue_button1 = driver.find_element_by_name('employeeLogin')
continue_button1.click()
time.sleep(2)

obj_prompt1 = driver.switch_to.alert
obj_prompt1.send_keys("Manish Jan")
time.sleep(2)

obj_prompt1.accept()
time.sleep(3)
obj_prompt.accept()
time.sleep(3)



obj_prompt = driver.switch_to.window(window_n)

driver.c
driver.close()
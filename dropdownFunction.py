from selenium import webdriver
import selenium
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("C:/Users/owner/Desktop/Drop_Down.html")


for i in range(1,20):
    time.sleep(1)
    drop_menu = driver.find_element_by_xpath("//select[@id ='fruits01']")
    drop_menu.click()
    time.sleep( 3 )
    fruit_element = driver.find_element_by_xpath("//select[@id ='fruits01']/option[text() = 'Mango']")

    time.sleep(1)

    fruit_element.click()
    time.sleep(1)
    fruit_element = driver.find_element_by_xpath("//select[@id ='fruits01']/option[text() = 'Banana']")

    time.sleep(1)

    fruit_element.click()

    fruit_element = driver.find_element_by_xpath( "//select[@id ='fruits01']/option[text() = 'Melon']" )

    time.sleep( 1 )

    fruit_element.click()

    time.sleep(1)
driver.close()
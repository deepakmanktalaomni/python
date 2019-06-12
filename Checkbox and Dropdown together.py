from selenium import webdriver
import selenium
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("C:/Users/owner/Desktop/Drop_Down.html")


for i in range(1,20):
    time.sleep(1)

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
    checkboxes = driver.find_elements_by_xpath( "//input[@type='checkbox']" )

    print( checkboxes[:] )

    checkbox_list = []

    for check in checkboxes:
        checkbox_list.append( check.get_attribute( 'value' ) )
        print( "************************************" )
        print( check, checkbox_list )
        print( "************************************" )
    for checkbox in checkboxes:
        print( checkbox )
        if not checkbox.is_selected():
            time.sleep( 1 )
            checkbox.click()

    checkboxes_deselect = driver.find_elements_by_xpath( "//input[@type='checkbox']" )
    for i in checkboxes_deselect:
        if i.is_selected():
            time.sleep( 1 )
            i.click()

driver.close()
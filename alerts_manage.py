from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import unittest

class CompareProducts(unittest.TestCase):
    def setUp (self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.flipkart.com/")
        self.driver.maximize_window()
        sleep(2)

    def test_compare_product_removal_alert(self):
        closefirstlogin = self.driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']")
        closefirstlogin.click()
        sleep(2)
        search_field = self.driver.find_element_by_xpath("//input[@name='q']")
        search_field.clear()

        search_field.send_keys('Phones')
        search_field.submit()
        sleep(2)

        self.driver.find_element_by_xpath("//div[contains(text(),'Redmi Note 5 (Black')]//parent::*//parent::*//parent::*//child::label//div[@class='_1p7h2j']").click()
        sleep(2)
        clear_all_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'COMPARE')]")))
        sleep(2)
        hoveraction1 = ActionChains(self.driver)
        hoveraction1.move_to_element(clear_all_link)
        hoveraction1.perform()
        sleep(5)
        #clear_all_link.click()
        closebutton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='_2giIUw']//child::span[@class='_3CbzG3']")))
        closebutton.click()
        sleep(5)
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        sleep(15)

        alert_text = alert.text

        self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)
        alert.accept()


        def tearDown(self):
            self.driver.quit()


    if __name__ == "__main__":
        unittest.main(verbosity=2)

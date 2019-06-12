import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get("http://cal.omniintegrate.com:9000/OmniSolutions")
        cls.driver.implicitly_wait( 30 )

    def test_CLA_Login(self):

        cla_user = self.driver.find_element_by_id( "UserName" )
        cla_user.clear()
        cla_user.send_keys( "Deepak" )
        cla_password = self.driver.find_element_by_id( "Password" )
        cla_password.clear()
        cla_password.send_keys( "Omni@123" )
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.ID, 'login') ))
        self.driver.find_element_by_id( "login" ).click()
        #print(self.driver.find_element_by_xpath("//*[contains(@title, 'Manage')]"))
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//*[contains(@title, 'Omni Integration')]") ) )
        self.assertTrue( self.is_element_present( By.XPATH, "//*[contains(@title, 'Manage')]" ))
        #self.assertEqual('Project Status',self.driver.find_element_by_link_text('Project Status') )

    def tearDown(cls):
       # close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element( by=how, value=what )
        except NoSuchElementException as e: return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=3)
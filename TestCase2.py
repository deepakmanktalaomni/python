import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoggedInPageTest(unittest.TestCase):
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


    def test_CLA_Board(self):

        cla_user = self.driver.find_element_by_id( "UserName" )
        cla_user.clear()
        cla_user.send_keys( "Deepak" )
        cla_password = self.driver.find_element_by_id( "Password" )
        cla_password.clear()
        cla_password.send_keys( "Omni@123" )
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.ID, 'login') ))
        self.driver.find_element_by_id( "login" ).click()
        #print(self.driver.find_element_by_xpath("//*[contains(@title, 'Manage')]"))
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//a[text()='Board Status']") ) )
        URL_Links = self.driver.find_elements_by_xpath('//*[@href]')

        for ii in URL_Links:
            print(ii.get_attribute('href'))
        self.driver.find_element_by_xpath("//a[text()='Board Status']").click()
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//select[@id='SelectedBoard']") ) )
        self.assertTrue( self.is_element_present( By.XPATH, "//select[@id='SelectedBoard']" ))
        #self.driver.find_element(By.XPATH("//a[text()='ABC company']//parent::td[@class='datalistrow']//preceding-sibling::td[@class='datalistrow']//input[@name='client_id']"))
        #self.assertTrue( self.is_element_present( By.XPATH, "//*[contains(@title, 'Manage')]" ))
        #self.assertEqual('Project Status',self.driver.find_element_by_link_text('Project Status') )
        self.driver.find_element_by_xpath("//option[contains(text(),'App')]").click()

    def test_dropdown_under_board(self):
            cla_user = self.driver.find_element_by_id( "UserName" )
            cla_user.clear()
            cla_user.send_keys( "Deepak" )
            cla_password = self.driver.find_element_by_id( "Password" )
            cla_password.clear()
            cla_password.send_keys( "Omni@123" )
            self.driver.element = WebDriverWait( self.driver, 10 ).until(
                EC.presence_of_element_located( (By.ID, 'login') ) )
            self.driver.find_element_by_id( "login" ).click()
            # print(self.driver.find_element_by_xpath("//*[contains(@title, 'Manage')]"))
            self.driver.element = WebDriverWait( self.driver, 10 ).until(
                EC.presence_of_element_located( (By.XPATH, "//a[text()='Board Status']") ) )
            URL_Links = self.driver.find_elements_by_xpath( '//*[@href]' )

            for ii in URL_Links:
                print( ii.get_attribute( 'href' ) )
            self.driver.find_element_by_xpath( "//a[text()='Board Status']" ).click()
            self.driver.element = WebDriverWait( self.driver, 10 ).until(
                EC.presence_of_element_located( (By.XPATH, "//select[@id='SelectedBoard']") ) )
            self.assertTrue( self.is_element_present( By.XPATH, "//select[@id='SelectedBoard']" ) )
            # self.driver.find_element(By.XPATH("//a[text()='ABC company']//parent::td[@class='datalistrow']//preceding-sibling::td[@class='datalistrow']//input[@name='client_id']"))
            # self.assertTrue( self.is_element_present( By.XPATH, "//*[contains(@title, 'Manage')]" ))
            # self.assertEqual('Project Status',self.driver.find_element_by_link_text('Project Status') )
            self.driver.find_element_by_xpath( "//option[contains(text(),'App')]" ).click()




    def test_dropdown_under_board(self):
        cla_user = self.driver.find_element_by_id( "UserName" )
        cla_user.clear()
        cla_user.send_keys( "Deepak" )
        cla_password = self.driver.find_element_by_id( "Password" )
        cla_password.clear()
        cla_password.send_keys( "Omni@123" )
        self.driver.element = WebDriverWait( self.driver, 10 ).until(
            EC.presence_of_element_located( (By.ID, 'login') ) )
        self.driver.find_element_by_id( "login" ).click()
        # print(self.driver.find_element_by_xpath("//*[contains(@title, 'Manage')]"))
        self.driver.element = WebDriverWait( self.driver, 10 ).until(
            EC.presence_of_element_located( (By.XPATH, "//a[text()='Board Status']") ) )
        URL_Links = self.driver.find_elements_by_xpath( '//*[@href]' )

        for ii in URL_Links:
            print( ii.get_attribute( 'href' ) )
        self.driver.find_element_by_xpath( "//a[text()='Board Status']" ).click()
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//select[@id='SelectedBoard']") ) )
        self.assertTrue( self.is_element_present( By.XPATH, "//select[@id='SelectedBoard']" ) )
        # self.driver.find_element(By.XPATH("//a[text()='ABC company']//parent::td[@class='datalistrow']//preceding-sibling::td[@class='datalistrow']//input[@name='client_id']"))
        # self.assertTrue( self.is_element_present( By.XPATH, "//*[contains(@title, 'Manage')]" ))
        # self.assertEqual('Project Status',self.driver.find_element_by_link_text('Project Status') )
        self.driver.find_element_by_xpath( "//option[contains(text(),'App')]" ).click()
        self.driver.find_element_by_xpath("//b[contains(text(),'AmericanExpress')]").click()
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//th[contains(text(),'Description')]")))
        self.assertTrue(self.is_element_present(By.XPATH,"//th[contains(text(),'Task ID')]"))


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
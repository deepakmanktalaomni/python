import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import
from selenium.webdriver.common.alert i
from selenium.common.exceptions import TimeoutException


import pytest
import _pytest

class SignupTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()


    def test_someone_can_signup(self):
        self.browser.get("https://login.yahoo.com/")
        user_name = self.browser.find_element_by_id("login-username")
        user_name.send_keys("manks_boy")
        time.sleep(1)
        next_button = self.browser.find_element_by_id("login-signin")
        user_name.send_keys(Keys.RETURN)
        time.sleep(1)

        try:
            myElem = WebDriverWait( self.browser, 10 ).until( EC.presence_of_element_located\
                                                                ( (By.XPATH,"//h1[@class = 'username']" ) ))
            print("Page is ready!")

        except TimeoutException:
            print("Loading is taking too much time")


        password = self.browser.find_element_by_id( "login-passwd" )

        password.send_keys("Muktsar@33")

        sign_up= self.browser.find_element_by_id( "login-signin" )
        sign_up.send_keys( Keys.RETURN )
        time.sleep(10)

        def tearDown(self):
            self.browser.close()

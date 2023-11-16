from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from percy import percy_snapshot
import os
import time
import unittest
from checkout import *

"""
opt= Options()
#opt.add_experimental_option("mobileEmulation", {"deviceName": "Pixel 2"})
opt.add_experimental_option("detach",True)
token=os.getenv("PERCY_TOKEN")
if token:
    print("Token is :", token)
driver= webdriver.Chrome(options= opt)
driver.maximize_window()
driver.get("https://facebook.com/")
time.sleep(8)

#percy_snapshot(driver, "HomePage")
"""

class TestCases(unittest.TestCase):
    def setUp(self):
        
        self.options= Options()
        self.options.add_argument("--headless")
        self.driver= webdriver.Chrome(options=self.options)
        #self.driver= webdriver.Chrome()
        self.driver.get("https://gardenforwildlife.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.close()


    def test_checkout(self):
        order_purchase= checkout(self.driver)
        order_purchase.open_pdp_product_plants()
        order_purchase.checkout_page()


if __name__ == "__main__":
    unittest.main()
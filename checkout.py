#this is checkout file
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class checkout:

    def __init__(self, driver):
        self.driver=driver
        self.driver.get("https://gardenforwildlife.com/collections/all-products")
        time.sleep(5)

    def open_pdp(self):
        self.driver.find_element(By.CSS_SELECTOR, product1).click()
        self.driver.find_element(By.CSS_SELECTOR, product1_zip).send_keys("15001")
        self.driver.find_element(By.CSS_SELECTOR, add_to_cart_button).click()
        time.sleep(3)
        

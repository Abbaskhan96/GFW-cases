#this is checkout file
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class checkout:

    def __init__(self, driver):
        self.driver=driver
       # self.driver.get("https://gardenforwildlife.com/collections/all-products")
        time.sleep(5)

    def open_pdp_product_plants(self):
        for i,j in zip(zip_value,range(1,3)):

            self.driver.get("https://gardenforwildlife.com/collections/all-products")
            self.driver.find_element(By.CSS_SELECTOR, products_plants[j]).click()
            self.driver.find_element(By.CSS_SELECTOR, product_zip).clear()
            self.driver.find_element(By.CSS_SELECTOR, product_zip).send_keys(i)

            self.driver.find_element(By.CSS_SELECTOR, add_to_cart_button).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, cart_close_btn).click()
        
    
    def checkout_page(self):
        self.driver.get("https://gardenforwildlife.com/cart")
        self.driver.find_element(By.XPATH, checkout_btn).click()
        time.sleep(3)
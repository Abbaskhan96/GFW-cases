#this is checkout file
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time



class checkout:

    def __init__(self, driver):
        self.driver=driver
       # self.driver.get("https://gardenforwildlife.com/collections/all-products")
        time.sleep(5)

    def open_pdp_product_plants(self):
        for i,j in zip(zip_value,range(1,3)):

            self.driver.get("https://gardenforwildlife.com/collections/all-products")
    
            if i==zip_value[-1]:
                zip_btn=self.driver.find_element(By.CSS_SELECTOR,zip_btn_plp).text
                assert zip_btn=='15001'
                
                zip_btn=self.driver.find_element(By.ID,"zip-form-2").clear()
                zip_btn=self.driver.find_element(By.CSS_SELECTOR,"#btn-zip-form-2").click()



            self.driver.find_element(By.CSS_SELECTOR, products_plants[j]).click()
            self.driver.find_element(By.CSS_SELECTOR, product_zip).clear()
            self.driver.find_element(By.CSS_SELECTOR, product_zip).send_keys(i)

            self.driver.find_element(By.CSS_SELECTOR, add_to_cart_button).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, cart_close_btn).click()

             
    
    def open_pdp_product_merch(self):
        
       for i in range(1,3):
            self.driver.get("https://gardenforwildlife.com/collections/gifts")
            self.driver.find_element(By.CSS_SELECTOR, product_merch[i]).click()

            self.driver.find_element(By.CSS_SELECTOR, add_to_cart_button).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, cart_close_btn).click()
            


    def checkout_page(self):
        self.driver.get("https://gardenforwildlife.com/cart")
        cart_price_value= self.driver.find_element(By.XPATH, cart_price).text
        assert cart_price_value == '$222.00'

        self.driver.find_element(By.XPATH, checkout_btn).click()
        time.sleep(3)
        
        for i,j in zip(checkout_fields_path.values(), checkout_field_values.values()):
            
            if j=="Florida":
                sel= Select(self.driver.find_element(By.XPATH,i))
                sel.select_by_visible_text(j)
                
            elif j=='33322':
                self.driver.find_element(By.XPATH,i).send_keys(j)

            else:
              self.driver.find_element(By.XPATH,i).send_keys(j)
            
        self.driver.find_element(By.XPATH, checkout_btn_1).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,remove_product).click
        self.driver.find_element(By.XPATH, continue_checkout).click()
        time.sleep(5)
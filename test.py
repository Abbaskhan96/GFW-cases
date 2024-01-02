from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from percy import percy_snapshot
import os
import time
import unittest
from checkout import *
import pyautogui




class TestCases(unittest.TestCase):
    def setUp(self):
        
        self.options= Options()
        #self.options.add_argument("--headless")
        #self.driver= webdriver.Chrome(options=self.options)
        self.driver= webdriver.Chrome()
        self.driver.get("https://gardenforwildlife.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.close()


    def test_checkout(self):
        order_purchase= checkout(self.driver)
        order_purchase.open_pdp_product_plants()
        order_purchase.open_pdp_product_merch()
        order_purchase.checkout_page()


if __name__ == "__main__":
    unittest.main()




#----------------------------------------------------------

#driver= webdriver.Chrome()
#driver.maximize_window()
#driver.get("https://display.ugc.bazaarvoice.com/bvstaging/static/partner-klaviyo/en_US/container.htm?bvaction=rr_submit_review&bvproductId=product6")
#time.sleep(5)
#shadow_host= driver.find_element(By.XPATH,"//div[@data-bv-product-id='product6']")
#script = 'return arguments[0].shadowRoot'
##shadow_root = driver.execute_script (script, shadow_host)
#shadow=driver.execute_script (script, shadow_host)
#
##adding text in the shadow-root div
#shadow.find_element(By.ID,"bv-ips-star-rating-1").click()
#shadow.find_element(By.NAME,'Review').clear()
#shadow.find_element(By.NAME,'Review').send_keys('These are my test Reviews Which i have to written.')
#shadow.find_element(By.NAME,'Review Title').send_keys('The Review titles should be spefic')
#shadow.find_element(By.NAME,'Nickname').send_keys('Jackson')
#shadow.find_element(By.NAME,'Email').send_keys('khan@gmail.com')
#time.sleep(2)
#check=shadow.find_element(By.ID,"sps-termsAndConditions-styledcheckbox").click()
#time.sleep(2)
#check_text=shadow.find_element(By.CSS_SELECTOR,".ips__sc-p5n3bz-0.VhgYi").text
#check_2=shadow.find_element(By.CSS_SELECTOR,".ips__sc-p5n3bz-0.VhgYi").click()
#time.sleep(6)
#
#shadow.find_element(By.ID,'bv-ips-photo-upload-btn').click()
#time.sleep(2)
#pyautogui.write(r'C:\Users\Abbas Khan\Pictures\text2.png')
#pyautogui.press("enter")
#
##Submiting picture
#time.sleep(2)
#shadow.find_element(By.CSS_SELECTOR,".ips__sc-p5n3bz-0.VhgYi").click()
#time.sleep(6)
##Personal Details
#shadow.find_element(By.NAME,"Where are you located?").send_keys("United States")
#shadow.find_element(By.ID,"2_Age-25to34").click()
#shadow.find_element(By.ID,"2_Gender-Male").click()
#shadow.find_element(By.ID,"2_IncentivizedReview-True").click()
#shadow.find_element(By.CSS_SELECTOR,".ips__sc-p5n3bz-0.VhgYi").click()
#time.sleep(3)
##Product Rating
#shadow.find_element(By.ID,"3_isrecommended-true").click()
#shadow.find_element(By.ID,"bv-ips-star-Quality-3").click()
#shadow.find_element(By.ID,"bv-ips-star-Value-3").click()
#
#time.sleep(5)


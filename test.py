from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from percy import percy_snapshot
import os
import time

opt= Options()
opt.add_experimental_option("mobileEmulation", {"deviceName": "iPad"})
opt.add_experimental_option("detach",True)
token=os.getenv("PERCY_TOKEN")
if token:
    print("Token is :", token)
driver= webdriver.Chrome(options= opt)
driver.maximize_window()
driver.get("https://gardenforwildlife.com/")
time.sleep(10)

#percy_snapshot(driver, "HomePage")


#web element command, used to interact the web page
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from se

driver_path = r"E:\Automation testing\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)

driver.  get("https://www.saucedemo.com/")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

username=driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("standard_user")

password=driver.find_element(By.ID,"password")
password.click()
password.send_keys("secret_sauce")

login=driver.find_element(By.ID,"login-button")
login.click()
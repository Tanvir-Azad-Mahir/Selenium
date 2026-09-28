from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

service_obj=Service()
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
d= webdriver.Chrome(options=options, service=service_obj)
d.get("https://skillandswap.netlify.app/login")
d.maximize_window()
d.find_element(By.ID,"login-email").send_keys("tanvirazadmahir@gmail.com")
d.find_element(By.ID,"login-password").send_keys("123456")
d.find_element(By.CSS_SELECTOR, '[type="submit"]').click()







from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

d = webdriver.Chrome(options=options, service=service_object)
d.get("https://rahulshettyacademy.com/client")
d.find_element(By.ID,"userEmail").send_keys(" 0112230001@gmail.com")
d.find_element(By.ID,"userPassword").send_keys("Ab#12345")
time.sleep(5)
d.find_element(By.CLASS_NAME,"forgot-password-link").click()
time.sleep(2)

heading = d.find_element(By.CSS_SELECTOR, "h3")
print("Forgot Password page heading:", heading.text)
d.back()
time.sleep(2)
d.find_element(By.ID,"userEmail").send_keys("tanvirazadmahir@gmail.com")
d.find_element(By.ID,"userPassword").send_keys("@Tam112233")
d.find_element(By.ID,"login").click()
time.sleep(2)
d.find_element(By.CSS_SELECTOR,"blinkingText").click()








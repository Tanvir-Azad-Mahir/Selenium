from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome driver
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")
print("Page title:", driver.title)

# Close browser
driver.quit()
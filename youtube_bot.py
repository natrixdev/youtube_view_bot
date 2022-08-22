from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import time 
driver = webdriver.Chrome()
while True:
    driver.get("INPUT YOUT VIDEO URL HERE")
    time.sleep(5)


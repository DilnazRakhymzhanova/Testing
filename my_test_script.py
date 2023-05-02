from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.google.com')
import time

locator_1 = driver.find_element(By.CLASS_NAME, 'gLFyf')
locator_1.send_keys("Selenium")
locator_1.send_keys(Keys.ENTER)
time.sleep(5)
locator_2 = driver.find_element(By.XPATH, '//*[@class="LC20lb MBeuO DKV0Md"]').click()
time.sleep(5)




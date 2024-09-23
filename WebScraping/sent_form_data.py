import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfKvACDg4x2a8zwcwkLxtilQzJip_dIBLDBHcsn2IYhZbYsAg/viewform")
driver.maximize_window()

input_text = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
input_text.click()
time.sleep(1)
input_text.send_keys("Elif Tosun")
meal_size = driver.find_element(By.ID, "i9")
meal_size.click()
chili_pepper = driver.find_element(By.ID, "i23")
chili_pepper.click()
green_pepper = driver.find_element(By.ID, "i26")
green_pepper.click()
corn = driver.find_element(By.ID, "i29")
corn.click()
payment_type = driver.find_element(By.XPATH, "//div[@class='MocG8c HZ3kWc mhLiyf LMgvRb KKjvXb DEh1R']")
payment_type.click()
payment_type.send_keys(Keys.ENTER)
time.sleep(1)
meal_card = driver.find_element(By.XPATH, "//div[@class='ry3kXd']/div[@data-value='Meal Card']/span[@class='vRMGwf oJeWuf']")
meal_card.click()
cash = driver.find_element(By.XPATH, "//div[@jscontroller='liFoG']/div[@role='listbox']/div[@jsname='LgbsSe']/div[@class='ry3kXd']/div[@class='MocG8c HZ3kWc mhLiyf OIC90c LMgvRb KKjvXb']/span[@class='vRMGwf oJeWuf']")
cash.click()
cash.send_keys(Keys.ENTER)

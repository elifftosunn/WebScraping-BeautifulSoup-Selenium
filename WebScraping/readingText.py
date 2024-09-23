from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

"""
FOR T3 KYS
"""
driver.get("https://t3kys.com/tr/accounts/login/?next=/tr/")
driver.find_element(By.ID, "id_login").send_keys("<email>")
driver.find_element(By.ID, "id_password").send_keys("<password>")
# driver.find_element(By.ID, "recaptcha-anchor").click()

WebDriverWait(driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[starts-with(@src, 'https://www.google.com/recaptcha/api2/anchor')]")))
WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='recaptcha-checkbox-border']"))).click()

driver.find_element(By.CSS_SELECTOR, "button.btn").click()
try:
    # Wait for up to 10 seconds before throwing an exception
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn"))
    )
    element.click()
except TimeoutException:
    print("Element not found within the time limit")

"""
FOR INSTAGRAM
"""
driver.get("https://www.instagram.com/")
driver.find_element(By.XPATH, "//form[@id='loginForm']/[input/@name='username']").send_keys("<username>")
driver.find_element(By.XPATH, "//form[@id='loginForm']/[input/@name='password']").send_keys("<password>")
driver.find_element(By.CSS_SELECTOR, "button._acan").click()
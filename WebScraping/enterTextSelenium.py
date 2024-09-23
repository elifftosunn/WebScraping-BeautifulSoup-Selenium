from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service = Service("./msedgedriver.exe")
driver = webdriver.Edge(service=service)


driver.find_element(By.ID, "r1-0").click()
driver.get("https://www.google.com/")
searchBox = driver.find_element(By.ID, "APjFqb")
searchBox.send_keys("Python")
searchBox.send_keys(Keys.ENTER)

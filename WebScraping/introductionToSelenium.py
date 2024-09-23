from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys


service = Service("./msedgedriver.exe")
driver = webdriver.Edge(service=service)


driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(10)
page_title = driver.title

if "google.com" in driver.current_url:
    print("Google works!")
driver.get("https://www.trendyol.com")
if "trendyol.com" in driver.current_url:
    print("Trendyol works!")
driver.back()
driver.set_window_size(600, 600)
driver.close()

# if "Google" in driver.title:
#     driver.save_screenshot("Google.png")

# if "Google" in driver.title:
#     print("Google works!")
# driver.forward()
# if "Trendyol" in driver.title:
#     print("Trendyol works!")
# # # driver.maximize_window()
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def order():
    driver.find_element(By.ID, "siparis").click()
def alert():
    return driver.find_element(By.ID, "mesaj").text


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://tomspizzeria.b4a.app/")
driver.maximize_window()

# customer name
order()
message = alert()
assert message == "Enter a customer name"

driver.find_element(By.ID, "musteri-adi").send_keys("Test Name")
order()
message = alert()
assert message == "Choose a pizza size"

kucuk = driver.find_element(By.CSS_SELECTOR, "input[value='Küçük']")
kucuk.click()
order()
message = alert()
assert message == "Choose a payment type"

dropdown = driver.find_element(By.ID, "odeme-tipi")
payment = Select(dropdown)
payment.select_by_index(2)
order()
message = alert()
assert message == "Your order has been received"


# name = driver.find_element(By.XPATH, "//input[@type='text']")
# name.click()
# print(name.text)
# name.send_keys("Jerry")
# print(name.text)
# pizza_size.click()
# add_zeytin = driver.find_element(By.XPATH, "//input[@value='zeytin']")
# add_zeytin.click()
# odeme_tipi_dropdown = driver.find_element(By.ID, "odeme-tipi")
#
# odeme = Select(odeme_tipi_dropdown)
# odeme_tipleri = odeme.options
# for tip in odeme_tipleri:
#     print(tip.text)
# driver.implicitly_wait(1)
#
# odeme.select_by_visible_text("Nakit")
# driver.implicitly_wait(2)
# odeme.select_by_index(2)
# driver.implicitly_wait(2)

# driver.quit()
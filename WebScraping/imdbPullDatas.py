from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.imdb.com/")
driver.maximize_window()

if "IMDb" in driver.title:
    print("IMDb in the title.")
else:
    print("IMDb is not in the title.")

driver.find_element(By.ID, "imdbHeader-navDrawerOpen").click()

# driver.get("https://www.imdb.com")
# driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
# """
# Option 1
# """
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']").click()
# """
# Option 2
# """
"""
BIR ELEMENTIN DEGISIP DEGISMEDIGINE BAKMAK ISTIYORSAK, DEGISTIKTEN SONRA AKSIYON ALMAK ISTIYORSAK WebDriverWait KULLANIRIZ.
poll_frequency = 0.5; saniyede bir expected_conditions şartın saglanip saglanmadigina bakar.
"""

button = WebDriverWait(driver, 5, 0.5,
                       ignored_exceptions=[NoSuchElementException,
                                           ElementClickInterceptedException]).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Top 250 Movies']")))
# button gozukene kadar bekle, 10 saniye beklemene gerek yok
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Top 250 Movies']")))
button.click()
"""
presence vs visibility
implicit wait - gizli bekleme
explicit wait - aciktan bekleme
"""
# Option 3
# time.sleep(1)
# top_250_film = [film.text for film in ]


top_250_film, top_250_film_rating = [], []
while len(top_250_film) != 250:
    top_250_film = [film.text for film in driver.find_elements(By.CSS_SELECTOR, ".iqHBGn h3")]
while len(top_250_film_rating) != 250:
    top_250_film_rating = [rating.text for rating in driver.find_elements(By.CSS_SELECTOR, ".jeHPdh .ipc-rating-star--rating")]

time_elements = driver.find_elements(By.XPATH, "//div[@class='sc-b189961a-0 iqHBGn cli-children']/div[@class='sc-b189961a-7 btCcOY cli-title-metadata']/span[@class='sc-b189961a-8 hCbzGp cli-title-metadata-item'][2]")
year_elements = driver.find_elements(By.XPATH, "//div[@class='sc-b189961a-0 iqHBGn cli-children']/div[@class='sc-b189961a-7 btCcOY cli-title-metadata']/span[@class='sc-b189961a-8 hCbzGp cli-title-metadata-item'][1]")
top_250_links = driver.find_elements(By.CSS_SELECTOR, ".sc-b189961a-0 .ipc-title a[href*='/title']")


time_list = [time.text for time in time_elements]
year_list = [year.text for year in year_elements]
top_250_film_links = [link.get_attribute("href") for link in top_250_links]

# Created TensorFlow Lite XNNPACK delegate for CPU.
options = webdriver.ChromeOptions()
options.add_argument("--log-level=1")

def getTop250FilmDetails():
    count = 0
    description_list, directorList, writersList, starsList = list(), list(), list(), list()
    for link in top_250_film_links:
        driver.implicitly_wait(1)
        driver.get(link)

        description = WebDriverWait(driver, 10, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='plot-xl']"))
        )
        description_list.append(description.text)

        director = WebDriverWait(driver, 10, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".dDErRr .ipc-inline-list__item > a"))
        )
        directorList.append(director.text)

        try:
            writers_div_element = WebDriverWait(driver, 1, 0.1).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Writer')]/following-sibling::div"))
            )
            writers = [t for t in re.findall(r'([A-Z][a-z]* [A-Z][a-z]*(?: [A-Z][a-z]*)?)', writers_div_element.text)]
            writersList.append(",".join(writers))
            print(writersList)

        except TimeoutException:
            try:
                writers_div_element = WebDriverWait(driver, 5, 0.5).until(
                    EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Writer')]/following-sibling::div"))
                )
                writers = [t for t in re.findall(r'([A-Z][a-z]* [A-Z][a-z]*(?: [A-Z][a-z]*)?)', writers_div_element.text)]
                writersList.append(",".join(writers))
                print(writersList)

            except NoSuchElementException:
                print("Element bulunamadı veya bekleme süresi aşıldı.")
                writersList.append(None)

        stars_div_element = WebDriverWait(driver, 5, 1).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Star')]/following-sibling::div")))
        stars = [t for t in re.findall(r'[A-Z][a-z]* [A-Z][a-z]*', stars_div_element.text)]
        starsList.append(",".join(stars))
        # count += 1
        # if count == 2:
        #     break
    return description_list, directorList, writersList, starsList

description_list, directorList, writersList, starsList = getTop250FilmDetails()

data = {
    "top_250_film": top_250_film,
    "top_250_film_rating": top_250_film_rating,
    'Year': year_list,
    'Time': time_list,
    "description": description_list,
    "director": directorList,
    'writers': writersList,
    'stars': starsList
}

df = pd.DataFrame(data)
print(df)
print(df.info())
df.to_csv('../datas/imdbPullData.csv', index=False)

driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import schedule


service = Service("C:/Users/HP/Documents/Development/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = service, options = options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(2)

cache_click = driver.find_element(By.CLASS_NAME, "cc_btn_accept_all")
cache_click.click()

time.sleep(2)

lang_click = driver.find_element(By.ID, "langSelect-EN")
lang_click.click()

time.sleep(5)

def powerup():
    try:
        crate_click = driver.find_element(By.XPATH, "(//div[@class='crate upgrade enabled'])[last()]").click()
    except NoSuchElementException:
        powerup_click = driver.find_element(By.XPATH, "(//div[@class='product unlocked enabled'])[last()]").click()

playsGame = True
schedule.every(5).seconds.do(powerup)

while playsGame:
    cookie_clicker = driver.find_element(By.ID, "bigCookie")
    cookie_clicker.click()
    
    try:
        schedule.run_pending()
    except NoSuchElementException:
        continue

driver.quit()
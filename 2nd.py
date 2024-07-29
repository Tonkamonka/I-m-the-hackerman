import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


print("trying to get rid of the window popping up asking me to select the default search engine.but its still there ffs")
chrome_options: Options = Options()
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(chrome_options)
driver.get('https://www.saucedemo.com/v1/')

try:
    driver.find_element(By.XPATH, "//*[@id='user-name']")
    print("Username section found.")
except:
    print("Username section NOT found.")

try:
    driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    print("Password section found.")
except:
    print("Password section NOT found.")



time.sleep(10)

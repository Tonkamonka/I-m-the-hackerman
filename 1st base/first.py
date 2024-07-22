import selenium
from selenium import webdriver
# installing the time package in general
import time
from selenium.webdriver.common.by import By
# variables
driver = webdriver.Chrome()
# running the test, opened the chrome, and boom shakalalaka
driver.get('https://www.saucedemo.com/v1/index.html')
driver.maximize_window()
print("Az egy merida dual thrust")
username_input_field = driver.find_element(By.XPATH,"//*[@id='user-name']")
password_input_field = driver.find_element(By.XPATH,"//*[@id='password']")
login_input_field = driver.find_element(By.XPATH,"//*[@type='submit']")
username_input_field.send_keys("standard_user")
print("Wow this guy knows what he is doing")
password_input_field.send_keys("secret_sauce")
print("Drink water!!!!4444444")
login_input_field.click()
headline_field = driver.find_element(By.XPATH,"//*[@class='product_label']")
time.sleep(5)
assert headline_field.text == "Products"
print("Can I get an ohhh yeah?")




# delaying the process to close down for X amount
time.sleep(10)


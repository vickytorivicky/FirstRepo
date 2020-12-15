from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Chrome()
# Verify on sign up if the password doesn't meet requirements an error message will be shown
driver.get("http://jobmight.com/session/partner/signup")
first_name_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "firstName"))))
first_name_input.send_keys ("Vicky")
last_name_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "lastName"))))
last_name_input.send_keys("Victoria")
email_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys ("vickysvictoria9@gmail.com")
password_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
password_input.send_keys ("_______")
next_button = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]"))))
next_button.click()
error_notification = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.XPATH, "//p[@class='MuiFormHelperText-root MuiFormHelperText-contained Mui-error MuiFormHelperText-filled']"))))
assert error_notification.text == "Password must contain a capital letter and symbol"

driver.quit()
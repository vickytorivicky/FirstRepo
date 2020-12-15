from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Chrome()
# Verify signing up as a Bounty Hunter user
driver.get("http://jobmight.com/session/partner/signup")
first_name_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "firstName"))))
first_name_input.send_keys ("Tim")
last_name_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "lastName"))))
last_name_input.send_keys("Testero")
email_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys ("timtestero@gmail.com")
password_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
password_input.send_keys ("timTest)")
next_button = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]"))))
next_button.click()

recruiting_experience_field = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.NAME, "recruitingExperience"))))
recruiting_experience_field.click()
recruiting_experience_field_option = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//option[contains(@value,'0')]"))))
recruiting_experience_field_option.click()
check_box_field = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//span[@class='MuiIconButton-label']"))))
check_box_field.click()
close_button = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Close')]"))))
close_button.click()
sign_up_button = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Sign up')]"))))
sign_up_button.click()

driver.quit()
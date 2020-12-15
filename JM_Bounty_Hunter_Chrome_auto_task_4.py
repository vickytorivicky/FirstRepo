from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Chrome()
# Verify that logging in with existing email but incorrect password will prompt a pop-up saying that credentials are not valid
driver.get("http://jobmight.com/session/partner/signin")
email_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys("vickysvictoria9@gmail.com")
password_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
password_input.send_keys("testing_time")
login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()
popup_window = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-gutterBottom']")))
assert popup_window.text == "Invalid credentials, could not log you in."

driver.quit()
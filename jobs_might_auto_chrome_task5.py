from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/emp/signin")

forgotpassword_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Forgot password?')]")))
forgotpassword_button.click()

email_input: object = WebDriverWait(driver, 60).until((EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))))
email_input.send_keys("vickytorivicky@gmail.com")

reset_password_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Reset Password')]")))
reset_password_button.click()
#verify confirmation message
confirmation_message = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//form[contains(text(),'Email successfully sent. If you have registered an')]")))

driver.quit()
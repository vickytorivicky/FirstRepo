from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Chrome()
# Verify forgot password functionality: after the user entered email the message is shown that the email was sent
driver.get("http://jobmight.com/session/partner/signin")
forgotpassword_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Forgot password?')]")))
forgotpassword_button.click()
# Redirecting to a proper page after clicking "Forgot password?" does not work
driver.quit()
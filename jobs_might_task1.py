from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/emp/signin")
email_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys("vickytorivicky@gmail.com")
password_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
password_input.send_keys("testingQA)")
#wait until log in button is clickable
login_button = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//button[contains(@type,'submit')]"))))
login_button.click()
#verify banner text (to see where user will be taken next)-two lines below can be run for that
#banner = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div/div[1]')))
#assert banner.text == "Feedback on job applications, guaranteed."

driver.quit()
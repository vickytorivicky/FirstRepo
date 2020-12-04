from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Firefox()
driver.get("http://jobmight.com/session/emp/signup")

email_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys("tester112@gmail.com")

company_name_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "companyName"))))
company_name_input.send_keys("Techno market")

password_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
password_input.send_keys("testing)T123)")

your_full_name_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "yourName"))))
your_full_name_input.send_keys("Tom Tester")

next_button = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]"))))
next_button.click()

company_website_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.XPATH, "//input[contains(@type,'text')]"))))
company_website_input.send_keys("www.techno.com")

zip_code_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.XPATH, "//input[contains(@type,'number')]"))))
zip_code_input.send_keys("11223")

telephone_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.XPATH, "//input[contains(@type,'tel')]"))))
telephone_input.send_keys("7181234567")

your_title_field = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//div[@id='demo-simple-select']"))))
your_title_field.click()

your_title_option = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'HR')]"))))
your_title_option.click()
your_title_option.click()

back_button = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Back')]"))))
back_button.click()
driver.quit()
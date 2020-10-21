
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")



contact_us_navigation_bar_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div/div[13]/a")))
contact_us_navigation_bar_btn.click()

name_input_field = WebDriverWait(driver,30).until((EC.visibility_of_element_located((By.NAME, "Name"))))
name_input_field.send_keys("Name Surname")
email_input_field = WebDriverWait(driver,30).until((EC.visibility_of_element_located((By.NAME, "e-mail"))))
email_input_field.send_keys("mail@example.com")
phone_input_field = WebDriverWait(driver,30).until((EC.visibility_of_element_located((By.NAME, "Phone"))))
phone_input_field.send_keys("111222333")
country_input_field = WebDriverWait(driver,30).until((EC.visibility_of_element_located((By.NAME, "Country"))))
country_input_field.send_keys("USA")
send_btn = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[17]/div/div/div[2]/div/form/div[2]/div[6]/button')))
send_btn.click()

def verifyMessage():
    message = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[17]/div/div/div[2]/div/form/div[1]')))
assert message.text == "Thank you! we will contact you soon"

driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://jobmight.com/dashboard")
def verifyLogo():
# Wait until logo on the footer is visible and verify its text
   logo = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@style,'display: block; justify-content: left; margin: 0px auto;')]")))
   assert logo.text == "JobsMight"

driver.quit()
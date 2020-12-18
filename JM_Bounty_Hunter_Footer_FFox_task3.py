from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Firefox()
driver.get("http://jobmight.com/bounty-hunter/stripe-dashboard")
# Verify the name of the link "Terms" and if it redirects to a new page
terms_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Terms')]")))
assert terms_name.text == "Terms"
terms_link = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Terms')]"))))
terms_link.click()

driver.quit()

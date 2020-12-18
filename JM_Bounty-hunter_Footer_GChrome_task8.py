from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Chrome()
driver.get("http://jobmight.com/bounty-hunter/stripe-dashboard")
# Verify the name of the link "Pricing" and if it redirects to a new page
pricing_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Pricing')]")))
assert pricing_name.text == "Pricing"
pricing_link = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Pricing')]"))))
pricing_link.click()

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Chrome()
driver.get("http://jobmight.com/bounty-hunter/stripe-dashboard")
# Verify the name of the link "About" and if it redirects to a new page
about_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'About')]")))
assert about_name.text == "About"
about_link = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'About')]"))))
about_link.click()

driver.quit()
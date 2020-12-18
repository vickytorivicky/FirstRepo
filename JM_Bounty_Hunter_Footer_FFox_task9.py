from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Firefox()
driver.get("http://jobmight.com/bounty-hunter/stripe-dashboard")
# Verify the name of the link "*NEW* Bounties" and if it redirects to a new page
new_bounties_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'*NEW* Bounties')]")))
assert new_bounties_name.text == "*NEW* Bounties"
new_bounties_link = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'*NEW* Bounties')]"))))
new_bounties_link.click()

driver.quit()
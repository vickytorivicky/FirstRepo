from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/emp/signup")

email_input: object = WebDriverWait(driver, 60).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys ("vickytorivicky@gmail.com")

company_name_input: object = WebDriverWait(driver, 60).until((EC.visibility_of_element_located((By.NAME, "companyName"))))
company_name_input.send_keys("Company")

password_input: object = WebDriverWait(driver, 60).until((EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))))
password_input.send_keys ("_______")

your_full_name_field = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//body/div[@id='root']/div[contains(@class,'topbar-fixed')]/div[@class='content-wrap position-relative']/div[@class='scrollable-content']/div[@id='content']/div[@class='signup flex flex-column w-full h-full-screen']/div[@class='justify-center d-flex align-items-baseline w-full h-full']/div[@class='MuiPaper-root MuiCard-root signup-card position-relative y-center MuiPaper-elevation1 MuiPaper-rounded']/div[@class='signup-wrapper']/div[@class='MuiGrid-root align-items-center MuiGrid-container']/div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-7 MuiGrid-grid-md-7 MuiGrid-grid-lg-7']/div[@class='p-9']/div/form/div[4]/div[1]/div[1]/input[1]"))))
your_full_name_field.click()
#check for an error notification
error_notification = WebDriverWait(driver, 60).until((EC.visibility_of_element_located((By.XPATH, "//p[contains(@class,'MuiFormHelperText-root MuiFormHelperText-contained Mui-error MuiFormHelperText-filled')]"))))
assert error_notification.text == "Password must contain a capital letter and symbol"

driver.quit ()

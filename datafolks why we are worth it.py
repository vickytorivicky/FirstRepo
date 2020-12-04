from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

see_why_we_are_worth_it_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[@data-elem-id=1551635176282]/u")))
see_why_we_are_worth_it_btn.click()


new_page_header = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[6]/div/div/div[3]/div")))
assert new_page_header.text == "Areas of expertise"


driver.quit()

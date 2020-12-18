from selenium import webdriver

driver = webdriver.Firefox()
# Verify Footer's text: "EMPLOYER RESOURCES"
driver.get("http://jobmight.com/bounty-hunter/stripe-dashboard")
emp_resources = driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/header/div/div/div/div[2]/div/h3")
print(emp_resources.text)

driver.quit()


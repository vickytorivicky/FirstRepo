from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://jobmight.com/dashboard")
# Verify Footer's text: "Fast Feedback. Accountable Hiring."
fast_feedback_accountable_hiring = driver.find_element_by_xpath("//div[@id='first-txt']/h6")

print(fast_feedback_accountable_hiring.text)
driver.quit()
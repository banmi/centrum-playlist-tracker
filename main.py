from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/trial-of-the-stones")

# Riddle of Stone
stone_input = browser.find_element_by_xpath("//input[@id='r1Input']")
stone_butn = browser.find_element_by_xpath("//button[@id='r1Btn']")
stone_code = browser.find_element_by_xpath("//div[@id='passwordBanner']/h4")

# Riddle of Secrets
secret_input = browser.find_element_by_xpath("//input[@id='r2Input']")
secret_butn = browser.find_element_by_xpath("//button[@id='r2Butn']")

# The Two Merchants
merchant_locator = browser.find_element_by_xpath("//p[text() = '3000'] /.. /span/b")
merchant_input = browser.find_element_by_id('r3Input')
merchant_butn = browser.find_element_by_css_selector("button#r3Butn")

# Check
check_butn = browser.find_element_by_css_selector("button#checkButn")
complete_msg = browser.find_element_by_css_selector("div#trialCompleteBanner > h4")

# Manipulate elements
stone_input.send_keys("rock")
stone_butn.click()
password = stone_code.get_attribute("innerHTML")
print(password)
secret_input.send_keys(password)
secret_butn.click()
name = merchant_locator.get_attribute("innerHTML")
print(name)
merchant_input.send_keys(name)
merchant_butn.click()
check_butn.click()

assert complete_msg.text == "Trial Complete"
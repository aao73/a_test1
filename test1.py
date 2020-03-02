from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("окей гугл")
elem.send_keys(Keys.RETURN)
print("мы на странице окей гугл")
driver.back()
elem = driver.find_element_by_name("q")
elem.send_keys("Я не гугл")
elem.send_keys(Keys.RETURN)
print(driver.title)
assert "окей гугл" not in driver.title
print("мы находимся на другой странице")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(r'C:\Users\lenovo\eclipse-workspace\libs\chromedriver')

driver.get("https://www.python.org")

search_bar = driver.find_element_by_name("q")

search_bar.clear()
search_bar.send_keys("python")
search_bar.send_keys(Keys.RETURN)

print(driver.current_url)

driver.close()


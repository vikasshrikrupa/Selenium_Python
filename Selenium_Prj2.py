from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome(r'C:\Users\lenovo\eclipse-workspace\libs\chromedriver')

driver.implicitly_wait(9)

driver.get("https://wiki.python.org")

search_bar = driver.find_element_by_id("searchinput")

search_bar.clear()
search_bar.send_keys("Beginner")
search_bar.send_keys(Keys.RETURN)

time.sleep(4)

#op1 = Select(driver.find_element_by_xpath("/html/body/div[2]/div[3]/ul/li[5]/form/div/select"))

op1= Select(driver.find_element_by_xpath("//*[@id='sidebar']/div[3]/ul/li[5]/form/div/select"))

op1.select_by_visible_text('Raw Text')

time.sleep(9)

driver.close()

print("Complete Successfully!!")

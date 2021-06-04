from selenium import webdriver
from PIL import Image
import time

# take screenshot
driver = webdriver.Chrome();

driver.implicitly_wait(9)

driver.get('https://wiki.python.org');
element = driver.find_element_by_id("logo");
location = element.location;
size = element.size;
driver.save_screenshot("pageImage.png");

# crop image
x = location['x'];
y = location['y'];
width = location['x']+size['width'];
height = location['y']+size['height'];
im = Image.open('pageImage.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('element.png')

time.sleep(9)

driver.quit()

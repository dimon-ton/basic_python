from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

path = r'C:\Users\saich\Documents\basic_python\EP.13_automate_web\msedgedriver.exe'
service = Service(path)
driver = webdriver.Edge(service=service)

url = 'https://www.google.com'
driver.get(url)



elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys('wikipedia')
time.sleep(3)
elem.send_keys(Keys.RETURN)
time.sleep(2)

driver.set_window_size(1500, 1000)

for i in range(2, 21, 2):
    driver.execute_script('window.scrollTo(0,{})'.format(i*100))
    time.sleep(1)
    driver.save_screenshot(r'EP.13_automate_web\capture{}.png'.format(i))


time.sleep(2)
driver.close()
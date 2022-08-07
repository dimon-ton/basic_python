from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
from datetime import datetime
from write_csv import *

path = r'C:\Users\saich\Documents\basic_python\EP.13_automate_web\msedgedriver.exe'
service = Service(path)

options = webdriver.EdgeOptions()
options.headless = True # Don't launch browser

driver = webdriver.Edge(service=service, options=options)

url = 'http://www.uncle-machine.com/login/'
driver.get(url)

driver.set_window_size(1920, 1080)

time.sleep(2)
username = driver.find_element(By.ID, "username")
username.send_keys('pimon777@gmail.com')

password = driver.find_element(By.ID, "password")
password.send_keys('1234')

password.send_keys(Keys.RETURN)

sensor_url = 'http://www.uncle-machine.com/sensor/'
driver.get(sensor_url)

search = driver.find_element(By.ID,'sid')
sensorid = 'ss_1001'
search.send_keys(sensorid)
search.send_keys(Keys.RETURN)

time.sleep(1)

temp = driver.find_element(By.CLASS_NAME, 'temp')
humid = driver.find_element(By.CLASS_NAME, 'humid')


stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

temp = temp.text.split(' ')[1]
humid = humid.text.split(' ')[1]


print(temp)
print(humid)

data = [sensorid, temp, humid, stamp]
write(data)

time.sleep(3)
driver.quit()

print('----success---')
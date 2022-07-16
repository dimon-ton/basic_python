from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

path = r'C:\Users\saich\Documents\basic_python\EP.13_automate_web\msedgedriver.exe'
service = Service(path)
driver = webdriver.Edge(service=service)

url = 'http://www.uncle-machine.com/login/'
driver.get(url)

driver.set_window_size(1920, 1080)

time.sleep(2)
username = driver.find_element(By.ID, "username")
username.send_keys('pimon777@gmail.com')

password = driver.find_element(By.ID, "password")
password.send_keys('1234')

password.send_keys(Keys.RETURN)

add_url = 'http://www.uncle-machine.com/addproduct/'
driver.get(add_url)

time.sleep(2)
product_name = 'Apple'
product_price = 200
prduct_detail = 'apple detail'

name_elem = driver.find_element(By.ID, 'name')
price_elem = driver.find_element(By.ID, 'price')
detail_elem = driver.find_element(By.ID, 'detail')

name_elem.send_keys(product_name)
price_elem.send_keys(product_price)
detail_elem.send_keys(prduct_detail)

browse = driver.find_element(By.XPATH, '//*[@id="photo"]')
img_path = r'C:\Users\saich\Documents\basic_python\EP.13_automate_web\Apple.jpg'
browse.send_keys(img_path)

time.sleep(2)
submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/form/button')
submit_button.click()

time.sleep(20)
driver.close()
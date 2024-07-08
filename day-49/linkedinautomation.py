from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium
import time


driver_path = "/Users/davitmirzoevi/Desktop/chromedriver"

service = Service(executable_path=driver_path)
driver = selenium.webdriver.Chrome(service=service)
url = "https://www.linkedin.com/jobs/search/?currentJobId=3968149023&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
my_email = "dmirzoevi@icloud.com"
my_pass = "mix23!Dix"
mob_number = "599544130"


driver.get(url)
time.sleep(2.5)
try:
    driver.find_element(By.XPATH, "/html/body/div[2]/a[1]").click()
except:
    driver.close()
    time.sleep(0.5)
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/a[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(my_email)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(my_pass)
driver.find_element(By.CLASS_NAME, "btn__primary--large").click()
time.sleep(1)
#Applying
apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
apply_button.click()
#entering number
time.sleep(0.5)
number_input = driver.find_element(By.CLASS_NAME, 'artdeco-text-input--input')
if number_input == "":
    number_input.send_keys(mob_number)
#next Buttons
driver.find_element(By.XPATH, '//button/span[text()="Next"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//button/span[text()="Next"]').click()


driver.find_element(By.CLASS_NAME, 't-14').click()
#Review Button

driver.find_element(By.XPATH, '//button/span[text()="Review"]').click()

#Submit App Button
driver.find_element(By.XPATH, '//button[@aria-label="Submit application"]').click()


time.sleep(5)

driver.quit()

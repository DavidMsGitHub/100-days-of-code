import selenium
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "/Users/davitmirzoevi/Desktop/chromedriver"

service = Service(executable_path=driver_path)
driver = selenium.webdriver.Chrome(service=service)

driver.get("https://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
sign_up_btn = driver.find_element(By.CLASS_NAME, "btn")

f_name.send_keys("Davita")
l_name.send_keys("Davitavar")
email.send_keys("Davita@gmail.com")
sign_up_btn.click()


time.sleep(5)
driver.quit()

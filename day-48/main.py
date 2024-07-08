from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/davitmirzoevi/Desktop/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
gelasha = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
gela = gelasha.find_elements(By.TAG_NAME, "li")

events = {}
num = 0

for names in gela:
    name = names.text
    the_name = name.split()
    date = the_name[0]
    event_name = " ".join(the_name[1:])
    events[num] = {"date": date,
                   "event": event_name}
    num += 1

print(events)



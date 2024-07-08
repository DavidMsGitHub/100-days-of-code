from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium
import time
from selenium.webdriver.chrome.options import Options


driver_path = "/Users/davitmirzoevi/Desktop/chromedriver"
url = 'https://www.instagram.com'
my_email = "dato2006213@gmail.com"
my_pass = "Dato2006mix23!Dix"

class InstaFollower:
    def __init__(self):
        self.chromedriver = driver_path
        self.service = Service(executable_path=self.chromedriver)
        self.driver = selenium.webdriver.Chrome(service=self.service)
        self.text_to_send = ""

    def main(self):
        self.driver.get(url)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(my_email)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(my_pass)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(8)
        self.driver.get("https://www.instagram.com/cristiano/followers/")
        time.sleep(4)
        self.driver.find_element(By.XPATH, f'//a[@href="/cristiano/followers/"]').click()
        time.sleep(2)
        self.follow()
        time.sleep(500)
        self.driver.quit()

    def follow(self):
        self.driver.find_element(By.CSS_SELECTOR, "div .x9f619 .x1n2onr6 .x1ja2u2z .xdt5ytf .x2lah0s .x193iq5w .xeuugli .xamitd3 .x78zum5").click()
        time.sleep(5)
        # for buttons in gelasha:
        #     buttons.click()
        scr1 = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        print("Scrolled")



insta = InstaFollower()
insta.main()
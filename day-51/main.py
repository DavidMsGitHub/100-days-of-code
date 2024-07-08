from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium
import time
from selenium.webdriver.chrome.options import Options


# Set options for headless bro

driver_path = "/Users/davitmirzoevi/Desktop/chromedriver"
promised_up = 100
promised_down = 100
my_email = "iceobladey22@gmail.com"
my_pass = "Dato2006mix23!Dix"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chromedriver = driver_path
        self.service = Service(executable_path=self.chromedriver)
        self.driver = selenium.webdriver.Chrome(service=self.service)
        self.text_to_send = ""

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(4)
        self.driver.find_element(By.TAG_NAME, "input").send_keys(my_email)
        self.driver.find_element(By.XPATH, "//button[.//span/span[contains(text(),'Next')]]").click()
        time.sleep(1)
        if self.driver.find_element(By.XPATH, f'//span[text()="Enter your phone number or username"]'):
            print("the verify detected")
            self.driver.find_element(By.TAG_NAME, 'input').send_keys("davidspython", Keys.ENTER)
            time.sleep(1)
            self.driver.find_element(By.NAME, 'password').send_keys(my_pass, Keys.ENTER)
            time.sleep(5)
            self.driver.find_element(By.CSS_SELECTOR, 'div .public-DraftStyleDefault-block').send_keys(self.text_to_send)
            self.driver.find_element(By.XPATH, '//span[contains(text(), "Post")]').click()
            print("button clicked")
            time.sleep(10)
            self.driver.quit()


    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "span.start-text").click()
        time.sleep(40)
        self.down_speed = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up_speed = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.text_to_send = f"Hey @MagtiCom, why is my internet speed {self.down_speed} DOWN / {self.up_speed} UP, when i was promised to get {promised_down} DOWN /{promised_up} UP????"
        time.sleep(3)

    def start(self):
        self.get_internet_speed()
        if self.down_speed < promised_down or self.up_speed < promised_up:
            self.tweet_at_provider()


bot = InternetSpeedTwitterBot()
bot.start()


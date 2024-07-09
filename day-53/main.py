import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.action_chains import ActionChains

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15'
}

driver_path = "/Users/davitmirzoevi/Desktop/chromedriver"
forms_url = "https://docs.google.com/forms/d/e/1FAIpQLSd45avh4cTZOslgdPqWeRaa-DKRrOnTjgXZc0rQlYjEbccOyA/viewform?usp=sf_link"
url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"


class Scraper:
    def __init__(self):
        self.items = []
        self.links = []
        self.prices_list = []
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.get_html()
        self.bs_scrape()


    def get_html(self):
        self.driver.get("https://www.zara.com/ge/en/man-sale-l7139.html?v1=2439352")
        time.sleep(2)
        # for i in range(5):
        #     time.sleep(1)
        #     self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        # time.sleep(3)
        self.html = self.driver.page_source

    def bs_scrape(self):
        self.soup = BeautifulSoup(self.html, "html.parser")
        items_with_links = self.soup.find_all("a", class_= ["product-link", "_item"])
        price_element = self.soup.find_all("span", class_="price-old__amount")


        for item in items_with_links:
            name = item.getText()
            link = item["href"]
            self.items.append(name)
            self.links.append(link)

        for prices in price_element:
            self.prices_list.append(prices.getText())


        for i in range(8):
            print(self.items[i], self.links[i], self.prices_list[i])

Scraper()
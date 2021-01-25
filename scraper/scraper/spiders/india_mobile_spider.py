import time

from scrapy import Spider, Request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class IndiaMobileSpider(Spider):
    name = 'india_mobile_spider'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.driver = webdriver.Chrome()

    def start_requests(self):
        start_url = "https://gadgets.ndtv.com/mobiles/phone-finder?facet[" \
                    "market_status]=1&sort=popularity_score&order=desc"
        self.driver.get(start_url)
        # self.scroll()
        urls = self.driver.find_elements_by_css_selector('div._lpdwgt._flx a._lpimga')
        urls = [u.get_attribute('href') for u in urls]
        print(urls)
        self.driver.close()
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = dict()
        table_rows = response.css('div._st-wrp table tr')

        for row in table_rows:
            parts = row.css('td::text').getall()
            if len(parts) >= 2:
                k = parts[0]
                v = parts[1]
                item[k] = v
        if len(item.keys()) > 0:
            yield item

    def scroll(self):
        wait = WebDriverWait(self.driver, 20)
        player = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#jsw'))
        )
        self.driver.execute_script('arguments[0].remove();', player)
        should_wait = True
        while True:
            try:
                if should_wait:
                    popup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__notify')))
                    self.driver.execute_script('arguments[0].remove();', popup)
                    should_wait = False
                btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.load-more._btn')))
                print('CLICK')
                self.driver.execute_script('arguments[0].scrollIntoView();', btn)
                btn.click()
                time.sleep(2)
            except:
                print('ERROR')
                break

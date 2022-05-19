from math import ceil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class ResponsiveTester:

    def __init__(self, urls):
        self.browser = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options)
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [500, 960, 1366, 1920]

    def screenshot(self, url):
        BROWSER_HEIGHT = 1055
        self.browser.get(url)
        for size in self.sizes:
            self.browser.set_window_size(size, BROWSER_HEIGHT)
            self.browser.execute_script("window.scrollTo(0,0)")
            time.sleep(2)
            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight")
            total_sections = ceil(scroll_size / BROWSER_HEIGHT)
            for section in range(total_sections + 1):
                browser_height_js = self.browser.execute_script(
                    "return window.innerHeight")
                self.browser.execute_script(
                    f"window.scrollTo(0, {(section) * (browser_height_js-64)})")
                self.browser.save_screenshot(
                    f"screenshots/{size}x{section+1}.png")
                time.sleep(1)

    def start(self):
        for url in self.urls:
            self.screenshot(url)

    def finish(self):
        self.browser.quit()


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

tester = ResponsiveTester(["https://nomadcoders.co", "https://google.com"])
tester.start()
tester.finish()

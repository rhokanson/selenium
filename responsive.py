from math import ceil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

BROWSER_HEIGHT = 1055

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(
    ChromeDriverManager().install(), options=chrome_options)

browser.get("https://nomadcoders.co")
browser.maximize_window()

sizes = [500, 960, 1366, 1920]

for size in sizes:
    browser.set_window_size(size, BROWSER_HEIGHT)
    time.sleep(3)
    scroll_size = browser.execute_script("return document.body.scrollHeight")
    total_sections = ceil(scroll_size / BROWSER_HEIGHT)
    for section in range(total_sections):
        browser.execute_script(
            f"window.scrollTo(0, {section+1 * BROWSER_HEIGHT})")


browser.quit()

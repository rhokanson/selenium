from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


class GoogleKeywordScreenShooter:
    def __init__(self, keyword, screenshots_dir):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir

    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        shitty_element = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Wt5Tfe")))

        self.browser.execute_script(
            """
        const shitty = arguments[0];
        shitty.parentElement.removeChild(shitty)
        """,
            shitty_element,
        )

        search_results = self.browser.find_element_by_id(
            "rso").find_elements_by_class_name("g")
        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index}.png")

    def finish(self):
        self.browser.quit()


domain_competitors = GoogleKeywordScreenShooter("buy domain", "screenshots")
domain_competitors.start()
domain_competitors.finish()
python_competitors = GoogleKeywordScreenShooter("python book", "screenshots")
python_competitors.start()
python_competitors.finish()


# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)


# browser = webdriver.Chrome(
#     ChromeDriverManager().install(), options=chrome_options)

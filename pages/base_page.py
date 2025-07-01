from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
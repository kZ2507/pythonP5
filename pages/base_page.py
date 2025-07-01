from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(EC.presence_of_element_located(args))
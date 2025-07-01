from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.alerts_locs import *
import allure

class AlertPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        self.browser.get('https://www.qa-practice.com/elements/alert/alert')

    def find_alert(self):
        return self.find(alert)

    def alert_click(self):
        self.find_alert().click()

    def switch_to_alert_and_accept(self):
        alert = WebDriverWait(self.browser, 10).until(
            EC.alert_is_present()
        )
        alert_text = alert.text
        alert.accept()
        return alert_text
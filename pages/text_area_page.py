from pages.base_page import BasePage
from locators.text_area_locs import *
import allure

class TestAreaPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        with allure.step('Open page'):
            self.browser.get('https://www.qa-practice.com/elements/textarea/single')

    def find_area(self):
        return self.find(area_selector)

    def area_is_displayed(self):
        return self.find_area().is_displayed()

    def find_name(self):
        return self.find(name_selector)

    @property
    def name_text(self):
        return self.find_name().text

    def area_send_text(self):
        self.find_area().click()
        self.find_area().send_keys('text text text')

    def find_submit(self):
        return self.find(submit_selector)

    def submit_click(self):
        self.find_submit().click()

    def find_result(self):
        return self.find(result_selector)

    @property
    def result_text(self):
        return self.find_result().text





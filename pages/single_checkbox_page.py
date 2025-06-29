from pages.base_page import BasePage
from locators.single_checkbox_locs import *
import allure

class SingleCheckboxPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        with allure.step('Open page'):
            self.browser.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')

    def find_checkbox(self):
        return self.find(checkbox_selector)

    def checkbox_is_displayed(self):
        return self.find_checkbox().is_displayed()

    def checkbox_click(self):
        self.find_checkbox().click()

    def find_submit(self):
        return self.find(submit_selector)

    def submit_click(self):
        self.find_submit().click()

    def find_result(self):
        return self.find(result_selector)

    @property
    def result_text(self):
        return self.find_result().text
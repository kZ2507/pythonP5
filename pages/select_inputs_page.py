from pages.base_page import BasePage
from locators.select_inputs_locs import *
import allure

class SelectInputsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        with allure.step('Open page'):
            self.browser.get('https://www.qa-practice.com/elements/select/single_select')

    def find_select(self):
        return self.find(select_selector)

    def select_is_displayed(self):
        return self.find_select().is_displayed()

    def find_name(self):
        return self.find(name_selector)

    @property
    def name_text(self):
        return self.find_name().text

    def select_click(self):
        self.find_select().click()
        self.find(option_selector).click()

    def find_submit(self):
        return self.find(submit_selector)

    def submit_click(self):
        self.find_submit().click()

    def find_result(self):
        return self.find(result_selector)

    @property
    def result_text(self):
        return self.find_result().text
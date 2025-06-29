import allure

from locators.text_input_locs import *
from pages.base_page import BasePage
import pyautogui

class TextInputPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        with allure.step('Open page'):
            self.browser.get('https://www.qa-practice.com/elements/input/simple')

    def find_field(self):
        return self.find(field_selector)

    def field_is_displayed(self):
        return self.find_field().is_displayed()

    def field_send_correct_text(self):
        self.find_field().click()
        self.find_field().send_keys('textTEXT1-_')
        pyautogui.press('enter')

    def field_send_incorrect_text(self):
        self.find_field().click()
        self.find_field().send_keys('text!@#')
        pyautogui.press('enter')

    def field_send_short_text(self):
        self.find_field().click()
        self.find_field().send_keys('t')
        pyautogui.press('enter')

    def field_send_long_text(self):
        self.find_field().click()
        self.find_field().send_keys('texttexttexttexttexttextte')
        pyautogui.press('enter')

    def find_error(self):
        return self.find(error_selector)

    @property
    def error_text(self):
        return self.find_error().text

    def find_result(self):
        return self.find(result_selector)

    @property
    def result_text(self):
        return self.find_result().text
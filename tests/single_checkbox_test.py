from selenium.common import NoSuchElementException
from pages.single_checkbox_page import SingleCheckboxPage
import allure

@allure.feature('Single Checkbox Page')
@allure.title('Single Checkbox is displayed')
def test_checkbox_exist(browser):
    checkbox_page = SingleCheckboxPage(browser)
    checkbox_page.open_page()
    assert checkbox_page.checkbox_is_displayed()

@allure.feature('Single Checkbox Page')
@allure.title('Single Checkbox is clicked')
def test_checkbox_click(browser):
    checkbox_page = SingleCheckboxPage(browser)
    checkbox_page.open_page()
    checkbox_page.checkbox_click()
    checkbox_page.submit_click()
    assert 'select me or not' == checkbox_page.result_text

@allure.feature('Single Checkbox Page')
@allure.title('Single Checkbox is not clicked')
def test_checkbox_not_click(browser):
    checkbox_page = SingleCheckboxPage(browser)
    checkbox_page.open_page()
    checkbox_page.submit_click()
    try:
        checkbox_page.find_result()
        assert False
    except NoSuchElementException:
        assert True

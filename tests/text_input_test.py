from pages.text_input_page import TextInputPage
import allure

@allure.feature('Text Input Page')
@allure.title('Text Input is displayed')
def test_field_exist(browser):
    select_page = TextInputPage(browser)
    select_page.open_page()
    assert select_page.field_is_displayed()

@allure.feature('Text Input Page')
@allure.title('Text Input is sent correct text')
def test_field_correct_text(browser):
    select_page = TextInputPage(browser)
    select_page.open_page()
    select_page.field_send_correct_text()
    assert 'textTEXT1-_' == select_page.result_text

@allure.feature('Text Input Page')
@allure.title('Text Input error')
def test_field_incorrect_text(browser):
    select_page = TextInputPage(browser)
    select_page.open_page()
    select_page.field_send_incorrect_text()
    assert 'Enter a valid string consisting of letters, numbers, underscores or hyphens.' == select_page.error_text

@allure.feature('Text Input Page')
@allure.title('Text Input error')
def test_field_short_text(browser):
    select_page = TextInputPage(browser)
    select_page.open_page()
    select_page.field_send_short_text()
    assert 'Please enter 2 or more characters' == select_page.error_text

@allure.feature('Text Input Page')
@allure.title('Text Input error')
def test_field_long_text(browser):
    select_page = TextInputPage(browser)
    select_page.open_page()
    select_page.field_send_long_text()
    assert 'Please enter no more than 25 characters' == select_page.error_text
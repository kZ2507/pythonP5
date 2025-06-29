from pages.text_area_page import TestAreaPage
import allure

@allure.feature('Text Area Page')
@allure.title('Text Area is displayed')
def test_area_exist(browser):
    select_page = TestAreaPage(browser)
    select_page.open_page()
    assert select_page.area_is_displayed()

@allure.feature('Text Area Page')
@allure.title('Text Area name')
def test_area_name(browser):
    select_page = TestAreaPage(browser)
    select_page.open_page()
    select_page.find_name()
    assert 'Text area' == select_page.name_text

@allure.feature('Text Area Page')
@allure.title('Text Area is sent text')
def test_area_text(browser):
    select_page = TestAreaPage(browser)
    select_page.open_page()
    select_page.area_send_text()
    select_page.submit_click()
    assert 'text text text' == select_page.result_text
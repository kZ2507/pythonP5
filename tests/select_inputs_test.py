from pages.select_inputs_page import SelectInputsPage
import allure

@allure.feature('Select Inputs Page')
@allure.title('Select input is displayed')
def test_select_exist(browser):
    select_page = SelectInputsPage(browser)
    select_page.open_page()
    assert select_page.select_is_displayed()

@allure.feature('Select Inputs Page')
@allure.title('Select input name')
def test_field_name(browser):
    select_page = SelectInputsPage(browser)
    select_page.open_page()
    select_page.find_name()
    assert 'Choose language' == select_page.name_text

@allure.feature('Select Inputs Page')
@allure.title('Select input choose Ruby')
def test_select_option(browser):
    select_page = SelectInputsPage(browser)
    select_page.open_page()
    select_page.submit_click()
    select_page.select_click()
    select_page.submit_click()
    assert 'Ruby' == select_page.result_text
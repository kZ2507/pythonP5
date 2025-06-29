from pages.alerts_page import AlertPage
import allure

@allure.feature('Alert Page')
@allure.title('Check alert text')
def test_alert(browser):
    page = AlertPage(browser)
    page.open_page()
    page.alert_click()
    alert_text = page.switch_to_alert_and_accept()
    assert alert_text == "I am an alert!"

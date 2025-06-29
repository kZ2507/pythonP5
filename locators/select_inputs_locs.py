from selenium.webdriver.common.by import By

select_selector = (By.ID, 'id_choose_language')
name_selector = (By.CSS_SELECTOR, "[class='form-label requiredField']")
option_selector = (By.XPATH, "//option[contains(text(), 'Ruby')]")
submit_selector = (By.ID, 'submit-id-submit')
result_selector = (By.ID, 'result-text')
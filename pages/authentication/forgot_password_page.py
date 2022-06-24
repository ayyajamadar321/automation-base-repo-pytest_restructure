import time
import constants
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    _EMAIL_ID_INPUT_LOCATOR = (By.CSS_SELECTOR, '#email')
    _FORGOT_PASSWORD_TEXT_LOCATOR = (By.XPATH, "//a[contains(text(),'Forgot Password?')]")
    _PASSWORD_RESET_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'button.btn-primary')
    _PASSWORD_RESET_EMAIL_SENT_TEXT_LOCATOR = (By.XPATH, "//h3[contains(text(),'Password Reset Email Sent')]")
    _EMAIL_ERROR_TEXT_LOCATOR = (By.CSS_SELECTOR, "div.alert-wrapper p")

    def click_on_forgot_password_link(self):
        return self.click_on_element(self._FORGOT_PASSWORD_TEXT_LOCATOR)

    def enter_invalid_email_id(self, email):
        return self.enter_field_input(self._EMAIL_ID_INPUT_LOCATOR, email)

    def enter_correct_email_id(self, email):
        time.sleep(2)
        return self.enter_field_input(self._EMAIL_ID_INPUT_LOCATOR, email)

    def click_on_password_reset_button(self):
        return self.click_on_element(self._PASSWORD_RESET_BUTTON_LOCATOR)

    def validate_the_password_reset_email_sent_text(self):
        time.sleep(2)
        a = self.get_text_of_elements(self._PASSWORD_RESET_EMAIL_SENT_TEXT_LOCATOR)
        print(self.convert_list_to_string(a))
        res1 = self.convert_list_to_string(a) == constants.PASSWORD_RESET_EMAIL_SENT_TEXT
        return res1

    def check_incorrect_error_message(self):
        a = self.get_text_of_elements(self._EMAIL_ERROR_TEXT_LOCATOR)
        res1 = self.convert_list_to_string(a) == constants.ENTER_VALID_EMAIL
        print(self.convert_list_to_string(a))
        return res1

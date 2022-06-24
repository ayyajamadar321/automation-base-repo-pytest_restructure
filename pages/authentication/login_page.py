from __future__ import print_function

import os
import time

import allure
from selenium.webdriver.common.by import By

import constants
from pages.base_page import BasePage


class LoginPage(BasePage):
    _USER_NAME_LOCATOR = (By.CSS_SELECTOR, ".user-name")
    _END_TOUR_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[data-role="end"]')
    _GET_STARTED_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[alt="Right Arrow"]')
    _EMAIL_ID_INPUT_LOCATOR = (By.CSS_SELECTOR, '#loginId[placeholder="Email"]')
    _PASSWORD_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name="password"]#password')
    _FORGOT_PASSWORD_LINK_LOCATOR = (By.CSS_SELECTOR, "#password_wrapper a")
    _SIGNIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button.btn-primary")
    _EMAIL_ERROR_LOCATOR = (By.CSS_SELECTOR, "#loginId_alert_wrapper p")
    _PASSWORD_ERROR_LOCATOR = (By.CSS_SELECTOR, "#password_alert_wrapper p")
    _TITLE_TEXT_LOCATOR = (By.TAG_NAME, "Title")
    _PROFILE_DROPDOWN_LOCATOR = (
        By.XPATH,
        "//i[@class='isc-angle-down-solid up-arrow ml-1 rtl:ml-0']",
    )
    _SIGN_OUT_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".action-bar .mat-button-wrapper")
    _STUDENT_PROFILE_DROPDOWN_LOCATOR = (
        By.CSS_SELECTOR,
        "#parentStudentDashboardDiv app-header ngx-avatar",
    )
    _STUDENT_SIGN_OUT_BUTTON_LOCATOR = (By.ID, "signout_button")

    def close_cookies(self):
        return self.click_on_element(self._LANDING_PAGE_SOUNDS_GOOD_BUTN_LOCATOR)

    def check_title_text_display(self):
        time.sleep(2)
        print(self.selenium.title)
        return self.selenium.title == os.getenv("PAGE_TITLE")

    def check_title_text_after_logout(self):
        time.sleep(2)
        print("checking title text")
        print(self.selenium.title)
        return self.selenium.title == "Sign out | iSchoolConnect"

    def click_on_get_started_button(self):
        return self.click_on_element(self._GET_STARTED_BUTTON_LOCATOR)

    def enter_email_id(self, email):
        return self.enter_field_input(self._EMAIL_ID_INPUT_LOCATOR, email)

    def enter_password(self, password):
        return self.enter_field_input(self._PASSWORD_INPUT_LOCATOR, password)

    def click_on_sign_in_button(self):
        return self.click_on_element(self._SIGNIN_BUTTON_LOCATOR)

    def check_empty_error_message(self):
        email_error = self.get_text_of_elements(self._EMAIL_ERROR_LOCATOR)
        res1 = (
            self.convert_list_to_string(email_error) == constants.ENTER_REGISTERED_EMAIL
        )
        print(self.convert_list_to_string(email_error))
        password_error = self.get_text_of_elements(self._PASSWORD_ERROR_LOCATOR)
        res2 = (
            self.convert_list_to_string(password_error) == constants.PASSWORD_REQUIRED
        )
        print(self.convert_list_to_string(password_error))
        return res1 and res2

    def check_incorrect_error_message(self):
        email_error = self.get_text_of_elements(self._EMAIL_ERROR_LOCATOR)
        res1 = self.convert_list_to_string(email_error) == constants.ENTER_VALID_EMAIL
        print(self.convert_list_to_string(email_error))
        password_error = self.get_text_of_elements(self._PASSWORD_ERROR_LOCATOR)
        res2 = (
            self.convert_list_to_string(password_error)
            == constants.PASSWORD_CHARACTERS_VALIDATION
        )
        print(self.convert_list_to_string(password_error))
        return res1 and res2

    @allure.step("Username and Password is {0} {1}")
    def sign_in(self, email, password):
        res = self.enter_email_id(email)
        res1 = self.enter_password(password)
        res2 = self.click_on_sign_in_button()
        return res and res1 and res2

    def click_on_forgot_password_link(self):
        return self.click_on_element(self._FORGOT_PASSWORD_LINK_LOCATOR)

    def click_on_profile_dropdown(self):
        return self.click_on_element(self._PROFILE_DROPDOWN_LOCATOR)

    def click_on_sign_out_button(self):
        return self.click_on_element(self._SIGN_OUT_BUTTON_LOCATOR)

    def click_on_student_profile_dropdown(self):
        return self.click_on_element(self._STUDENT_PROFILE_DROPDOWN_LOCATOR)

    def click_on_student_sign_out_button(self):
        return self.click_on_element(self._STUDENT_SIGN_OUT_BUTTON_LOCATOR)

    def sign_out(self):
        time.sleep(5)
        res1 = self.click_on_profile_dropdown()
        res2 = self.click_on_sign_out_button()
        return res1 and res2

    def student_sign_out(self):
        res1 = self.click_on_student_profile_dropdown()
        res2 = self.click_on_student_sign_out_button()
        return res1 and res2

    def check_dashboard_url(self, check_url):
        print("Dashboard url is = ", check_url)
        return self.check_for_new_url(check_url)

from __future__ import print_function
import os
import time

from selenium.webdriver import ActionChains

import constants
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ManageStudentPage(BasePage):
    _NEW_STUDENT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#add_new_student")
    _STUDENT_FIRST_NAME_INPUT_LOCATOR = (By.ID, "input_fname")
    _STUDENT_LAST_NAME_INPUT_LOCATOR = (By.ID, "input_lname")
    _STUDENT_EMAIL_INPUT_LOCATOR = (By.ID, "input_email")
    _STUDENT_PHONE_NUMBER_LOCATOR = (By.CSS_SELECTOR, "div.iti #phone")
    _SAVE_BUTTON_LOCATOR = (By.ID, "save_button")
    _CANCEL_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button.btn-cancel")
    _ADVISOR_DROPDOWN_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        '[formcontrolname="advisor_id"] input',
    )
    _ADVISOR_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, '[formcontrolname="advisor_id"]')
    _SELECT_ADVISOR_DROPDOWN_LIST_LOCATOR = (By.CSS_SELECTOR, '[role="option"]')
    _STUDENT_IDENTIFIER_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        "#input_student_account_identifier",
    )
    _CONSENT_CHECK_BOX = (By.CSS_SELECTOR, "span.mat-checkbox-inner-container")
    _SEARCH_INPUT_LOCATOR = (By.CSS_SELECTOR, "#search_box")
    _SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "i.isc-search_by-solid")
    parent_link = (
        "/html/body/agt-root/agt-dashboard-index/div/div/div[2]/div[1]/ng-component/div[1]/div["
        "3]/isc-ptable/div[1]/table/tbody"
    )
    _STUDENT_NAME_LOCATOR = (
        By.XPATH,
        "//span[@class='w-full ltr:mr-1 rtl:ml-1 text-normal leading-normal font-medium']",
    )

    _STUDENT_EMAIL_LOCATOR = (
        By.XPATH,
        "//p[@class='break-all text-sm leading-sm text-gray w-full']",
    )

    _STUDENT_CONTACT_LOCATOR = (By.XPATH, "//p[@class='text-gray text-sm w-full']")
    _ADVISOR_LOCATOR = (
        By.CSS_SELECTOR,
        "[class='text-md leading-md text-gray-paragraph opacity-75 mobile-agency-name-div ng-star-inserted']",
    )
    _SEARCH_BAR_LOCATOR = (By.ID, "search_box")
    _IMPERSONATE_BUTTON_LOCATOR = (
        By.ID,
        "ptable_action_manage_students_options_actions_impersonate",
    )
    _CLOSE_IMPERSONATE_MODEL = (By.ID, "no_button")
    _OKAY_IMPERSONATE_MODEL_LOCATOR = (By.ID, "yes_button")
    _IMPERSONATE_STUDENT_FIRST_NAME_LOCATOR = (
        By.CSS_SELECTOR,
        "#impersonation_banner .impersonatinFirstName",
    )
    _IMPERSONATE_STUDENT_LAST_NAME_LOCATOR = (
        By.CSS_SELECTOR,
        "#impersonation_banner .impersonatinLastName",
    )
    _FIRST_NAME_ERROR_LOCATOR = (By.CSS_SELECTOR, "#fname_whitespace_error")
    _LAST_NAME_ERROR_LOCATOR = (By.CSS_SELECTOR, "#lname_whitespace_error")
    _EMAIL_ERROR_LOCATOR = (By.CSS_SELECTOR, "#email_required_error")
    _PHONE_NUMBER_ERROR_LOCATOR = (By.CSS_SELECTOR, "#phone_invalid_error")
    _IDENTIFIER_ERROR_LOCATOR = (By.CSS_SELECTOR, "#student_account_identifier_whitespace_error")
    _CHANGE_ACCESS_LEVEL_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(),'Change Access Level')]")
    _CHANGE_ACCESS_LEVEL_DROP_DOWN_LOCATOR = (By.CSS_SELECTOR, "#change_plan__account_type_select")
    _CHOOSE_ACCESS_LEVEL_LOCATOR = (By.CSS_SELECTOR, "#change_plan__account_type_select option:nth-child(2)")
    _VALIDATE_CHANGED_ACCESS_LEVEL_LOCATOR = (By.CSS_SELECTOR, "[class='plan-pills rounded-full tier-1']")
    _CHANGE_ACCESS_LEVEL_SAVE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#change_plan__save")
    _RETURN_TO_IMPERSONATION_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "#impersonation_banner span.underline.cursor-pointer.font-medium.text-gray-paragraph",
    )

    def check_student_dashboard_url(self):
        return self.check_for_new_url(os.environ.get("MANAGE_STUDENT_URL"))

    def click_on_new_student_btn(self):
        return self.click_on_element(self._NEW_STUDENT_BUTTON_LOCATOR)

    def add_student_fname(self, first_name):
        return self.enter_field_input(self._STUDENT_FIRST_NAME_INPUT_LOCATOR, first_name)

    def add_student_lname(self, last_name):
        return self.enter_field_input(self._STUDENT_LAST_NAME_INPUT_LOCATOR, last_name)

    def add_student_email(self, stud_email):
        return self.enter_field_input(self._STUDENT_EMAIL_INPUT_LOCATOR, stud_email)

    def add_student_phone_no_without_changing_ISD(self, stud_number):
        return self.enter_field_input(self._STUDENT_PHONE_NUMBER_LOCATOR, stud_number)

    def add_student_identifier(self, identifier):
        return self.enter_field_input(
            self._STUDENT_IDENTIFIER_INPUT_LOCATOR, identifier
        )

    def click_on_consent_checkbox(self):
        return self.click_on_element(self._CONSENT_CHECK_BOX)

    def click_on_save_button(self):
        return self.click_on_element(self._SAVE_BUTTON_LOCATOR)

    def add_advisor_dropdown_input(self):
        return self.click_on_element(self._SELECT_ADVISOR_DROPDOWN_LIST_LOCATOR)

    def click_on_select_advisor(self):
        return self.click_on_element(self._ADVISOR_DROPDOWN_LOCATOR)

    def create_student(self, first_name, last_name, email, stud_number, identifier):
        res1 = self.click_on_new_student_btn
        res2 = self.add_student_fname(first_name)
        res3 = self.add_student_lname(last_name)
        res4 = self.add_student_email(email)
        res5 = self.add_student_phone_no_without_changing_ISD(stud_number)
        res6 = self.click_on_select_advisor
        res10 = self.enter_field_input(
            self._ADVISOR_DROPDOWN_INPUT_LOCATOR, "ajamadar advisor"
        )
        res11 = self.add_advisor_dropdown_input
        time.sleep(2)
        res7 = self.add_student_identifier(identifier)
        res8 = self.click_on_consent_checkbox
        res9 = self.click_on_save_button
        return (
                res1
                and res2
                and res3
                and res4
                and res5
                and res6
                and res7
                and res8
                and res9
                and res10
                and res11
        )

    def create_student_without_advisor(self, first_name, last_name, email, number, identifier):
        time.sleep(3)
        res1 = self.click_on_new_student_btn()
        res2 = self.add_student_fname(first_name)
        res3 = self.add_student_lname(last_name)
        res4 = self.add_student_email(email)
        res5 = self.add_student_phone_no_without_changing_ISD(number)
        res7 = self.add_student_identifier(identifier)
        res8 = self.click_on_consent_checkbox()
        res9 = self.click_on_save_button()
        return res1 and res2 and res3 and res4 and res5 and res7 and res8 and res9

    def create_student_with_invalid_data(self, first_name, last_name, email, number, identifier):
        res1 = self.click_on_new_student_btn()
        res2 = self.add_student_fname(first_name)
        res3 = self.add_student_lname(last_name)
        res4 = self.add_student_email(email)
        res5 = self.add_student_phone_no_without_changing_ISD(number)
        res7 = self.add_student_identifier(identifier)
        res8 = self.click_on_consent_checkbox()
        return res1 and res2 and res3 and res4 and res5 and res7 and res8

    def search_for_student(self, email):
        time.sleep(3)
        res1 = self.enter_field_input(self._SEARCH_INPUT_LOCATOR, email)
        time.sleep(2)
        return res1

    def check_for_student_name(self, first_name, last_name):
        print("i" + first_name, last_name)
        a = self.get_text_of_elements(self._STUDENT_NAME_LOCATOR)
        print("ex" + self.convert_list_to_string(a))
        return self.convert_list_to_string(a) == first_name, last_name

    def check_for_student_email(self, email):
        print(email)
        a = self.get_text_of_elements(self._STUDENT_EMAIL_LOCATOR)
        print(self.convert_list_to_string(a))
        return self.convert_list_to_string(a) == email

    def check_for_student_number(self, student_number):
        print(student_number)
        a = self.get_text_of_elements(self._STUDENT_CONTACT_LOCATOR)
        print(self.convert_list_to_string(a))
        return self.convert_list_to_string(a) == "+91 " + student_number

    def check_for_advisor_name(self, advisor_name):
        print(advisor_name)
        a = self.get_text_of_elements(self._ADVISOR_LOCATOR)
        print(self.convert_list_to_string(a))
        return self.convert_list_to_string(a) == advisor_name

    def enter_in_search(self, email):
        res1 = self.click_on_element(self._SEARCH_BAR_LOCATOR)
        res2 = self.enter_field_input(self._SEARCH_BAR_LOCATOR, email)
        return res1 and res2

    def click_on_impersonate_button(self):
        return self.click_on_element(self._IMPERSONATE_BUTTON_LOCATOR)

    def close_impersonate_model(self):
        return self.click_on_element(self._CLOSE_IMPERSONATE_MODEL)

    def verify_student_name(self, student_name):
        b = self.get_text_of_elements(self._IMPERSONATE_STUDENT_LAST_NAME_LOCATOR)
        a = self.get_text_of_elements(self._IMPERSONATE_STUDENT_FIRST_NAME_LOCATOR)
        print(self.convert_list_to_string(a), self.convert_list_to_string(b))
        return (
            self.convert_list_to_string(a),
            self.convert_list_to_string(b) == student_name,
        )

    def check_all_error_messages(self):
        a = self.get_text_of_elements(self._FIRST_NAME_ERROR_LOCATOR)
        res1 = self.convert_list_to_string(a) == constants.USER_FORM_FIRST_NAME
        print(self.convert_list_to_string(a))
        b = self.get_text_of_elements(self._LAST_NAME_ERROR_LOCATOR)
        res2 = self.convert_list_to_string(b) == constants.USER_FORM_LAST_NAME
        print(self.convert_list_to_string(b))
        c = self.get_text_of_elements(self._EMAIL_ERROR_LOCATOR)
        res3 = self.convert_list_to_string(c) == constants.USER_FORM_EMAIL
        print(self.convert_list_to_string(c))
        d = self.get_text_of_elements(self._PHONE_NUMBER_ERROR_LOCATOR)
        res4 = self.convert_list_to_string(d) == constants.USER_FORM_PHONE_NUMBER
        print(self.convert_list_to_string(d))
        e = self.get_text_of_elements(self._IDENTIFIER_ERROR_LOCATOR)
        res5 = self.convert_list_to_string(e) == constants.USER_FORM_IDENTIFIER
        print(self.convert_list_to_string(e))
        return res1 and res2 and res3 and res4 and res5

    def click_on_action_button(self):
        time.sleep(5)
        hover_ele = self.selenium.find_element(By.CSS_SELECTOR, "div .has-action-button")
        action = ActionChains(self.selenium)
        action.move_to_element(hover_ele).perform()
        action.click(hover_ele)
        action_button = self.selenium.find_element(By.CSS_SELECTOR, "#ptable_actions >.mat-button-wrapper")
        action.move_to_element(action_button).perform()
        action_button.click()
        time.sleep(2)
        return True

    def click_on_change_access_level_button(self):
        return self.click_on_element(self._CHANGE_ACCESS_LEVEL_BUTTON_LOCATOR)

    def click_on_change_access_level_dropdown(self):
        return self.click_on_element(self._CHANGE_ACCESS_LEVEL_DROP_DOWN_LOCATOR)

    def choose_other_access_level(self):
        return self.click_on_element(self._CHOOSE_ACCESS_LEVEL_LOCATOR)

    def click_on_change_access_level_save_button(self):
        return self.click_on_element(self._CHANGE_ACCESS_LEVEL_SAVE_BUTTON_LOCATOR)

    def validate_access_level_text(self):
        time.sleep(3)
        a = self.get_text_of_elements(self._VALIDATE_CHANGED_ACCESS_LEVEL_LOCATOR)
        print(self.convert_list_to_string(a))
        res = self.convert_list_to_string(a) == constants.CHANGE_ACCESS_LEVEL_VIEW_ACCESS or constants.CHANGE_ACCESS_LEVEL_ESSENTIAL
        return res

    def ok_button_impersonate_model(self):
        res = self.click_on_element(self._OKAY_IMPERSONATE_MODEL_LOCATOR)
        time.sleep(5)
        return res

    def click_on_return_to_impersonate_button(self):
        return self.click_on_element(self._RETURN_TO_IMPERSONATION_BUTTON_LOCATOR)

from __future__ import print_function
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import constants


class ManageAdvisorPage(BasePage):
    _ADD_ADVISOR_BUTTON_LOCATOR = (By.ID, "add_new_advisor")
    _ADVISOR_FIRST_NAME_INPUT_LOCATOR = (By.CSS_SELECTOR, "#input_fname")
    _ADVISOR_LAST_NAME_INPUT_LOCATOR = (By.ID, "input_adminLname")
    _ADVISOR_EMAIL_INPUT_LOCATOR = (By.ID, "input_email")
    _ADVISOR_PHONE_NUMBER_INPUT_LOCATOR = (By.CSS_SELECTOR, "div.iti #phone")
    _DIVISION_DROPDOWN_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        '#select_agency_dropdown [role="combobox"] input',
    )
    _SELECT_DIVISION_DROPDOWN_LIST_LOCATOR = (
        By.CSS_SELECTOR,
        "[role='option']",
    )
    _SEARCH_INPUT_LOCATOR = (By.CSS_SELECTOR, "#search_box")
    _SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "i.isc-search_by-solid")
    _DIVISION_FILTER_LOCATOR = (
        By.CSS_SELECTOR,
        '.dropdown-wrapper .ng-select-searchable [role="combobox"] input',
    )
    _DIVISION_DROPDOWN_FILTER_LOCATOR = (By.CSS_SELECTOR, "")
    _CROSS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "span.modal-close")
    _SAVE_BUTTON_LOCATOR = (By.ID, "save_button")
    _CANCEL_BUTTON_LOCATOR = (By.ID, "cancel_button")
    _STATUS_FILTER_LOCATOR = (By.CSS_SELECTOR, "span.badge")
    parent_link = (
        "/html/body/agt-root/agt-dashboard-index/div[2]/div/div[3]/div/div["
        "1]/agt-dashboard-manage-advisors/div/div[3]/agt-ptable/table/tbody/tr[1]/td[1]/div/div["
        "2]/agt-dropdown/div/div"
    )
    _ACTION_BUTTON_HOVER_LOCATOR = (
        By.XPATH,
        "/html/body/agt-root/agt-dashboard-index/div/div/div[2]/div[1]"
        "/ng-component/div[1]/div[3]/isc-ptable/div[1]/table/tbody/tr",
    )
    _ACTION_BUTTON_LOCATOR = (By.XPATH, parent_link + "/div[1]/span[1]")
    _EDIT_BUTTON_LOCATOR = (By.ID, "ptable_action_labels_edit")
    _DISABLE_BUTTON_LOCATOR = (By.ID, "ptable_action_labels_disable")
    _ADVISOR_NAME_LOCATOR = (
        By.XPATH,
        "//div[@class='relative w-full flex items-center undefined has-action-button']//p[@class='name "
        "ng-star-inserted']",
    )

    _ADVISOR_EMAIL_LOCATOR = (By.XPATH, "//p[@class='subtitle ng-star-inserted']")
    _ADVISOR_CONTACT_LOCATOR = (
        By.XPATH,
        "//span[@class='whitespace-nowrap text-sm ng-star-inserted']",
    )
    _ADVISOR_DIVISION_LOCATOR = (
        By.CSS_SELECTOR,
        "advisor-ptable td:nth-child(3) span",
    )
    _NO_OF_STUDENTS_LOCATOR = ()
    _ADVISOR_FIRST_NAME_ERROR_MSG = (By.CSS_SELECTOR, "#fname_required_error")
    _ADVISOR_LAST_NAME_ERROR_MSG = (By.CSS_SELECTOR, "#lname_required_error")
    _ADVISOR_EMAIL_ERROR_MSG = (By.CSS_SELECTOR, "#email_required_error")
    _ADVISOR_PHONE_ERROR_MSG = (By.CSS_SELECTOR, "#phone_required_error")
    _DISABLE_CONFIRMATION_BUTTON_LOCATOR = (By.ID, "yes_button")
    _DISABLE_USER_ALERT_MSG = (By.CSS_SELECTOR, "#alert_wrapper p")
    _ENABLE_BUTTON_LOCATOR = (By.ID, "ptable_action_labels_enable")
    _STATUS_FILTER_DROPDOWN_LOCATOR = (
        By.ID,
        "manage_advisors__filter_status",
    )
    _FILTER_DROPDOWN_LIST_LOCATOR = (By.CSS_SELECTOR, '[role="option"]')
    _STATUS_FILTER_LIST_LOCATOR = (By.CSS_SELECTOR, "span.badge")
    _CLEAR_ALL_LINK_LOCATOR = (By.ID, "clear_button")
    _COMMISSION_CHECKBOX = (By.CSS_SELECTOR, "span.mat-checkbox-inner-container")
    _STUDENT_DISABLE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#ptable_action_manage_students_options_actions_disable span")
    _STUDENT_STATUS_FILTER_LOCATOR = (By.CSS_SELECTOR, "div.text-sm")
    _STUDENT_ENABLE_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(),'Enable')]")

    division_name = ["mumbai division", "testdivision", "Test ISC"]

    def check_advisor_dashboard_url(self):
        return self.check_for_new_url(os.environ.get("MANAGE_ADVISOR_URL"))

    def click_on_add_advisor_button(self):
        return self.click_on_element(self._ADD_ADVISOR_BUTTON_LOCATOR)

    def click_on_close_advisor_button(self):
        return self.click_on_element(self._CROSS_BUTTON_LOCATOR)

    def add_advisor_fname(self, advisor_first_name):
        return self.enter_field_input(
            self._ADVISOR_FIRST_NAME_INPUT_LOCATOR, advisor_first_name
        )

    def add_advisor_lname(self, advisor_last_name):
        return self.enter_field_input(
            self._ADVISOR_LAST_NAME_INPUT_LOCATOR, advisor_last_name
        )

    def add_advisor_email(self, email):
        return self.enter_field_input(self._ADVISOR_EMAIL_INPUT_LOCATOR, email)

    def add_advisor_phone_no_without_changing_ISD(self, number):
        return self.enter_field_input(self._ADVISOR_PHONE_NUMBER_INPUT_LOCATOR, number)

    def click_on_select_division(self):
        return self.click_on_element(self._DIVISION_DROPDOWN_INPUT_LOCATOR)

    def add_division_dropdown_input(self):
        return self.click_on_element(self._SELECT_DIVISION_DROPDOWN_LIST_LOCATOR)

    def click_on_save_button(self):
        time.sleep(2)
        return self.click_on_element(self._SAVE_BUTTON_LOCATOR)

    def create_advisor(self, advisor_first_name, advisor_last_name, email, number):
        res1 = self.click_on_add_advisor_button()
        res2 = self.add_advisor_fname(advisor_first_name)
        res3 = self.add_advisor_lname(advisor_last_name)
        res4 = self.add_advisor_email(email)
        res5 = self.add_advisor_phone_no_without_changing_ISD(number)
        res6 = self.click_on_select_division
        res10 = self.enter_field_input(
            self._DIVISION_DROPDOWN_INPUT_LOCATOR, self.division_name[0]
        )
        res7 = self.add_division_dropdown_input
        res8 = self.click_on_save_button
        return (
                res1
                and res2
                and res3
                and res4
                and res5
                and res6
                and res7
                and res8
                and res10
        )

    def create_advisor_without_division(
            self, advisor_first_name, advisor_last_name, email, number
    ):
        res1 = self.click_on_add_advisor_button
        res2 = self.add_advisor_fname(advisor_first_name)
        res3 = self.add_advisor_lname(advisor_last_name)
        res4 = self.add_advisor_email(email)
        res5 = self.add_advisor_phone_no_without_changing_ISD(number)
        res8 = self.click_on_save_button
        return res1 and res2 and res3 and res4 and res5 and res8

    def check_for_advisor_name(self, advisor_first_name, advisor_last_name):
        print("i" + advisor_first_name, advisor_last_name)
        a = self.get_text_of_elements(self._ADVISOR_NAME_LOCATOR)
        print("ex" + self.convert_list_to_string(a))
        print(self.convert_list_to_string(a) == advisor_first_name, advisor_last_name)
        return self.convert_list_to_string(a) == advisor_first_name, " " + advisor_last_name

    def check_for_advisor_email(self, email):
        print(email)
        a = self.get_text_of_elements(self._ADVISOR_EMAIL_LOCATOR)
        print(self.convert_list_to_string(a))
        print(self.convert_list_to_string(a) == email)
        return self.convert_list_to_string(a) == email

    def check_for_advisor_number(self, new_number):
        time.sleep(3)
        print(new_number)
        a = self.get_text_of_elements(self._ADVISOR_CONTACT_LOCATOR)
        print(self.convert_list_to_string(a))
        return self.convert_list_to_string(a) == "+91 " + new_number

    def check_for_division_name(self, ):
        a = self.get_text_of_elements(self._ADVISOR_DIVISION_LOCATOR)
        output_text = self.convert_list_to_string(a[0])
        print(output_text)
        return output_text == self.division_name[1] or self.division_name[2]

    def check_for_no_of_students(self, stud_number):
        return self.get_text_of_elements(self._NO_OF_STUDENTS_LOCATOR) == stud_number

    def click_on_edit_butn(self):
        return self.click_on_element(self._EDIT_BUTTON_LOCATOR)

    def edit_advisor_details(self, advisor_first_name, advisor_last_name, number, division):
        res1 = self.enter_field_input(
            self._ADVISOR_FIRST_NAME_INPUT_LOCATOR, advisor_first_name
        )
        res2 = self.enter_field_input(
            self._ADVISOR_LAST_NAME_INPUT_LOCATOR, advisor_last_name
        )
        res3 = self.enter_field_input(self._ADVISOR_PHONE_NUMBER_INPUT_LOCATOR, number)
        res4 = self.enter_field_input(self._DIVISION_DROPDOWN_INPUT_LOCATOR, division)
        res5 = self.add_division_dropdown_input
        res6 = self.click_on_save_button()
        return res1 and res2 and res3 and res4 and res5 and res6

    def edit_advisor_details_without_division(
            self, advisor_first_name, advisor_last_name, number
    ):
        res1 = self.enter_field_input(
            self._ADVISOR_FIRST_NAME_INPUT_LOCATOR, advisor_first_name
        )
        res2 = self.enter_field_input(
            self._ADVISOR_LAST_NAME_INPUT_LOCATOR, advisor_last_name
        )
        res3 = self.enter_field_input(self._ADVISOR_PHONE_NUMBER_INPUT_LOCATOR, number)
        res4 = self.click_on_save_button
        return res1 and res2 and res3 and res4

    def check_advisor_fname_error_msg(self):
        a = self.get_text_of_elements(self._ADVISOR_FIRST_NAME_ERROR_MSG)
        print(self.convert_list_to_string(a))
        res1 = self.convert_list_to_string(a) == constants.FIRST_NAME_REQUIRED
        return res1

    def check_advisor_lname_error_msg(self):
        a = self.get_text_of_elements(self._ADVISOR_LAST_NAME_ERROR_MSG)
        print(self.convert_list_to_string(a))
        res1 = self.convert_list_to_string(a) == constants.LAST_NAME_REQUIRED
        return res1

    def check_advisor_phone_number_error_msg(self):
        a = self.get_text_of_elements(self._ADVISOR_PHONE_ERROR_MSG)
        print(self.convert_list_to_string(a))
        res1 = self.convert_list_to_string(a) == constants.PHONE_NUMBER_REQUIRED
        return res1

    def check_advisor_email_error_msg(self):
        self.scroll_into_view(self._ADVISOR_EMAIL_ERROR_MSG)
        a = self.get_text_of_elements(self._ADVISOR_EMAIL_ERROR_MSG)
        print(self.convert_list_to_string(a))
        res1 = self.convert_list_to_string(a) == constants.EMAIL_REQUIRED
        return res1

    def search_for_advisor(self, email):
        time.sleep(3)
        return self.enter_field_input(self._SEARCH_INPUT_LOCATOR, email)

    def search_for_commission_advisor(self, email):
        res1 = self.enter_field_input(self._SEARCH_INPUT_LOCATOR, email)
        return res1

    def search_for_commission_checkbox(self):
        return self.click_on_element(self._COMMISSION_CHECKBOX)

    def click_on_action_butn(self):
        time.sleep(5)
        hover_ele = self.selenium.find_element_by_css_selector("div .has-action-button")
        action = ActionChains(self.selenium)
        action.move_to_element(hover_ele).perform()
        action.click(hover_ele)
        action_button = self.selenium.find_element_by_css_selector(
            "#ptable_actions >.mat-button-wrapper"
        )
        action.move_to_element(action_button).perform()
        action_button.click()
        time.sleep(2)
        return True

    def disable_advisor_details(self):
        time.sleep(2)
        res1 = self.click_on_element(self._DISABLE_BUTTON_LOCATOR)
        res2 = self.click_on_element(self._DISABLE_CONFIRMATION_BUTTON_LOCATOR)
        return res1 and res2

    def check_for_status_name(self, status):
        time.sleep(4)
        print(status)
        a = self.get_text_of_elements(self._STATUS_FILTER_LOCATOR)
        print(self.convert_list_to_string(a))
        return self.convert_list_to_string(a) == status

    def check_disable_user_login_text(self, alert_msg):
        time.sleep(2)
        print(alert_msg)
        a = self.get_text_of_elements(self._DISABLE_USER_ALERT_MSG)
        print(self.convert_list_to_string(a))
        return self.convert_list_to_string(a) == alert_msg

    def enable_advisor(self):
        time.sleep(2)
        return self.click_on_element(self._ENABLE_BUTTON_LOCATOR)

    def click_on_status_filter(self):
        return self.click_on_non_click_able(self._STATUS_FILTER_DROPDOWN_LOCATOR)

    def check_status_filter_is_working(self, a, v):
        res1 = self.click_on_status_filter
        if (len(a) == 1 and v.upper() == a.pop()) or len(a) == 0:
            print(a)
            self.click_on_element(self._CLEAR_ALL_LINK_LOCATOR)
            return True
        else:
            return Exception

    def click_on_filter_list_option(self, k):
        return self.click_on_element(self._FILTER_DROPDOWN_LIST_LOCATOR, k)

    def check_status_filter_output(self, locator):
        print(self.get_text_of_elements(locator))
        text_output_result = set(self.get_text_of_elements(locator))
        print(text_output_result)
        return text_output_result

    def check_for_filters(self, status):
        time.sleep(3)
        result = True
        for k, v in status.items():
            res1 = self.click_on_status_filter
            self.click_on_filter_list_option(k)
            text_output = self.check_status_filter_output(
                self._STATUS_FILTER_LIST_LOCATOR
            )  # output text
            if self.check_status_filter_is_working(text_output, v):
                print(text_output)
                result = True
            else:
                result = False
        return result

    def click_on_division_filter(self):
        return self.click_on_element(self._DIVISION_FILTER_LOCATOR)

    def select_division_from_filter_list(self, division):
        res1 = self.enter_field_input(self._DIVISION_FILTER_LOCATOR, division)
        res2 = self.click_on_element(self._FILTER_DROPDOWN_LIST_LOCATOR)
        return res1 and res2

    def apply_and_verify_division_filter(self, division_name):
        res1 = self.click_on_division_filter()
        res2 = self.select_division_from_filter_list(division_name)
        res3 = self.check_for_division_name()
        return res1 and res2 and res3

    def disable_student_details(self):
        time.sleep(2)
        res1 = self.click_on_element(self._STUDENT_DISABLE_BUTTON_LOCATOR)
        res2 = self.click_on_element(self._DISABLE_CONFIRMATION_BUTTON_LOCATOR)
        return res1 and res2

    def check_for_student_status_name(self, status):
        time.sleep(4)
        print(status)
        a = self.get_text_of_elements(self._STUDENT_STATUS_FILTER_LOCATOR)
        print(self.convert_list_to_string(a))
        return self.convert_list_to_string(a) == status

    def enable_student(self):
        return self.click_on_element(self._STUDENT_ENABLE_BUTTON_LOCATOR)

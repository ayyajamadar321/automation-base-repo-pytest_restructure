from __future__ import print_function
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import constants
from pages.base_page import BasePage


class ManageDivisionPage(BasePage):

    _MANAGE_DIVISION_TAB_LOCATOR = (
        By.CSS_SELECTOR,
        '[ng-reflect-router-link="/dashboard/manage-agency"]',
    )
    _MANAGE_ADVISOR_TAB_LOCATOR = (
        By.CSS_SELECTOR,
        'a[href="/dashboard/manage-advisors"]',
    )
    _ADD_DIVISION_BUTTON_LOCATOR = (By.ID, "add_new_agency")
    _DIVISION_NAME_INPUT_LOCATOR = (By.ID, "input_agency_name")
    _DIVISION_PHONE_NUMBER_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        "#add_division__input_phone #phone",
    )
    _ADMIN_FIRST_NAME_INPUT_LOCATOR = (By.ID, "input_admin_fname")
    _ADMIN_LAST_NAME_INPUT_LOCATOR = (By.ID, "input_adminLname")
    _ADMIN_EMAIL_INPUT_LOCATOR = (By.ID, "input_admin_email")
    _ADMIN_PHONE_NUMBER_LOCATOR = (
        By.CSS_SELECTOR,
        "#add_agency__admin_phone_input #phone",
    )
    _SAVE_BUTTON_LOCATOR = (By.ID, "save_button")
    _CANCEL_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button.btn-cancel")
    _CROSS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "span.modal-close")
    _STATUS_FILTER_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, "[role='combobox']")
    _STATUS_FILTER_DROPDOWN_LIST_LOCATOR = (By.CSS_SELECTOR, '[role="option"]')
    _DIVISION_NAME_LOCATOR = (
        By.XPATH,
        "//div[@class='relative w-full flex items-center undefined has-action-button']//p[@class='name ng-star-inserted']",
    )
    _DIVISION_PHONE_NUMBER_LOCATOR = (
        By.XPATH,
        "//div[@class='relative w-full flex items-center undefined has-action-button']//p[@class='subtitle ng-star-inserted']",
    )
    _ADMIN_NAME_LOCATOR = (
        By.XPATH,
        "//div[@class='relative w-full flex items-center undefined']//p[@class='name ng-star-inserted']",
    )
    _ADMIN_EMAIL_LOCATOR = (
        By.XPATH,
        "//div[@class='relative w-full flex items-center undefined']//p[@class='subtitle ng-star-inserted']",
    )
    _NO_OF_ADVISOR_LOCATOR = (
        By.XPATH,
        "/html/body/agt-root/agt-dashboard-index/div/div[2]"
        "/div[2]/div/div[1]/agt-manage-agency/div/div[3]"
        "/agt-ptable/table/tbody/tr[1]/td[3]",
    )
    _APPLICATION_FILTER_LOCATOR = ()
    _STATUS_FILTER_LOCATOR = (By.CSS_SELECTOR, ".badge.ng-star-inserted")
    _STATUS_FILTER_LIST_LOCATOR = (By.CSS_SELECTOR, "span.badge")
    _DIVISION_NAME_ERROR_MSG = (By.CSS_SELECTOR, "#agency_name_required_error")
    _DIVISION_PHONE_ERROR_MSG = (By.CSS_SELECTOR, "#agency_phone_required_error")
    _ADMIN_FIRST_NAME_ERROR_MSG = (By.CSS_SELECTOR, "#admin_fname_required_error")
    _ADMIN_LAST_NAME_ERROR_MSG = (By.CSS_SELECTOR, "#admin_lname_required_error")
    _ADMIN_EMAIL_ERROR_MSG = (By.CSS_SELECTOR, "#admin_email_required_error")
    _ADMIN_PHONE_ERROR_MSG = (By.CSS_SELECTOR, "#admin_phone_required_error")
    _ACTION_BUTTON_HOVER = (
        By.XPATH,
        "/html/body/agt-root/agt-dashboard-index/div/div/div[2]/div[1]"
        "/isc-manage-agency/div[1]/div[3]/isc-ptable/div[1]/table/tbody/tr[1]",
    )
    _ACTION_BUTTON_LOCATOR = (By.ID, "ptable_actions")
    _EDIT_BUTTON_LOCATOR = (By.ID, "ptable_action_edit")
    _DISABLE_BUTTON_LOCATOR = (By.ID, "ptable_action_disable")
    _ENABLE_BUTTON_LOCATOR = (By.ID, "ptable_action_enable")
    _DISABLE_CONFIRMATION_BUTTON_LOCATOR = (By.ID, "yes_button")
    _EDIT_DIVISION_NAME_INPUT_LOCATOR = (By.XPATH, "//input[@id='input_fname']")
    _EDIT_DIVISION_NUMBER_INPUT_LOCATOR = (By.XPATH, "//input[@id='phone']")
    _SOUNDS_GOOD_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        'a[aria-label="dismiss cookie message"]',
    )
    _SEARCH_INPUT_LOCATOR = (By.CSS_SELECTOR, "#search_box")
    _SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "i.isc-search_by-solid")
    _STUDENT_DASHBOARD_LOCATOR = (
        By.CSS_SELECTOR,
        '[href="/dashboard/manage-students"]',
    )
    _DISABLE_USER_ALERT_MSG = (By.CSS_SELECTOR, "#alert_wrapper p")
    _CLEAR_ALL_LINK_LOCATOR = (By.ID, "clear_button")
    _FILTERS_LINK_LOCATOR = (By.ID, "toggle_more_filters")

    def click_on_filter_link(self):
        return self.click_on_element(self._FILTERS_LINK_LOCATOR)

    def click_on_add_division_button(self):
        return self.click_on_element(self._ADD_DIVISION_BUTTON_LOCATOR)

    def click_on_close_division_button(self):
        return self.click_on_element(self._CROSS_BUTTON_LOCATOR)

    def add_division_name(self, division_name):
        return self.enter_field_input(self._DIVISION_NAME_INPUT_LOCATOR, division_name)

    def add_division_phone_no_without_changing_ISD(self, division_number):
        return self.enter_field_input(
            self._DIVISION_PHONE_NUMBER_INPUT_LOCATOR, division_number
        )

    def add_admin_fname(self, fname):
        return self.enter_field_input(self._ADMIN_FIRST_NAME_INPUT_LOCATOR, fname)

    def add_admin_lname(self, lname):
        return self.enter_field_input(self._ADMIN_LAST_NAME_INPUT_LOCATOR, lname)

    def add_admin_email(self, email):
        return self.enter_field_input(self._ADMIN_EMAIL_INPUT_LOCATOR, email)

    def add_admin_phone_no_without_changing_isd(self, number):
        self.scroll_into_view(self._ADMIN_PHONE_NUMBER_LOCATOR)
        return self.enter_field_input(self._ADMIN_PHONE_NUMBER_LOCATOR, number)

    def click_on_save_button(self):
        time.sleep(2)
        return self.click_on_element(self._SAVE_BUTTON_LOCATOR)

    def create_division(self, division_name, division_number, fname, lname, email):
        time.sleep(2)
        res1 = self.click_on_add_division_button()
        res2 = self.add_division_name(division_name)
        res3 = self.add_division_phone_no_without_changing_ISD(division_number)
        res4 = self.add_admin_fname(fname)
        res5 = self.add_admin_lname(lname)
        res6 = self.add_admin_email(email)
        res7 = self.add_admin_phone_no_without_changing_isd(division_number)
        return res1 and res2 and res3 and res4 and res5 and res6 and res7

    def check_for_division_name(self, division_name):
        print(division_name)
        text = self.get_text_of_elements(self._DIVISION_NAME_LOCATOR)
        print(self.convert_list_to_string(text))
        return self.convert_list_to_string(text) == division_name

    def check_for_division_number(self, division_number):
        print(division_number)
        time.sleep(3)
        text = self.get_text_of_elements(self._DIVISION_PHONE_NUMBER_LOCATOR)
        print(self.convert_list_to_string(text))
        # return self.convert_list_to_string(a) == "+1 " + division_number
        return self.convert_list_to_string(text) == "+91 " + division_number

    def check_for_admin_name(self, fname, lname):
        print(fname, lname)
        text = self.get_text_of_elements(self._ADMIN_NAME_LOCATOR)
        print(self.convert_list_to_string(text))
        return self.convert_list_to_string(text) == fname, " " + lname

    def check_for_admin_email(self, email):
        print(email)
        text = self.get_text_of_elements(self._ADMIN_EMAIL_LOCATOR)
        print(self.convert_list_to_string(text))
        return self.convert_list_to_string(text) == email

    def check_for_no_of_advisors(self, adv_number):
        print(adv_number)
        text = self.get_text_of_elements(self._NO_OF_ADVISOR_LOCATOR)
        print(self.convert_list_to_string(text))
        return self.convert_list_to_string(text) == adv_number

    def enter_value_in_search(self, search_input):
        return self.enter_field_input(self._SEARCH_INPUT_LOCATOR, search_input)

    def click_on_search_butn(self):
        return self.click_on_element(self._SEARCH_BUTTON_LOCATOR)

    def check_search_is_working_for_division_name(self, search_input):
        res1 = self.enter_value_in_search(search_input)
        res2 = self.click_on_search_butn()
        res3 = self.check_for_division_name(search_input)
        return res1 and res2 and res3

    def check_admin_fname_error_msg(self):
        text = self.get_text_of_elements(self._ADMIN_FIRST_NAME_ERROR_MSG)
        print(self.convert_list_to_string(text))
        res1 = self.convert_list_to_string(text) == constants.FIRST_NAME_REQUIRED
        return res1

    def check_admin_lname_error_msg(self):
        text = self.get_text_of_elements(self._ADMIN_LAST_NAME_ERROR_MSG)
        print(self.convert_list_to_string(text))
        res1 = self.convert_list_to_string(text) == constants.LAST_NAME_REQUIRED
        return res1

    def check_division_phone_number_error_msg(self):
        text = self.get_text_of_elements(self._DIVISION_PHONE_ERROR_MSG)
        print(self.convert_list_to_string(text))
        res1 = self.convert_list_to_string(text) == constants.PHONE_NUMBER_REQUIRED
        return res1

    def check_admin_email_error_msg(self):
        self.scroll_into_view(self._ADMIN_EMAIL_ERROR_MSG)
        text = self.get_text_of_elements(self._ADMIN_EMAIL_ERROR_MSG)
        print(self.convert_list_to_string(text))
        res1 = self.convert_list_to_string(text) == constants.EMAIL_REQUIRED
        return res1

    def check_admin_number_error_msg(self):
        # self.scroll_into_view(self._ADMIN_PHONE_ERROR_MSG)
        # time.sleep(3)
        text = self.get_text_of_elements(self._ADMIN_PHONE_ERROR_MSG)
        print(self.convert_list_to_string(text))
        res1 = self.convert_list_to_string(text) == constants.PHONE_NUMBER_REQUIRED
        return res1

    def check_admin_incorrect_number_error_msg(self):
        self.scroll_into_view(self._ADMIN_PHONE_ERROR_MSG)
        text = self.get_text_of_elements(self._ADMIN_PHONE_ERROR_MSG)
        print(self.convert_list_to_string(text))
        res1 = self.convert_list_to_string(text) == constants.PHONE_NUMBER_VALIDATION
        return res1

    def check_division_incorrect_phone_number_error_msg(self):
        self.scroll_into_view(self._DIVISION_PHONE_ERROR_MSG)
        text = self.get_text_of_elements(self._DIVISION_PHONE_ERROR_MSG)
        print(self.convert_list_to_string(text))
        res1 = self.convert_list_to_string(text) == constants.PHONE_NUMBER_VALIDATION
        return res1

    def check_admin_incorrect_email_error_msg(self):
        self.scroll_into_view(self._ADMIN_EMAIL_ERROR_MSG)
        text = self.get_text_of_elements(self._ADMIN_EMAIL_ERROR_MSG)
        print(self.convert_list_to_string(text))
        res1 = self.convert_list_to_string(text) == constants.EMAIL_REQUIRED
        return res1

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

    def click_on_edit_butn(self):
        time.sleep(3)
        return self.click_on_element(self._EDIT_BUTTON_LOCATOR)

    def edit_division_details(self, division_name, division_number):
        res1 = self.enter_field_input(
            self._EDIT_DIVISION_NAME_INPUT_LOCATOR, division_name
        )
        res2 = self.enter_field_input(
            self._EDIT_DIVISION_NUMBER_INPUT_LOCATOR, division_number
        )
        res3 = self.click_on_save_button()
        return res1 and res2 and res3

    def disable_division_details(self):
        time.sleep(2)
        res1 = self.click_on_element(self._DISABLE_BUTTON_LOCATOR)
        res2 = self.click_on_element(self._DISABLE_CONFIRMATION_BUTTON_LOCATOR)
        return res1 and res2

    def enable_division(self):
        return self.click_on_element(self._ENABLE_BUTTON_LOCATOR)

    def go_to_manage_advisor_page(self):
        return self.click_on_element(self._MANAGE_ADVISOR_TAB_LOCATOR)

    def enter_search_input(self, division_name):
        res1 = self.enter_field_input(self._SEARCH_INPUT_LOCATOR, division_name)
        res2 = self.click_on_element(self._SEARCH_BUTTON_LOCATOR)
        return res1 and res2

    def check_for_searched_division(self, division_name):
        print(division_name)
        text = self.get_text_of_elements(self._DIVISION_NAME_LOCATOR)
        print(self.convert_list_to_string(text))
        return self.convert_list_to_string(text) == division_name

    def search_by_email(self, email):
        time.sleep(3)
        self.click_on_element(self._SEARCH_INPUT_LOCATOR)
        res1 = self.enter_field_input(self._SEARCH_INPUT_LOCATOR, email)
        res2 = self.click_on_element(self._SEARCH_BUTTON_LOCATOR)
        return res2 and res1

    def go_to_student_dashboard(self):
        return self.click_on_element(self._STUDENT_DASHBOARD_LOCATOR)

    def check_for_status_name(self, status):
        time.sleep(4)
        print(status)
        text = self.get_text_of_elements(self._STATUS_FILTER_LOCATOR)
        print(self.convert_list_to_string(text))
        return self.convert_list_to_string(text) == status

    def check_disable_user_login_text(self, alert_msg):
        time.sleep(2)
        print(alert_msg)
        text = self.get_text_of_elements(self._DISABLE_USER_ALERT_MSG)
        print(self.convert_list_to_string(text))
        return self.convert_list_to_string(text) == alert_msg

    def click_on_status_filter(self):
        return self.click_on_non_click_able(self._STATUS_FILTER_DROPDOWN_LOCATOR)

    def check_status_filter_is_working(self, a, v):
        res1 = self.click_on_status_filter
        if (len(a) == 1 and v.upper() == a.pop()) or len(a) == 0:
            print(a)
            self.click_on_element(self._CLEAR_ALL_LINK_LOCATOR)
            return True and res1
        else:
            return Exception

    def click_on_filter_list_option(self, k):
        return self.click_on_element(self._STATUS_FILTER_DROPDOWN_LIST_LOCATOR, k)

    def check_status_filter_output(self, locator=None):
        print(self.get_text_of_elements(locator))
        text_output = set(self.get_text_of_elements(locator))
        return text_output

    def check_for_filters(self, status):
        result = True
        for k, v in status.items():
            res = self.click_on_filter_link
            res1 = self.click_on_status_filter
            self.click_on_filter_list_option(k)
            text_output = self.check_status_filter_output(
                self._STATUS_FILTER_LIST_LOCATOR
            )
            if self.check_status_filter_is_working(text_output, v):
                print(text_output)
                result = True and res and res1
            else:
                result = False
        return result

import os
import time
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import constants
from pages.base_page import BasePage


class StudentApplicationPage(BasePage):
    _NEW_URL_SIGN_OUT = (By.XPATH, "//*[contains(text(),'Sign Out')]")
    _DEGREE_LOCATOR = (By.CSS_SELECTOR,
                       "div.hidden.md\:block > div:nth-child(1) div:nth-child(3) > button")
    _DISCIPLINE_LOCATOR = (By.XPATH, "//button[contains(text(),' Computer Science')]")
    _YEAR_LOCATOR = (By.XPATH, "//button[contains(text(),' 2023')]")
    _SEASON_LOCATOR = (By.XPATH, "//button[contains(text(),' Fall')]")
    _DONE_LOCATOR = (By.XPATH, "//span[contains(text(),'Done')]")
    _STUDENT_SIDE_APPLICATION_STATUS = (
        By.CSS_SELECTOR,
        "section.student_application_status_details  h3",
    )

    _DASHBOARD_LOCATOR = (
        By.XPATH,
        "//div[@class='navbar-inner-wrapper-for-scroll']/a[contains(text(),'Dashboard')]",
    )

    _CHANGE_STATUS_LOCATOR = (By.XPATH, "//span[contains(text(),'Change Status')]")
    _FORM_BUILDER_RADIO_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        ".application_additional_detail_checkbox .mat-checkbox-inner-container",
    )
    _UPLOAD_DOCUMENT = (By.CSS_SELECTOR, "applications-document-list-trigger > span")
    _IMPERSONATION_YES_BUTTON_LOCATOR = (By.ID, "yes_button")
    _DOCUMENT_TYPE_LOCATOR = (By.CSS_SELECTOR, "div.ng-input input[type=text]")
    _SCHOOL_TRANSCRIPT_DOCUMENT_LOCATOR = (
        By.CSS_SELECTOR,
        "[role='option']",
    )
    _UNIVERSITY_TRANSCRIPT_DOCUMENT_LOCATOR = (
        By.CSS_SELECTOR,
        "[role='option']",
    )
    _SELECT_DOCUMENT_LOCATOR = (
        By.CSS_SELECTOR,
        "[class='isc-upload-solid-1 upload-icon rtl:mr-0 rtl:ml-1']",
    )
    _CLOSE_DOCUMENT_WINDOW = (By.CSS_SELECTOR, "[class = 'isc-times-solid font-bold']")
    _SEND_REVIEW_LOCATOR = (
        By.CSS_SELECTOR,
        "section.student_application_status_details span.mat-button-wrapper",
    )
    _UPLOAD_DOCUMENT_RADIO_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        ".application_document_list_checkbox .mat-checkbox-inner-container-no-side-margin",
    )
    _SOP_ESSAY_RADIO_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        ".application_dwm_list_checkbox .mat-checkbox-inner-container",
    )
    _PAYMENT_RADIO_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        ".applications_fees_modal__item  .mat-checkbox-inner-container",
    )
    _MANDATORY_DOCUMENT_PASSPORT = (
        By.CSS_SELECTOR,
        "stdnt-document-table  tr:nth-child(1) td:nth-child(1)",
    )
    _MANDATORY_DOCUMENT_SCHOOL = (
        By.CSS_SELECTOR,
        "stdnt-document-table  tr:nth-child(3) td:nth-child(1)",
    )
    _UNIVERSITY_ACCEPTED_YES_BUTTON = (
        By.CSS_SELECTOR,
        "section.student_application_status_details button.mat-focus-indicator.application_status_accepted_accept_button span.mat-button-wrapper",
    )

    _UNIVERSITY_ACCEPTED_NO_BUTTON = (
        By.CSS_SELECTOR,
        "section.student_application_status_details button.mat-focus-indicator.application_status_accepted_reject_button span.mat-button-wrapper",
    )
    _UNIVERSITY_REJECTED_REASON = (By.CSS_SELECTOR, "div textarea")
    _SAVE_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "[class='mat-focus-indicator px-4 mat-flat-button mat-button-base mat-primary'] [class='mat-button-wrapper']",
    )
    _APPLY_BUTTON_LIST = (
        By.CSS_SELECTOR,
        ".desktop .apply__button .mat-button-wrapper",
    )
    _FORWARD_ARROW_BUTTON = (By.CSS_SELECTOR, ".paginator .isc-angle-right-solid")
    _ADD_TO_FAVOURITES = (
        By.CSS_SELECTOR,
        "isc-school-item:nth-child(1) isc-course-item:nth-child(1) div.action.desktop.showFavorite isc-shortlist-button span.mat-button-wrapper span",
    )
    _APPLY = (
        By.CSS_SELECTOR,
        "isc-school-item:nth-child(1) isc-course-item:nth-child(1) div.action.desktop.showFavorite > isc-apply-button > button > span.mat-button-wrapper",
    )
    _FINAL_APPLY = (By.CSS_SELECTOR, "#save_button > span.mat-button-wrapper")
    _PASSPORT_DOCUMENT_LOCATOR = (By.XPATH, "//div[contains(text(),'Passport')]")
    _STUD_EXPLORE_SCHOOL_TAB_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="navbar-inner-wrapper-for-scroll"] a:nth-child(3)',
    )
    _SELECT_YEAR = (By.XPATH, "//*[contains(text(),'2023')]")
    _SELECT_SEASON = (By.CSS_SELECTOR, "[for='application_cycle_season-0']")
    _FORM_BUILDER_RADIO_BUTTON_SELECTED_LOCATOR = (
        By.CSS_SELECTOR, "applications-additional-details-trigger [aria-checked='true']")
    _UPLOAD_DOCUMENT_RADIO_BUTTON_SELECTED_LOCATOR = (
        By.CSS_SELECTOR, "applications-document-list-trigger [aria-checked='true']")
    _SOP_AND_ESSAY_RADIO_BUTTON_SELECTED_LOCATOR = (
        By.CSS_SELECTOR, "application-dwm-list-trigger [aria-checked='true']")
    _PAYMENT_RADIO_BUTTON_SELECTED_LOCATOR = (By.CSS_SELECTOR, "applications-fees-trigger [aria-checked='true']")
    _UPLOAD_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[translate='buttons.upload']")
    _RETURN_TO_IMPERSONATION_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "#impersonation_banner span.underline.cursor-pointer.font-medium.text-gray-paragraph",
    )
    _STUDENT_APPLICATION_FORM = (
        By.XPATH,
        "//*[@id='sidebar']//a[2]",
    )
    _SEARCH_INPUT_LOCATOR = (By.CSS_SELECTOR, "#search_box")
    _ADVISOR_SIDE_APPLICATION_STATUS = (By.CSS_SELECTOR, "header h3")
    _APPLICATION_TAB_LOCATOR = (By.CSS_SELECTOR, '[href="/dashboard/manage-applications"]')
    _REVIEW_PASSED_LOCATOR = (By.XPATH, "//span[contains(text(),'Review Passed')]")
    _ON_HOLD_LOCATOR = (By.XPATH, "//span[contains(text(),'On Hold')]")
    _UNDER_REVIEW_STATUS_LOCATOR = (By.XPATH, "//span[contains(text(),'Under Review')]")
    _AWAITING_RESULT_LOCATOR = (By.XPATH, "//span[contains(text(),'Awaiting Results')]")
    _UNIVERSITY_ACCEPTED_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'University Accepted')]",
    )
    _CANCELLED_STATUS_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'Cancelled')]",
    )
    _FINANCIAL_DOCUMENTATION_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'Financial Documentation')]",
    )
    _CONDITIONAL_ACCEPTED_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'Conditional Acceptance')]",
    )
    _ADDITIONAL_SCREENING_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'Additional Screening')]",
    )
    _REASON_INPUT_TEXT_LOCATOR = (
        By.CSS_SELECTOR,
        "[formcontrolname='advisor_message']",
    )
    _CLICK_ON_TICKET_LOCATOR = (
        By.CSS_SELECTOR,
        "[class='isc-note note_icon ng-star-inserted']",
    )
    _TEXT_CONTENT_LOCATOR = (
        By.CSS_SELECTOR,
        "[class='advisor_parent_modal_content scrollbar']",
    )
    _CLICK_0N_OK_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "div.advisor_parent_modal_footer span.mat-button-wrapper",
    )
    _FINAL_ACCEPTED_STATUS_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'Final Acceptance')]",
    )
    _IMPERSONATION_LOCATOR = (By.XPATH, "//span[contains(text(),'Impersonate')]")

    document_strings = [r"\documents\passport_1.png", r"\documents\school_transcript.jpg",
                        r"\documents\university_transcript.jpg", r"\documents\bank_statement.png",
                        r"\documents\financial_support.png"]

    def switch_to_the_new_window(self):
        time.sleep(2)
        self.switch_to_new_window()
        return True

    # def switch_to_the_old_window(self):
    #     time.sleep(2)
    #     self.switch_to_old_window()
    #     time.sleep(5)
    #     return True

    def open_new_window(self):
        self.selenium.execute_script("window.open('');")
        return True

    def old_window(self):
        time.sleep(2)
        res = self.selenium.switch_to.window(self.selenium.window_handles[0])
        return res

    def click_on_sign_out(self):
        res = self.click_on_element(self._NEW_URL_SIGN_OUT)
        return res

    def click_on_degree_to_pursue(self):
        return self.click_on_element(self._DEGREE_LOCATOR)

    def click_on_discipline(self):
        self.scroll_into_view(self._DISCIPLINE_LOCATOR)
        return self.click_on_element(self._DISCIPLINE_LOCATOR)

    def click_on_year(self):
        return self.click_on_element(self._YEAR_LOCATOR)

    def click_on_season(self):
        return self.click_on_element(self._SEASON_LOCATOR)

    def click_on_done(self):
        time.sleep(2)
        return self.click_on_element(self._DONE_LOCATOR)

    def application_status_student_side(self, status):
        time.sleep(3)
        a = self.get_text_of_elements(self._STUDENT_SIDE_APPLICATION_STATUS)
        res1 = self.convert_list_to_string(a) == status
        print(res1)
        return res1

    def documentation_application_status_student(self):
        a = self.get_text_of_elements(self._STUDENT_SIDE_APPLICATION_STATUS)
        res1 = self.convert_list_to_string(a) == "Documentation "
        print(res1)
        return res1

    def under_review_application_status_student(self):
        time.sleep(5)
        a = self.get_text_of_elements(self._STUDENT_SIDE_APPLICATION_STATUS)
        res1 = self.convert_list_to_string(a) == "Under Review "
        print(res1)
        return res1

    def click_on_dashboard_button(self):
        time.sleep(2)
        return self.click_on_element(self._DASHBOARD_LOCATOR)

    def click_on_form_builder_radio_button(self):
        time.sleep(3)
        res = self.click_on_element(self._FORM_BUILDER_RADIO_BUTTON_LOCATOR)
        return res

    def verify_form_builder_radio_button(self):
        time.sleep(2)
        return self.check_page_element(self._FORM_BUILDER_RADIO_BUTTON_SELECTED_LOCATOR)

    # def check_mandatory_document(self):
    #     id_text = self.get_text_of_elements(self._MANDATORY_DOCUMENT_PASSPORT)
    #     print(self.convert_list_to_string(id_text))
    #     resume_text = self.get_text_of_elements(self._MANDATORY_DOCUMENT_SCHOOL)
    #     print(self.convert_list_to_string(resume_text))
    #     return (
    #         self.convert_list_to_string(id_text) in " Passport ",
    #         self.convert_list_to_string(resume_text)
    #         in " Secondary School transcripts ",
    #     )

    def click_on_upload_document(self):
        return self.click_on_element(self._UPLOAD_DOCUMENT)

    def select_school_transcript_document_type(self, document):
        time.sleep(5)
        res1 = self.scroll_into_view(self._DOCUMENT_TYPE_LOCATOR)
        res2 = self.enter_field_input(
            self._DOCUMENT_TYPE_LOCATOR, document
        )
        res3 = self.click_on_element(self._SCHOOL_TRANSCRIPT_DOCUMENT_LOCATOR)
        return res1, res2, res3

    def choose_school_transcript_document(self):
        self.click_on_element(self._SELECT_DOCUMENT_LOCATOR)
        time.sleep(2)
        pyautogui.write(
            os.getcwd() + self.document_strings[1]
        )  # find current dir and path of File
        pyautogui.press("enter")  # Click on Open
        return True

    def select_university_transcript_document_type(self, document):
        time.sleep(5)
        res1 = self.scroll_into_view(self._DOCUMENT_TYPE_LOCATOR)
        res2 = self.enter_field_input(self._DOCUMENT_TYPE_LOCATOR, document)
        res3 = self.click_on_element(self._UNIVERSITY_TRANSCRIPT_DOCUMENT_LOCATOR)
        return res1, res2, res3

    def click_financial_support_documents_button(self):
        res1 = self.scroll_into_view(self._DOCUMENT_TYPE_LOCATOR)
        res2 = self.enter_field_input(self._DOCUMENT_TYPE_LOCATOR, "financial")
        res3 = self.click_on_element(self._UNIVERSITY_TRANSCRIPT_DOCUMENT_LOCATOR)
        return res1, res2, res3

    def click_bank_statement_button(self):
        res1 = self.scroll_into_view(self._DOCUMENT_TYPE_LOCATOR)
        res2 = self.enter_field_input(self._DOCUMENT_TYPE_LOCATOR, "bank")
        res3 = self.click_on_element(self._UNIVERSITY_TRANSCRIPT_DOCUMENT_LOCATOR)
        return res1, res2, res3

    def choose_university_transcript_document(self):
        self.click_on_element(self._SELECT_DOCUMENT_LOCATOR)
        time.sleep(2)
        pyautogui.write(
            os.getcwd() + self.document_strings[2]
        )  # find current dir and path of File
        pyautogui.press("enter")  # Click on Open
        return True

    def choose_financial_support_document(self):
        self.click_on_element(self._SELECT_DOCUMENT_LOCATOR)
        time.sleep(2)
        pyautogui.write(
            os.getcwd() + self.document_strings[4]
        )  # find current dir and path of File
        pyautogui.press("enter")  # Click on Open
        return True

    def choose_bank_statement(self):
        self.click_on_element(self._SELECT_DOCUMENT_LOCATOR)
        time.sleep(2)
        pyautogui.write(
            os.getcwd() + self.document_strings[3]
        )  # find current dir and path of File
        pyautogui.press("enter")  # Click on Open
        return True

    def close_upload_doc_window(self):
        time.sleep(10)
        return self.click_on_element(self._CLOSE_DOCUMENT_WINDOW)

    def verify_send_for_review_text(self, status):
        a = self.get_text_of_elements(self._SEND_REVIEW_LOCATOR)
        res1 = self.convert_list_to_string(a) == status
        print(res1)
        return res1

    def click_on_upload_documents_radio_button(self):
        time.sleep(3)
        return self.click_on_element(self._UPLOAD_DOCUMENT_RADIO_BUTTON_LOCATOR)

    def click_on_sop_essay_radio_button(self):
        return self.click_on_element(self._SOP_ESSAY_RADIO_BUTTON_LOCATOR)

    def click_on_payment_radio_button(self):
        return self.click_on_element(self._PAYMENT_RADIO_BUTTON_LOCATOR)

    def click_on_send_for_review_button(self):
        res = self.click_on_element(self._SEND_REVIEW_LOCATOR)
        time.sleep(2)
        return res

    def verify_upload_documents_radio_button(self):
        time.sleep(2)
        return self.check_page_element(self._UPLOAD_DOCUMENT_RADIO_BUTTON_SELECTED_LOCATOR)

    def verify_sop_essay_radio_button(self):
        time.sleep(2)
        return self.check_page_element(self._SOP_AND_ESSAY_RADIO_BUTTON_SELECTED_LOCATOR)

    def verify_payment_radio_button(self):
        time.sleep(2)
        return self.check_page_element(self._PAYMENT_RADIO_BUTTON_SELECTED_LOCATOR)

    def click_on_university_accepted_yes_button(self):
        time.sleep(2)
        return self.click_on_element(self._UNIVERSITY_ACCEPTED_YES_BUTTON)

    def click_university_accepted_no_button(self):
        time.sleep(2)
        res = self.click_on_element(self._UNIVERSITY_ACCEPTED_NO_BUTTON)
        res1 = self.enter_field_input(
            self._UNIVERSITY_REJECTED_REASON, "Admit Rejected"
        )
        res3 = self.click_on_element(self._SAVE_BUTTON_LOCATOR)
        return res, res1, res3

    def admit_accepted_application_status_student(self):
        time.sleep(5)
        a = self.get_text_of_elements(self._STUDENT_SIDE_APPLICATION_STATUS)
        res1 = self.convert_list_to_string(a) == "Admit Accepted "
        print(res1)
        return res1

    def admit_rejected_application_status_student(self):
        time.sleep(5)
        a = self.get_text_of_elements(self._STUDENT_SIDE_APPLICATION_STATUS)
        res1 = self.convert_list_to_string(a) == "Admit Rejected "
        print(res1)
        return res1

    def final_acceptance_application_status_student(self):
        time.sleep(2)
        a = self.get_text_of_elements(self._STUDENT_SIDE_APPLICATION_STATUS)
        res1 = self.convert_list_to_string(a) == "Final Acceptance "
        print(res1)
        return res1

    def click_on_apply(self):
        res2 = self.click_on_element(self._APPLY_BUTTON_LIST)
        res3 = self.click_on_element(self._SEASON_LOCATOR)
        res5 = self.click_on_element(self._FINAL_APPLY)
        time.sleep(3)
        return res2 and res3 and res5

    # def check_apply_button(self):
    #     res = self.get_text_of_elements(self._APPLY_BUTTON_LIST)
    #     print(res)
    #     for i in res:
    #         print(i)
    #         if i == "Apply":
    #             res1 = self.click_on_apply
    #             return res1
    #     else:
    #         self.scroll_into_view(self._FORWARD_ARROW_BUTTON)
    #         return self.click_on_element(self._FORWARD_ARROW_BUTTON)

    def select_passport_document_type(self, document):
        time.sleep(3)
        self.scroll_into_view(self._DOCUMENT_TYPE_LOCATOR)
        self.enter_field_input(self._DOCUMENT_TYPE_LOCATOR, document)
        return self.click_on_element(self._PASSPORT_DOCUMENT_LOCATOR)

    def choose_passport1_document(self):
        self.click_on_element(self._SELECT_DOCUMENT_LOCATOR)
        time.sleep(2)
        path_parent = os.path.dirname(os.getcwd())
        os.chdir(path_parent)
        path_parent = os.path.dirname(os.getcwd())
        os.chdir(path_parent)
        pyautogui.write(
            os.getcwd() + self.document_strings[0]
        )  # find current dir and path of File
        pyautogui.press("enter")  # Click on Open
        return True

    def click_on_student_explore_school(self):
        return self.click_on_element(self._STUD_EXPLORE_SCHOOL_TAB_LOCATOR)

    def apply_on_application(self):
        res1 = self.click_on_element(self._APPLY)
        res2 = self.click_on_element(self._SELECT_YEAR)
        res3 = self.click_on_element(self._SELECT_SEASON)
        res4 = self.click_on_element(self._FINAL_APPLY)
        time.sleep(2)
        return res1 and res2 and res3 and res4

    def click_add_to_favorites_and_apply(self):
        self.scroll_into_view(self._ADD_TO_FAVOURITES)
        res1 = self.click_on_element(self._ADD_TO_FAVOURITES)
        time.sleep(2)
        res2 = self.apply_on_application()
        return res1 and res2

    def verify_added_to_favorites_and_applied(self):
        text_output_added_to_favorites = self.get_text_of_elements(
            self._ADD_TO_FAVOURITES
        )
        print(self.convert_list_to_string(text_output_added_to_favorites))
        text_output_applied = self.get_text_of_elements(self._APPLY)
        print(self.convert_list_to_string(text_output_applied))
        return (
            self.convert_list_to_string(text_output_added_to_favorites[0])
            == constants.ADDED_TO_FAVORITES,
            self.convert_list_to_string(text_output_applied[0]) == constants.APPLIED
        )

    def click_on_upload_button(self):
        return self.click_on_element(self._UPLOAD_BUTTON_LOCATOR)

    def click_on_return_to_impersonate_button(self):
        return self.click_on_element(self._RETURN_TO_IMPERSONATION_BUTTON_LOCATOR)

    def click_on_student_application_form(self):
        return self.click_on_element(self._STUDENT_APPLICATION_FORM)

    def search_for_student(self, name):
        res1 = self.enter_field_input(self._SEARCH_INPUT_LOCATOR, name)
        time.sleep(2)
        return res1

    def application_status_advisor_side(self, status):
        time.sleep(3)
        a = self.get_text_of_elements(self._ADVISOR_SIDE_APPLICATION_STATUS)
        res1 = self.convert_list_to_string(a) == status
        print(res1)
        return res1

    def click_on_change_status_option(self):
        return self.click_on_element(self._CHANGE_STATUS_LOCATOR)

    def change_status_to_on_hold(self):
        res = self.click_on_element(self._ON_HOLD_LOCATOR)
        res2 = self.enter_field_input(self._REASON_INPUT_TEXT_LOCATOR, "On Hold text")
        res3 = self.click_on_element(self._SAVE_BUTTON_LOCATOR)
        return res, res2, res3

    def change_status_to_under_review(self):
        res = self.click_on_element(self._UNDER_REVIEW_STATUS_LOCATOR)
        res2 = self.enter_field_input(
            self._REASON_INPUT_TEXT_LOCATOR, "Under Review Text"
        )
        res3 = self.click_on_element(self._SAVE_BUTTON_LOCATOR)
        return res, res2, res3

    def change_status_to_review_passed(self):
        res = self.click_on_element(self._REVIEW_PASSED_LOCATOR)
        res2 = self.enter_field_input(
            self._REASON_INPUT_TEXT_LOCATOR, "Review passed text"
        )
        res3 = self.click_on_element(self._SAVE_BUTTON_LOCATOR)
        return res, res2, res3

    def change_status_to_awaiting_result(self):
        res = self.click_on_element(self._AWAITING_RESULT_LOCATOR)
        res2 = self.enter_field_input(
            self._REASON_INPUT_TEXT_LOCATOR, "Awaiting Results text"
        )
        res3 = self.click_on_element(self._SAVE_BUTTON_LOCATOR)
        return res, res2, res3

    def check_review_passed_ticket_text(self):
        self.click_on_element(self._CLICK_ON_TICKET_LOCATOR)
        a = self.get_text_of_elements(self._TEXT_CONTENT_LOCATOR)
        res = self.convert_list_to_string(a) == "Review passed text"
        print(res)
        self.click_on_element(self._CLICK_0N_OK_BUTTON_LOCATOR)
        return True

    def admit_rejected_check_ticket_text(self):
        self.click_on_element(self._CLICK_ON_TICKET_LOCATOR)
        a = self.get_text_of_elements(self._TEXT_CONTENT_LOCATOR)
        res = self.convert_list_to_string(a) == "Admit Rejected"
        print(res)
        self.click_on_element(self._CLICK_0N_OK_BUTTON_LOCATOR)
        return True

    def check_awaiting_result_ticket_text(self):
        self.click_on_element(self._CLICK_ON_TICKET_LOCATOR)
        a = self.get_text_of_elements(self._TEXT_CONTENT_LOCATOR)
        res = self.convert_list_to_string(a) == "Awaiting Results text"
        print(res)
        self.click_on_element(self._CLICK_0N_OK_BUTTON_LOCATOR)
        return True

    def change_status_to_conditional_acceptance(self):
        res = self.click_on_element(self._CONDITIONAL_ACCEPTED_LOCATOR)
        res2 = self.enter_field_input(
            self._REASON_INPUT_TEXT_LOCATOR, "Conditional Acceptance text"
        )
        res3 = self.click_on_element(self._SAVE_BUTTON_LOCATOR)
        return res, res2, res3

    def change_status_to_additional_screening(self):
        res = self.click_on_element(self._ADDITIONAL_SCREENING_LOCATOR)
        res2 = self.enter_field_input(
            self._REASON_INPUT_TEXT_LOCATOR, "Additional Screening text"
        )
        res3 = self.click_on_element(self._SAVE_BUTTON_LOCATOR)
        return res, res2, res3

    def change_status_to_university_accepted(self):
        res = self.click_on_element(self._UNIVERSITY_ACCEPTED_LOCATOR)
        res2 = self.enter_field_input(
            self._REASON_INPUT_TEXT_LOCATOR, "University Accepted text"
        )
        res3 = self.click_on_element(self._SAVE_BUTTON_LOCATOR)
        return res, res2, res3

    def change_status_to_financial_documentation(self):
        res = self.click_on_element(self._FINANCIAL_DOCUMENTATION_LOCATOR)
        res2 = self.enter_field_input(
            self._REASON_INPUT_TEXT_LOCATOR, "Financial Documentation text"
        )
        res3 = self.click_on_element(self._SAVE_BUTTON_LOCATOR)
        return res, res2, res3

    def change_status_final_acceptance(self):
        res = self.click_on_element(self._FINAL_ACCEPTED_STATUS_LOCATOR)
        res2 = self.enter_field_input(
            self._REASON_INPUT_TEXT_LOCATOR, "Final Acceptance text"
        )
        res3 = self.click_on_element(self._SAVE_BUTTON_LOCATOR)
        return res, res2, res3

    def click_on_action_button_manage_application(self):
        time.sleep(5)
        hover_ele = self.selenium.find_element_by_xpath("//tbody/tr[1]/td[1]")
        action = ActionChains(self.selenium)
        action.move_to_element(hover_ele).perform()
        action.click(hover_ele)
        action_button = self.selenium.find_element_by_css_selector(
            "#undefined button .mat-button-wrapper"
        )
        action.move_to_element(action_button).perform()
        action_button.click()
        time.sleep(2)
        return True

    def click_on_impersonate_button_university_accepted(self):
        res1 = self.click_on_element(self._IMPERSONATION_LOCATOR)
        res2 = self.click_on_element(self._IMPERSONATION_YES_BUTTON_LOCATOR)
        time.sleep(5)
        return res1, res2

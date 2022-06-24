import time

from selenium.webdriver.common.by import By

import constants
from pages.base_page import BasePage


class RecommendationReportPage(BasePage):
    _SHARE_RECOMMENDATION_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(),' Share ')]")
    _ENTER_EMAIL_IN_INPUT_FIELD_LOCATOR = (By.XPATH, "//input[@name='email']")
    _ADD_EMAIL_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")
    _FINAL_SHARE = (By.ID, "save_button")
    _EDIT_RECOMMENDATION_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(),'Edit Recommendations')]")
    _EDIT_RECOMMENDATION_OK_BUTTON = (By.XPATH, "//button[@class='isc-btn sm btn-primary']")
    _DELETE_UNIVERSITY_FROM_SAFE_BUCKET_LOCATOR = (
        By.XPATH,
        "//isc-reco-drs-section[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/i[1]",
    )
    _SELECT_FEEDBACK_DROP_DOWN_LOCATOR = (By.XPATH, "//span[@class='ng-arrow-wrapper']")
    _SELECT_FEEDBACK_OPTION_LOCATOR = (
        By.CSS_SELECTOR,
        "[aria-label='Options list'] [role='option']",
    )
    _SAVE_FEEDBACK_BUTTON_LOCATOR = (By.ID, "save_button")
    _SAVE_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(),'Save')]")
    _RECOMMENDATION_ADD_COURSE_TO_FAVOURITES_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "#drs_section_dream_0 isc-shortlist-button span.mat-button-wrapper span ",
    )
    _RECOMMENDATION_APPLY_LOCATOR = (
        By.CSS_SELECTOR,
        "#drs_section_dream_0 isc-apply-button button span.mat-button-wrapper",
    )
    _APPLICATION_CYCLE_YEAR_BUTTON_LOCATOR = (By.XPATH, "//*[contains(text(),'2023')]")
    _APPLICATION_CYCLE_SEASON_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[for='application_cycle_season-0']")
    _APPLICATION_CYCLE_APPLY_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#save_button > span.mat-button-wrapper")
    _CANCEL_APPLICATION_CONFIRMATION_LOCATOR = (By.ID, "yes_button")
    _OUTPUT_TEXT_DREAM = (By.XPATH, "//h5[@class='title text-dream']")
    _OUTPUT_TEXT_SAFE = (By.XPATH, "//h5[@class='title text-safe']")
    _OUTPUT_TEXT_UNIVERSITY_COURSE = (By.XPATH, "//h5[@class='course']/span[1]")

    discipline = ["Computer", "Computer Science", "Data",
                  "Agriculture", "Agriculture Science", "soil"]

    def click_on_share_button(self):
        self.scroll_into_view(self._SHARE_RECOMMENDATION_BUTTON_LOCATOR)
        return self.click_on_element(self._SHARE_RECOMMENDATION_BUTTON_LOCATOR)

    def text_input_enter_email(self, email):
        return self.enter_field_input(self._ENTER_EMAIL_IN_INPUT_FIELD_LOCATOR, email)

    def click_on_add_button(self):
        return self.click_on_element(self._ADD_EMAIL_BUTTON_LOCATOR)

    def click_on_final_share_button(self):
        return self.click_on_element(self._FINAL_SHARE)

    def click_on_edit_button(self):
        self.scroll_into_view(self._SHARE_RECOMMENDATION_BUTTON_LOCATOR)
        return self.click_on_element(self._EDIT_RECOMMENDATION_BUTTON_LOCATOR)

    def click_on_edit_ok_button(self):
        return self.click_on_element(self._EDIT_RECOMMENDATION_OK_BUTTON)

    def click_on_delete_button(self):
        return self.click_on_element(self._DELETE_UNIVERSITY_FROM_SAFE_BUCKET_LOCATOR)

    def click_on_feedback_field(self):
        res1 = self.click_on_element(self._SELECT_FEEDBACK_DROP_DOWN_LOCATOR)
        res2 = self.click_on_element(self._SELECT_FEEDBACK_OPTION_LOCATOR)
        return res1 and res2

    def click_on_feedback_save_button(self):
        return self.click_on_element(self._SAVE_FEEDBACK_BUTTON_LOCATOR)

    def click_on_save_button(self):
        time.sleep(3)
        return self.click_on_element(self._SAVE_BUTTON_LOCATOR)

    def get_add_to_favourites_text(self, text_result):
        text_output = self.get_text_of_elements(self._RECOMMENDATION_ADD_COURSE_TO_FAVOURITES_BUTTON_LOCATOR)
        print(self.convert_list_to_string(text_output))
        return self.convert_list_to_string(text_output[0]) == text_result

    def click_on_add_to_favorites_button(self):
        self.scroll_into_view(self._RECOMMENDATION_ADD_COURSE_TO_FAVOURITES_BUTTON_LOCATOR)
        return self.click_on_element(self._RECOMMENDATION_ADD_COURSE_TO_FAVOURITES_BUTTON_LOCATOR)

    def click_on_add_to_favorites(self):
        return self.click_on_add_to_favorites()

    def get_apply_button_text(self, text_result):
        text_output = self.get_text_of_elements(self._RECOMMENDATION_APPLY_LOCATOR)
        print(self.convert_list_to_string(text_output))
        return self.convert_list_to_string(text_output[0]) == text_result

    def click_on_apply_button(self):
        return self.click_on_element(self._RECOMMENDATION_APPLY_LOCATOR)

    def fill_application_cycle_form(self):
        self.click_on_element(self._APPLICATION_CYCLE_YEAR_BUTTON_LOCATOR)
        self.click_on_element(self._APPLICATION_CYCLE_SEASON_BUTTON_LOCATOR)
        return self.click_on_element(self._APPLICATION_CYCLE_APPLY_BUTTON_LOCATOR)

    def check_for_dream_bucket_text_output(self):
        self.scroll_into_view(self._OUTPUT_TEXT_DREAM)
        time.sleep(3)
        a = self.get_text_of_elements(self._OUTPUT_TEXT_DREAM)
        print(self.convert_list_to_string(a))
        return self.convert_list_to_string(a) == constants.DREAM_BUCKET

    def check_for_safe_bucket_text_output(self):
        self.scroll_into_view(self._OUTPUT_TEXT_SAFE)
        time.sleep(3)
        a = self.get_text_of_elements(self._OUTPUT_TEXT_SAFE)
        print(self.convert_list_to_string(a))
        return self.convert_list_to_string(a) == constants.SAFE_BUCKET

    def check_for_output_university_course(self):
        course = self.get_text_of_elements(self._OUTPUT_TEXT_UNIVERSITY_COURSE)
        print(self.convert_list_to_string(course))
        if (
                self.discipline[0] or self.discipline[1] or self.discipline[2]
        ) in self.convert_list_to_string(course):
            return True

    def check_for_output_agriculture_university_course(self):
        course = self.get_text_of_elements(self._OUTPUT_TEXT_UNIVERSITY_COURSE)
        print(self.convert_list_to_string(course))
        if (
                self.discipline[3] or self.discipline[4] or self.discipline[5]
        ) in self.convert_list_to_string(course):
            return True

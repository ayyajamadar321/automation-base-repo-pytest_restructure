from __future__ import print_function
import random
import time
from selenium.webdriver.common.by import By
import constants
from pages.base_page import BasePage


class KaplanRecoPage(BasePage):
    _RECOMMENDATIONS_LOCATOR = (By.LINK_TEXT, "Recommendations")
    _REFINE_PROFILE_LOCATOR = (By.CSS_SELECTOR, "button#refine_profile_button")
    _SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(),'Submit')]")
    _SELECT_CS_SPECIALIZATION_DROP_DOWN_LOCATOR = (
        By.XPATH,
        "//p[contains(text(),'Computer Science')]",
    )
    _BACHELORS_HIGH_SCHOOL_SCORE = (
        By.XPATH,
        "//formly-field[1]/isc-reco-tests[1]/formly-group[1]/formly-field[1]/isc-reco-single-score[1]/input[1]",
    )
    _BUDGET_INPUT_LOCATOR = (By.XPATH, "//input[@placeholder='Eg. 30000 (in USD)']")
    _COUNTRY_ENABLE_BUTTON = (
        By.CSS_SELECTOR,
        '[class="relative option ng-star-inserted active"]',
    )
    _HIGH_SCHOOL_SCORE_ERROR_MESSAGE_LOCATOR = (
        By.XPATH,
        "//*[contains(text(),'Your score must be less than 4.')]",
    )
    _BUDGET_ERROR_MESSAGE_LOCATOR = (
        By.XPATH,
        "//*[contains(text(),'Budget range should be between 0 to 1,00,000')]",
    )
    _STUDENT_PROFILE_DROPDOWN_LOCATOR = (
        By.CSS_SELECTOR,
        "#parentStudentDashboardDiv app-header ngx-avatar",
    )
    _VALIDATE_SUB_DISCIPLINES_LOCATOR = (
        By.CSS_SELECTOR,
        "#subdisciplines span.ng-value-label.ng-star-inserted",
    )
    _VALIDATE_DISCIPLINES_LOCATOR = (
        By.CSS_SELECTOR,
        "#disciplines span.ng-value-label.ng-star-inserted",
    )
    _SELECT_AGRICULTURE_ENGINEERING_SPECIALIZATION_DROP_DOWN_LOCATOR = (
        By.XPATH,
        "//p[contains(text(),'Agricultural Engineering')]",
    )
    _SELECT_AGRICULTURE_SCIENCE_SPECIALIZATION_DROP_DOWN_LOCATOR = (
        By.XPATH,
        "//p[contains(text(),'Agricultural Science')]",
    )
    _EXAM_LIST_LOCATOR = (By.CSS_SELECTOR, "#high_school_gpa_score")
    _SELECT_GPA_SCORE_LOCATOR = (By.XPATH, "//div[contains(text(),'GPA(4)')]")
    _SELECT_CGPA_SCORE_LOCATOR = (By.XPATH, "//div[contains(text(),'CGPA(10)')]")
    _SELECT_PERCENTAGE_SCORE_LOCATOR = (
        By.XPATH,
        "//div[contains(text(),'Percentage (100)')]",
    )

    # ***************************** Kaplan Exam *******************************
    _KAPLAN_SPECIALIZATION_INPUT_LOCATOR = (By.CSS_SELECTOR,
                                            '#mat-chip-list-1 input')
    _KAPLAN_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "isc-reco-tests formly-field:nth-child(1) > isc-reco-tests > div > formly-validation-message",
    )
    _UNDERGRAD_SPECIALIZATION_INPUT = (By.CSS_SELECTOR, "#undergrad_specialization input[type=text]")
    _KAPLAN_UNDERGRAD_SPECIALIZATION_DROP_DOWN = (By.CSS_SELECTOR, "[role='option']")
    _KAPLAN_UNDERGRAD_SCORE_LOCATOR = (By.XPATH, "//isc-reco-tests/formly-group/formly-field["
                                                 "4]/isc-reco-tests/formly-group/formly-field["
                                                 "1]/isc-reco-single-score/input")
    _KAPLAN_BACHELORS_HIGH_SCHOOL_SCORE = (
        By.XPATH,
        "//formly-field[1]/isc-reco-tests[1]/formly-group[1]/formly-field[1]/isc-reco-single-score[1]/input[1]",
    )
    _KAPLAN_LEVEL_LOCATOR = (By.XPATH, "//label[@for='english_tests-0']")
    # ********************************* Kaplan English Exam Test *******************
    _SELECT_ENGLISH_TEST_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'English Test Score')]",
    )
    _EXAM_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(10) formly-wrapper-animation isc-reco-tests > div > formly-validation-message",
    )
    _EXAM_IELTS_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(4) > formly-wrapper-animation > div > isc-reco-tests > div > formly-validation-message",
    )
    _EXAM_TOEFL_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(6) formly-field:nth-child(5)  div > isc-reco-tests > div > formly-validation-message",
    )
    _EXAM_KITE_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(6) formly-field:nth-child(6) > formly-wrapper-animation isc-reco-tests > div > "
        "formly-validation-message",
    )
    _EXAM_CAE_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(6) formly-field:nth-child(7) > formly-wrapper-animation > div > isc-reco-tests > div "
        "> formly-validation-message",
    )
    _INPUT_IELTS_EXAM_SCORE_LOCATOR = (
        By.CSS_SELECTOR,
        "[placeholder='Out of 9']",
    )
    _INPUT_TOEFL_EXAM_SCORE_LOCATOR = (
        By.CSS_SELECTOR,
        "[placeholder='Out of 120']",
    )
    _INPUT_KITE_EXAM_SCORE_LOCATOR = (
        By.CSS_SELECTOR,
        "[placeholder='Out of 700']",
    )
    _INPUT_CAE_EXAM_SCORE_LOCATOR = (By.CSS_SELECTOR, "[placeholder='80 - 230']")
    _SELECT_IELTS_BUTTON_LOCATOR = (By.XPATH, "//label[@for='test_name-0']")
    _SELECT_TOEFL_BUTTON_LOCATOR = (By.XPATH, "//label[@for='test_name-1']")
    _SELECT_KITE_BUTTON_LOCATOR = (By.XPATH, "//label[@for='test_name-2']")
    _SELECT_CAE_BUTTON_LOCATOR = (By.XPATH, "//label[@for='test_name-3']")
    _ENGLISH_TEST_SCORE_LOCATOR = (By.ID, "english_tests-1")
    _ELEMENTARY_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[for='kaplan_level-0']")
    _LOWER_INTERMEDIATE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[for='kaplan_level-1']")
    _INTERMEDIATE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[for='kaplan_level-2']")
    _HIGHER_INTERMEDIATE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[for='kaplan_level-3']")
    _ADVANCED_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[for='kaplan_level-4']")
    _PROFICIENCY_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[for='kaplan_level-5']")

    select_kaplan_level = [
        _ELEMENTARY_BUTTON_LOCATOR,
        _LOWER_INTERMEDIATE_BUTTON_LOCATOR,
        _HIGHER_INTERMEDIATE_BUTTON_LOCATOR,
        _INTERMEDIATE_BUTTON_LOCATOR,
        _ADVANCED_BUTTON_LOCATOR,
        _PROFICIENCY_BUTTON_LOCATOR
    ]
    # ***************************** countries *****************************
    _AUS_COUNTRY_LOCATOR = (
        By.XPATH,
        "//label[@for='countries-2']",
    )
    _CAN_COUNTRY_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'CAN')]",
    )
    _GBR_COUNTRY_LOCATOR = (
        By.XPATH,
        "//label[@for='countries-3']",
    )
    _USA_COUNTRY_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'USA')]",
    )
    select_country_to_study = [
        _USA_COUNTRY_LOCATOR,
        _CAN_COUNTRY_LOCATOR,
        _GBR_COUNTRY_LOCATOR,
        _AUS_COUNTRY_LOCATOR,
    ]
    # ***************************** Certifications *******************************
    _SELECT_CERTIFICATION_YES_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='taken_certifications-1']",
    )
    _SELECT_CERTIFICATION_NO_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='taken_certifications-0']",
    )
    _EXTRA_CURRICULAR_CERTIFICATION_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='certification_type-0']",
    )
    _VOLUNTEERING_CERTIFICATION_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='certification_type-1']",
    )
    _BOTH_CERTIFICATION_BUTTON = (By.CSS_SELECTOR, "[for ='certification_type-2']")
    _ONE_CERTIFICATION_BUTTON = (By.CSS_SELECTOR, "[for ='certification_number-0']")
    _TWO_CERTIFICATION_BUTTON = (By.CSS_SELECTOR, "[for ='certification_number-1']")
    _THREE_CERTIFICATION_BUTTON = (By.CSS_SELECTOR, "[for ='certification_number-2']")
    _MORE_THAN_THREE_CERTIFICATION_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='certification_number-3']",
    )
    select_isc_certifications = [
        _EXTRA_CURRICULAR_CERTIFICATION_BUTTON,
        _VOLUNTEERING_CERTIFICATION_BUTTON,
        _BOTH_CERTIFICATION_BUTTON,
    ]
    select_number_of_certifications = [
        _ONE_CERTIFICATION_BUTTON,
        _TWO_CERTIFICATION_BUTTON,
        _THREE_CERTIFICATION_BUTTON,
        _MORE_THAN_THREE_CERTIFICATION_BUTTON,
    ]
    # ***************************** Aptitude Test *******************************
    _NO_APTITUDE_TEST = (By.CSS_SELECTOR, "[for ='aptitude_test-0']")
    _SAT_APTITUDE_TEST_BUTTON = (By.CSS_SELECTOR, "[for ='aptitude_test-1']")
    _ACT_APTITUDE_TEST_BUTTON = (By.CSS_SELECTOR, "[for ='aptitude_test-2']")
    _INPUT_SAT_APTITUDE_TEST = (By.CSS_SELECTOR, "#formly_51_single-score_total_0")
    _INPUT_ACT_APTITUDE_TEST = (By.CSS_SELECTOR, "#formly_52_single-score_total_0")
    _SAT_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(4) > formly-wrapper-animation > div > isc-reco-tests > div > formly-validation-message",
    )
    _ACT_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(5) > formly-wrapper-animation > div > isc-reco-tests > div > formly-validation-message",
    )

    def click_on_recommendations_button(self):
        return self.click_on_element(self._RECOMMENDATIONS_LOCATOR)

    def click_on_refine_profile_button(self):
        return self.click_on_element(self._REFINE_PROFILE_LOCATOR)

    def click_on_isc_degree_to_pursue(self):
        return self.click_on_element(random.choice(self.select_country_to_study))

    def kaplan_enter_input_in_preferred_specialization(self, specialization):
        self.scroll_into_view(self._KAPLAN_SPECIALIZATION_INPUT_LOCATOR)
        return self.enter_field_input(
            self._KAPLAN_SPECIALIZATION_INPUT_LOCATOR, specialization
        )

    def kaplan_enter_computer_science_specialization(self, specialization):
        res1 = self.kaplan_enter_input_in_preferred_specialization(specialization)
        time.sleep(2)
        res2 = self.click_on_element(self._SELECT_CS_SPECIALIZATION_DROP_DOWN_LOCATOR)
        return res1 and res2

    def kaplan_enter_agriculture_engineering_specialization(self, specialization):
        res1 = self.kaplan_enter_input_in_preferred_specialization(specialization)
        time.sleep(2)
        res2 = self.click_on_element(self._SELECT_AGRICULTURE_ENGINEERING_SPECIALIZATION_DROP_DOWN_LOCATOR)
        return res1 and res2

    def kaplan_enter_agriculture_science_specialization(self, specialization):
        res1 = self.kaplan_enter_input_in_preferred_specialization(specialization)
        time.sleep(2)
        res2 = self.click_on_element(self._SELECT_AGRICULTURE_SCIENCE_SPECIALIZATION_DROP_DOWN_LOCATOR)
        return res1 and res2

    def click_on_exam_list(self):
        return self.click_on_element(self._EXAM_LIST_LOCATOR)

    def get_kaplan_ielts_exam_error_message(self):
        error_message = self.get_text_of_elements(self._EXAM_IELTS_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.IELTS_EXAM_ERROR_MESSAGE

    def enter_kaplan_ielts_exam_score(self, mark):
        return self.enter_field_input(self._INPUT_IELTS_EXAM_SCORE_LOCATOR, mark)

    def click_on_kaplan_ielts_exam(self, mark):
        self.click_on_element(self._SELECT_IELTS_BUTTON_LOCATOR)
        self.enter_kaplan_ielts_exam_score(mark)
        return self.get_kaplan_ielts_exam_error_message()

    def enter_kaplan_toefl_exam_score(self, mark):
        return self.enter_field_input(self._INPUT_TOEFL_EXAM_SCORE_LOCATOR, mark)

    def get_kaplan_toefl_exam_error_message(self):
        error_message = self.get_text_of_elements(self._EXAM_TOEFL_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.TOEFL_EXAM_ERROR_MESSAGE

    def click_on_kaplan_toefl_exam(self, mark):
        self.click_on_element(self._SELECT_TOEFL_BUTTON_LOCATOR)
        self.enter_kaplan_toefl_exam_score(mark)
        return self.get_kaplan_toefl_exam_error_message()

    def enter_kaplan_kite_exam_score(self, mark):
        return self.enter_field_input(self._INPUT_KITE_EXAM_SCORE_LOCATOR, mark)

    def get_kaplan_kite_exam_error_message(self):
        error_message = self.get_text_of_elements(self._EXAM_KITE_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.KITE_EXAM_ERROR_MESSAGE

    def click_on_kaplan_kite_exam(self, mark):
        self.click_on_element(self._SELECT_KITE_BUTTON_LOCATOR)
        self.enter_kaplan_kite_exam_score(mark)
        return self.get_kaplan_kite_exam_error_message()

    def get_kaplan_cae_exam_error_message(self):
        error_message = self.get_text_of_elements(self._EXAM_CAE_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return (
                self.convert_list_to_string(error_message) == constants.CAE_EXAM_ERROR_MESSAGE
        )

    def enter_kaplan_cae_exam_score(self, mark):
        return self.enter_field_input(self._INPUT_CAE_EXAM_SCORE_LOCATOR, mark)

    def click_on_kaplan_cae_exam(self, mark):
        self.click_on_element(self._SELECT_CAE_BUTTON_LOCATOR)
        self.enter_kaplan_cae_exam_score(mark)
        return self.get_kaplan_cae_exam_error_message()

    def click_on_kaplan_level_button(self):
        self.scroll_into_view(self._KAPLAN_LEVEL_LOCATOR)
        return self.click_on_element(self._KAPLAN_LEVEL_LOCATOR)

    def select_random_kaplan_level(self):
        return self.click_on_element(random.choice(self.select_kaplan_level))

    def click_and_apply_kaplan_level(self):
        self.click_on_kaplan_level_button()
        return self.select_random_kaplan_level()

    def click_on_english_test_score(self):
        self.scroll_into_view(self._SELECT_ENGLISH_TEST_LOCATOR)
        return self.click_on_element(self._SELECT_ENGLISH_TEST_LOCATOR)

    def enter_input_in_budget_field(self, budget):
        return self.enter_field_input(self._BUDGET_INPUT_LOCATOR, budget)

    def click_on_budget_field(self, budget):
        self.scroll_to_down()
        res1 = self.click_on_element(self._BUDGET_INPUT_LOCATOR)
        res2 = self.enter_input_in_budget_field(budget)
        return res1 and res2

    def click_on_submit_button(self):
        self.scroll_to_down()
        return self.click_on_element(self._SUBMIT_BUTTON_LOCATOR)

    def check_budget_error_message(self):
        error_message = self.get_text_of_elements(self._BUDGET_ERROR_MESSAGE_LOCATOR)
        print(self.convert_list_to_string(error_message))
        res1 = self.convert_list_to_string(error_message) == constants.BUDGET_FIELD_VALIDATION
        return res1

    def click_on_no_aptitude_test(self):
        time.sleep(2)
        return self.click_on_element(self._NO_APTITUDE_TEST)

    def click_on_kaplan_english_test_button(self):
        self.scroll_into_view(self._SELECT_ENGLISH_TEST_LOCATOR)
        return self.click_on_element(self._SELECT_ENGLISH_TEST_LOCATOR)

    def click_on_country_of_study(self):
        time.sleep(3)
        res1 = self.click_on_element(self._CAN_COUNTRY_LOCATOR)
        res2 = self.click_on_element(self._USA_COUNTRY_LOCATOR)
        return res1 and res2

    def check_multiple_option_enable_for_country(self):
        return self.check_page_element(self._COUNTRY_ENABLE_BUTTON)

    def get_error_message_for_gpa(self):
        error_message = self.get_text_of_elements(self._KAPLAN_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.GPA_EXAM_ERROR_MESSAGE

    def click_on_gpa_and_validate(self, mark):
        self.enter_field_input(self._BACHELORS_HIGH_SCHOOL_SCORE, mark)
        return self.get_error_message_for_gpa()

    def get_error_message_for_cgpa(self):
        error_message = self.get_text_of_elements(self._KAPLAN_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.CGPA_EXAM_ERROR_MESSAGE

    def click_on_exam_drop_down(self):
        return self.click_on_element(self._EXAM_LIST_LOCATOR)

    def click_on_cgpa_and_validate(self):
        time.sleep(2)
        self.click_on_exam_drop_down()
        self.click_on_element(self._SELECT_CGPA_SCORE_LOCATOR)
        return self.get_error_message_for_cgpa()

    def get_error_message_for_high_school(self):
        error_message = self.get_text_of_elements(self._KAPLAN_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.HIGH_SCHOOL_PERCENTAGE_ERROR_MESSAGE

    def click_on_percentage_high_school_score(self):
        time.sleep(2)
        self.click_on_exam_drop_down()
        self.click_on_element(self._SELECT_PERCENTAGE_SCORE_LOCATOR)
        return self.get_error_message_for_high_school()

    def click_on_kaplan_high_school_Score(self, mark):
        self.click_on_exam_drop_down()
        self.click_on_element(self._SELECT_GPA_SCORE_LOCATOR)
        return self.enter_field_input(self._KAPLAN_BACHELORS_HIGH_SCHOOL_SCORE, mark)

    def enter_kaplan_undergrad_specialization(self, discipline):
        res = self.scroll_into_view(self._UNDERGRAD_SPECIALIZATION_INPUT)
        res1 = self.enter_field_input(self._UNDERGRAD_SPECIALIZATION_INPUT, discipline)
        return res, res1

    def enter_kaplan_undergrad_score(self, mark):
        res = self.click_on_element(self._KAPLAN_UNDERGRAD_SPECIALIZATION_DROP_DOWN)
        res1 = self.enter_field_input(self._KAPLAN_UNDERGRAD_SCORE_LOCATOR, mark)
        return res, res1

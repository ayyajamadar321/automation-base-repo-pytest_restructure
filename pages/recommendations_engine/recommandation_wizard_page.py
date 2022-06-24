import random
import time
from selenium.webdriver.common.by import By

import constants
from pages.base_page import BasePage


class RecommendationWizardPage(BasePage):
    _GENERATE_RECOMMENDATION = (
        By.XPATH,
        "//span[contains(text(),' Generate Recommendations ')]",
    )
    _AUS_COUNTRY_LOCATOR = (
        By.XPATH,
        "//label[@for='countries-2']",
    )
    _CAN_COUNTRY_LOCATOR = (
        By.XPATH,
        "//label[@for='countries-0']",
    )
    _GBR_COUNTRY_LOCATOR = (
        By.XPATH,
        "//label[@for='countries-3']",
    )
    _USA_COUNTRY_LOCATOR = (
        By.XPATH,
        "//label[@for='countries-5']",
    )
    _UNDERGRADUATE_DEGREE_LOCATOR = (
        By.XPATH,
        "//label[contains(text(),'undergraduate')]",
    )
    _GRADUATE_DEGREE_LOCATOR = (By.XPATH, "")
    _MASTER_DEGREE_LOCATOR = (By.XPATH, "//span[contains(text(),'Masters')]")
    _BACHELORS_DEGREE_LOCATOR = (By.XPATH, "//span[contains(text(),'Bachelors')]")
    _DOCTORATE_DEGREE_LOCATOR = (By.XPATH, "//span[@for='degrees-2']")
    _ASSOCIATE_DEGREE_LOCATOR = (By.XPATH, "//span[contains(text(),'Associate')]")
    _DIPLOMA_DEGREE_LOCATOR = (By.XPATH, "//span[contains(text(),'Diploma')]")
    _PGA_DEGREE_LOCATOR = (By.XPATH, "//span[@for='degrees-7']")
    _SPECIALIZATION_INPUT_LOCATOR = (By.CSS_SELECTOR,
                                     '[class="mat-chip-list-wrapper"] input')
    _KAPLAN_SPECIALIZATION_INPUT_LOCATOR = (By.CSS_SELECTOR,
                                            '[class="ng-untouched ng-invalid ng-dirty"] input')
    _SELECT_CS_SPECIALIZATION_DROP_DOWN_LOCATOR = (
        By.XPATH,
        "//p[contains(text(),'Computer Science')]",
    )
    _SELECT_AGRICULTURE_ENGINEERING_SPECIALIZATION_DROP_DOWN_LOCATOR = (
        By.XPATH,
        "//p[contains(text(),'Agricultural Engineering')]",
    )
    _SELECT_AGRICULTURE_SCIENCE_SPECIALIZATION_DROP_DOWN_LOCATOR = (
        By.XPATH,
        "//p[contains(text(),'Agricultural Science')]",
    )
    _SUB_DISCIPLINES_INPUT_LOCATOR = (By.CSS_SELECTOR, "#subdisciplines input")
    _INPUT_ISC_BACHELORS_HIGH_SCHOOL_SCORE = (
        By.CSS_SELECTOR,
        "input.input__normalizer.ng-dirty.ng-valid",
    )
    _UNDERGRAD_SCHOOL_INPUT_LOCATOR = (By.XPATH, "//formly-field[2]//isc-reco-single-score[1]/input[1]")
    _UNDERGRAD_SPECIALIZATION_INPUT_LOCATOR = (By.ID, "undergrad_specialization")
    _BACHELORS_HIGH_SCHOOL_SCORE = (
        By.XPATH,
        "//formly-field[1]/isc-reco-tests[1]/formly-group[1]/formly-field[1]/isc-reco-single-score[1]/input[1]",
    )
    _KAPLAN_LEVEL_LOCATOR = (By.XPATH, "//label[@for='english_tests-0']")
    _ENGLISH_TEST_SCORE_LOCATOR = (By.ID, "english_tests-1")
    _ELEMENTARY_BUTTON_LOCATOR = (By.ID, "kaplan_level-0")
    _LOWER_INTERMEDIATE_BUTTON_LOCATOR = (By.ID, "kaplan_level-1")
    _INTERMEDIATE_BUTTON_LOCATOR = (By.XPATH, "//label[@for='kaplan_level-2']")
    _HIGHER_INTERMEDIATE_BUTTON_LOCATOR = (By.ID, "kaplan_level-3")
    _ADVANCED_BUTTON_LOCATOR = (By.ID, "kaplan_level-4")
    _PROFICIENCY_BUTTON_LOCATOR = (By.ID, "kaplan_level-5")
    _SEARCH_BY_INPUT_LOCATOR = (By.ID, "filter_category")
    _BUDGET_INPUT_LOCATOR = (By.CSS_SELECTOR, "isc-reco-single-score input")
    _SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(),'Submit')]")
    _HIGH_SCHOOL_ERROR_MSG = (
        By.XPATH,
        "//*[contains(text(),'Your score must be less than 4.')]",
    )
    _BUDGET_ERROR_MSG = (
        By.XPATH,
        "//*[contains(text(),'Budget range should be between 0 to 1,00,000')]",
    )
    _NEXT_PAGE_LOCATOR = (By.XPATH, "//*[contains(text(),'Next')]")
    _INVALID_EMAIL_ERROR_LOCATOR = (By.CSS_SELECTOR, "[class='error ng-star-inserted']")
    _COUNTRY_ENABLE_BUTTON = (
        By.CSS_SELECTOR,
        '[class="relative option ng-star-inserted active"]',
    )
    _DEGREE_ENABLE_BUTTON = (
        By.CSS_SELECTOR,
        "fieldset div.option.ng-star-inserted.active  i",
    )
    _SELECT_YEAR_LOCATOR = (By.CSS_SELECTOR, '[for="application_cycle_year-2"]')
    _SELECT_SEASON_LOCATOR = (By.CSS_SELECTOR, '[for="application_cycle_season-0"]')
    _SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(1) isc-reco-tests > div formly-validation-message",
    )
    _EXAM_LIST_LOCATOR = (By.CSS_SELECTOR, "#high_school_gpa_score")
    _SELECT_GPA_SCORE_LOCATOR = (By.XPATH, "//div[contains(text(),'GPA(4)')]")
    _SELECT_CGPA_SCORE_LOCATOR = (By.XPATH, "//div[contains(text(),'CGPA(10)')]")
    _SELECT_PERCENTAGE_SCORE_LOCATOR = (
        By.XPATH,
        "//div[contains(text(),'Percentage (100)')]",
    )
    # ***************************** Certifications *******************************
    _SELECT_CERTIFICATION_YES_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='taken_certifications-1']",
    )
    _SELECT_PAPER_PUBLICATIONS_YES_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='research_paper_published-1']",
    )
    _SELECT_INTERNSHIP_YES_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='done_internships-1']",
    )
    _SELECT_SEMINAR_YES_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='conducted_seminars-1']",
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
    # ------------------
    _INTERNATIONAL_PAPER_BUTTON = (By.CSS_SELECTOR, "[for ='research_paper_type-0']")
    _NATIONAL_PAPER_BUTTON = (By.CSS_SELECTOR, "[for ='research_paper_type-1']")
    _BOTH_PAPER_BUTTON = (By.CSS_SELECTOR, "[for ='research_paper_type-2']")
    _ONE_PAPER_BUTTON = (By.CSS_SELECTOR, "[for ='research_paper_number-0']")
    _TWO_PAPER_BUTTON = (By.CSS_SELECTOR, "[for ='research_paper_number-1']")
    _THREE_PAPER_BUTTON = (By.CSS_SELECTOR, "[for ='research_paper_number-2']")
    _MORE_THAN_THREE_PAPER_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='research_paper_number-3']",
    )
    # -------------------
    _INTERNATIONAL_SEMINAR_BUTTON = (By.CSS_SELECTOR, "[for ='seminar_type-0']")
    _NATIONAL_SEMINAR_BUTTON = (By.CSS_SELECTOR, "[for ='seminar_type-1']")
    _BOTH_SEMINAR_BUTTON = (By.CSS_SELECTOR, "[for ='seminar_type-2']")
    _ONE_SEMINAR_BUTTON = (By.CSS_SELECTOR, "[for ='seminar_number-0']")
    _TWO_SEMINAR_BUTTON = (By.CSS_SELECTOR, "[for ='seminar_number-1']")
    _THREE_SEMINAR_BUTTON = (By.CSS_SELECTOR, "[for ='seminar_number-2']")
    _MORE_THAN_THREE_SEMINAR_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='seminar_number-3']",
    )

    # -------------------
    _PUBLIC_INTERNSHIP_BUTTON = (By.CSS_SELECTOR, "[for ='internship_type-0']")
    _PRIVATE_INTERNSHIP_BUTTON = (By.CSS_SELECTOR, "[for ='internship_type-1']")
    _BOTH_INTERNSHIP_BUTTON = (By.CSS_SELECTOR, "[for ='internship_type-2']")
    _ONE_INTERNSHIP_BUTTON = (By.CSS_SELECTOR, "[for ='internship_number-0']")
    _TWO_INTERNSHIP_BUTTON = (By.CSS_SELECTOR, "[for ='internship_number-1']")
    _THREE_INTERNSHIP_BUTTON = (By.CSS_SELECTOR, "[for ='internship_number-2']")
    _MORE_THAN_THREE_INTERNSHIP_BUTTON = (
        By.CSS_SELECTOR,
        "[for ='internship_number-4']",
    )
    _ONE_YEAR_WORK_EXPERIENCE_BUTTON = (By.CSS_SELECTOR, "[for ='work_exp_years-1']")
    _TWO_YEAR_WORK_EXPERIENCE_BUTTON = (By.CSS_SELECTOR, "[for ='work_exp_years-2']")
    _THREE_YEAR_WORK_EXPERIENCE_BUTTON = (By.CSS_SELECTOR, "[for ='work_exp_years-3']")
    _FOUR_YEAR_WORK_EXPERIENCE_BUTTON = (By.CSS_SELECTOR, "[for ='work_exp_years-4']")

    # ***************************** Aptitude Test *******************************
    _NO_APTITUDE_TEST = (By.CSS_SELECTOR, "[for ='aptitude_test-0']")
    _SAT_APTITUDE_TEST_BUTTON = (By.CSS_SELECTOR, "[for ='aptitude_test-1']")
    _ACT_APTITUDE_TEST_BUTTON = (By.CSS_SELECTOR, "[for ='aptitude_test-2']")
    _GRE_APTITUDE_TEST_BUTTON = (By.CSS_SELECTOR, "[for='aptitude_test-1']")
    _GMAT_APTITUDE_TEST_BUTTON = (By.CSS_SELECTOR, "[for='aptitude_test-2']")
    _INPUT_SAT_APTITUDE_TEST = (By.CSS_SELECTOR, "[placeholder='400 - 1600']")
    _INPUT_GRE_APTITUDE_TEST = (By.CSS_SELECTOR, "[placeholder='260 - 340']")
    _INPUT_GMAT_APTITUDE_TEST = (By.CSS_SELECTOR, "[placeholder='200 - 800']")
    _INPUT_ACT_APTITUDE_TEST = (By.CSS_SELECTOR, "[placeholder='Out of 36']")
    _SAT_SCORE_ERROR_MESSAGE = (By.CSS_SELECTOR, "formly-field:nth-child(1) > formly-group > formly-field:nth-child("
                                                 "4) > formly-wrapper-animation > div > isc-reco-tests > div > "
                                                 "formly-validation-message",
                                )
    _ACT_SCORE_ERROR_MESSAGE = (By.CSS_SELECTOR, "formly-field:nth-child(1) > formly-group > formly-field:nth-child("
                                                 "5) > formly-wrapper-animation > div > isc-reco-tests > div > "
                                                 "formly-validation-message")
    _GRE_SCORE_ERROR_MESSAGE = (By.XPATH,
                                "//formly-group/formly-field[1]//formly-field["
                                "2]//isc-reco-tests/div/formly-validation-message "
                                )
    _GMAT_SCORE_ERROR_MESSAGE = (By.CSS_SELECTOR,
                                 "formly-group > formly-field:nth-child(1) formly-field:nth-child(3) > "
                                 "formly-wrapper-animation isc-reco-tests > div > formly-validation-message "
                                 )

    # ********************************* English Exam Test *******************
    _NO_ISC_ENGLISH_TEST_LOCATOR = (By.CSS_SELECTOR, "[for='english_test-0']")
    _EXAM_ISC_IELTS_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(2) > formly-group > formly-field:nth-child(2) > formly-wrapper-animation > div > "
        "isc-reco-tests > div > formly-validation-message",
    )
    _EXAM_ISC_TOEFL_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(2) > formly-group > formly-field:nth-child(3) > formly-wrapper-animation > div > "
        "isc-reco-tests > div > formly-validation-message",
    )
    _EXAM_ISC_CAE_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(2) > formly-group > formly-field:nth-child(4) > formly-wrapper-animation > div > "
        "isc-reco-tests > div > formly-validation-message",
    )
    _EXAM_ISC_PTE_SCORE_ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "formly-field:nth-child(2) formly-field:nth-child(5) > formly-wrapper-animation > div > isc-reco-tests > div "
        "formly-validation-message",
    )
    _INPUT_ISC_IELTS_EXAM_SCORE_LOCATOR = (
        By.CSS_SELECTOR,
        "[placeholder='Out of 9']",
    )
    _INPUT_ISC_TOEFL_EXAM_SCORE_LOCATOR = (
        By.CSS_SELECTOR,
        "[placeholder='Out of 120']",
    )
    _INPUT_ISC_CAE_EXAM_SCORE_LOCATOR = (
        By.CSS_SELECTOR,
        "[placeholder='80 - 230']",
    )
    _INPUT_ISC_PTE_EXAM_SCORE_LOCATOR = (
        By.CSS_SELECTOR,
        "[placeholder='10 - 90']",
    )
    _SELECT_ISC_IELTS_BUTTON_LOCATOR = (By.XPATH, "//label[@for='english_test-1']")
    _SELECT_ISC_TOEFL_BUTTON_LOCATOR = (By.XPATH, "//label[@for='english_test-2']")
    _SELECT_ISC_CAE_BUTTON_LOCATOR = (By.XPATH, "//label[@for='english_test-3']")
    _SELECT_ISC_PTE_BUTTON_LOCATOR = (By.XPATH, "//label[@for='english_test-4']")

    GPA = str(random.randint(1, 4))
    select_degree_to_pursue = [
        _BACHELORS_DEGREE_LOCATOR,
    ]
    select_country_to_study = [
        _USA_COUNTRY_LOCATOR,
        _CAN_COUNTRY_LOCATOR,
        _GBR_COUNTRY_LOCATOR,
        _AUS_COUNTRY_LOCATOR,
    ]
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
    select_published_paper = [
        _INTERNATIONAL_PAPER_BUTTON,
        _NATIONAL_PAPER_BUTTON,
        _BOTH_PAPER_BUTTON,
    ]
    select_number_of_paper_published = [
        _ONE_PAPER_BUTTON,
        _TWO_PAPER_BUTTON,
        _THREE_PAPER_BUTTON,
        _MORE_THAN_THREE_PAPER_BUTTON,
    ]
    select_seminar = [
        _INTERNATIONAL_SEMINAR_BUTTON,
        _NATIONAL_SEMINAR_BUTTON,
        _BOTH_SEMINAR_BUTTON,
    ]
    select_number_of_seminar_published = [
        _ONE_SEMINAR_BUTTON,
        _TWO_SEMINAR_BUTTON,
        _THREE_SEMINAR_BUTTON,
        _MORE_THAN_THREE_SEMINAR_BUTTON,
    ]
    select_internship = [
        _PUBLIC_INTERNSHIP_BUTTON,
        _PRIVATE_INTERNSHIP_BUTTON,
        _BOTH_INTERNSHIP_BUTTON,
    ]
    select_number_of_internship = [
        _ONE_INTERNSHIP_BUTTON,
        _TWO_INTERNSHIP_BUTTON,
    ]

    select_work_experience = [
        _ONE_YEAR_WORK_EXPERIENCE_BUTTON,
        _TWO_YEAR_WORK_EXPERIENCE_BUTTON,
        _THREE_YEAR_WORK_EXPERIENCE_BUTTON,
        _FOUR_YEAR_WORK_EXPERIENCE_BUTTON
    ]

    def click_on_generate_recommendations(self):
        time.sleep(2)
        return self.click_on_element(self._GENERATE_RECOMMENDATION)

    def click_on_country_of_study(self):
        time.sleep(3)
        res1 = self.click_on_element(self._CAN_COUNTRY_LOCATOR)
        res2 = self.click_on_element(self._USA_COUNTRY_LOCATOR)
        return res1 and res2

    def isc_enter_input_in_preferred_specialization(self, specialization):
        return self.enter_field_input(
            self._SPECIALIZATION_INPUT_LOCATOR, specialization
        )

    def isc_enter_computer_science_specialization(self, specialization):
        self.scroll_into_view(self._SPECIALIZATION_INPUT_LOCATOR)
        res1 = self.isc_enter_input_in_preferred_specialization(specialization)
        time.sleep(2)
        res2 = self.click_on_element(self._SELECT_CS_SPECIALIZATION_DROP_DOWN_LOCATOR)
        return res1 and res2

    def isc_enter_agriculture_engineering_specialization(self, specialization):
        self.scroll_into_view(self._SPECIALIZATION_INPUT_LOCATOR)
        res1 = self.isc_enter_input_in_preferred_specialization(specialization)
        time.sleep(2)
        res2 = self.click_on_element(self._SELECT_AGRICULTURE_ENGINEERING_SPECIALIZATION_DROP_DOWN_LOCATOR)
        return res1 and res2

    def isc_enter_agriculture_science_specialization(self, specialization):
        time.sleep(2)
        res1 = self.isc_enter_input_in_preferred_specialization(specialization)
        time.sleep(2)
        res2 = self.click_on_element(self._SELECT_AGRICULTURE_SCIENCE_SPECIALIZATION_DROP_DOWN_LOCATOR)
        return res1 and res2

    def kaplan_enter_input_in_preferred_specialization(self, specialization):
        return self.enter_field_input(
            self._KAPLAN_SPECIALIZATION_INPUT_LOCATOR, specialization
        )

    def kaplan_enter_computer_science_specialization(self, specialization):
        self.scroll_into_view(self._KAPLAN_SPECIALIZATION_INPUT_LOCATOR)
        res1 = self.kaplan_enter_input_in_preferred_specialization(specialization)
        time.sleep(2)
        res2 = self.click_on_element(self._SELECT_CS_SPECIALIZATION_DROP_DOWN_LOCATOR)
        return res1 and res2

    def click_on_canada(self):
        return self.click_on_element(self._CAN_COUNTRY_LOCATOR)

    def click_on_usa(self):
        return self.click_on_element(self._USA_COUNTRY_LOCATOR)

    def select_master_degree(self):
        return self.click_on_element(self._MASTER_DEGREE_LOCATOR)

    def select_bachelors_degree(self):
        return self.click_on_element(self._BACHELORS_DEGREE_LOCATOR)

    def select_doctorate_degree(self):
        return self.click_on_element(self._DOCTORATE_DEGREE_LOCATOR)

    def select_associate_degree(self):
        return self.click_on_element(self._ASSOCIATE_DEGREE_LOCATOR)

    def select_diploma_degree(self):
        return self.click_on_element(self._DIPLOMA_DEGREE_LOCATOR)

    def select_under_grad_degree(self):
        return self.click_on_element(self._UNDERGRADUATE_DEGREE_LOCATOR)

    def select_grad_degree(self):
        return self.click_on_element(self._GRADUATE_DEGREE_LOCATOR)

    def select_PGA_degree(self):
        return self.click_on_element(self._PGA_DEGREE_LOCATOR)

    def select_your_preferred_specialization(self, spec):
        return self.enter_field_input(self._SPECIALIZATION_INPUT_LOCATOR, spec)

    def select_your_preferred_sub_discipline(self, spec):
        return self.enter_field_input(self._SUB_DISCIPLINES_INPUT_LOCATOR, spec)

    def enter_high_school_score(self, score):
        return self.enter_field_input(self._BACHELORS_HIGH_SCHOOL_SCORE, score)

    def select_english_proficiency_indicator(self):
        return self.click_on_element(self._ENGLISH_TEST_SCORE_LOCATOR)

    def click_on_submit(self):
        return self.click_on_element(self._SUBMIT_BUTTON_LOCATOR)

    def enter_input_in_budget_field(self, budget):
        return self.enter_field_input(self._BUDGET_INPUT_LOCATOR, budget)

    def click_on_budget_field(self, budget):
        self.scroll_into_view(self._SUBMIT_BUTTON_LOCATOR)
        res = self.enter_input_in_budget_field(budget)
        return res

    def check_budget_error_message(self):
        error_message = self.get_text_of_elements(self._BUDGET_ERROR_MSG)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.BUDGET_FIELD_VALIDATION

    def click_on_next_button(self):
        return self.click_on_element(self._NEXT_PAGE_LOCATOR)

    def INPUT_ISC_BACHELORS_HIGH_SCHOOL_SCORE(self, mark):
        return self.enter_field_input(self.INPUT_ISC_BACHELORS_HIGH_SCHOOL_SCORE, mark)

    def check_invalid_email_error_message(self):
        invalid_email = self.get_text_of_elements(self._INVALID_EMAIL_ERROR_LOCATOR)
        res1 = self.convert_list_to_string(invalid_email) == constants.INVALID_EMAIL
        print(res1)
        return res1

    def check_multiple_option_enable_for_country(self):
        return self.check_page_element(self._COUNTRY_ENABLE_BUTTON)

    def check_option_enable_for_degree(self):
        return self.check_page_element(self._DEGREE_ENABLE_BUTTON)

    def click_on_year(self):
        return self.click_on_element(self._SELECT_YEAR_LOCATOR)

    def click_on_season(self):
        return self.click_on_element(self._SELECT_SEASON_LOCATOR)

    def get_error_message_for_gpa(self):
        error_message = self.get_text_of_elements(self._SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.GPA_EXAM_ERROR_MESSAGE

    def click_on_gpa_and_validate(self, mark):
        self.enter_field_input(self._BACHELORS_HIGH_SCHOOL_SCORE, mark)
        return self.get_error_message_for_gpa()

    def get_error_message_for_cgpa(self):
        error_message = self.get_text_of_elements(self._SCORE_ERROR_MESSAGE)
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
        error_message = self.get_text_of_elements(self._SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.HIGH_SCHOOL_PERCENTAGE_ERROR_MESSAGE

    def click_on_percentage_high_school_score(self):
        time.sleep(2)
        self.click_on_exam_drop_down()
        self.click_on_element(self._SELECT_PERCENTAGE_SCORE_LOCATOR)
        return self.get_error_message_for_high_school()

    def click_on_isc_high_school_Score(self, mark):
        self.scroll_into_view(self._BACHELORS_HIGH_SCHOOL_SCORE)
        self.click_on_exam_drop_down()
        self.click_on_element(self._SELECT_GPA_SCORE_LOCATOR)
        return self.enter_field_input(self._BACHELORS_HIGH_SCHOOL_SCORE, mark)

    def click_on_isc_undergrad_Score(self, mark):
        self.scroll_into_view(self._UNDERGRAD_SCHOOL_INPUT_LOCATOR)
        return self.enter_field_input(self._UNDERGRAD_SCHOOL_INPUT_LOCATOR, mark)

    def click_on_certification_yes_button(self):
        return self.click_on_element(self._SELECT_CERTIFICATION_YES_BUTTON)

    def select_random_certification(self):
        return self.click_on_element(random.choice(self.select_isc_certifications))

    def select_random_number_of_certifications(self):
        return self.click_on_element(random.choice(self.select_number_of_certifications))

    def click_on_certifications(self):
        res1 = self.click_on_certification_yes_button()
        res2 = self.select_random_certification()
        res3 = self.select_random_number_of_certifications()
        time.sleep(2)
        return res1 and res2 and res3

    def click_on_paper_publications_yes_button(self):
        self.scroll_into_view(self._SELECT_PAPER_PUBLICATIONS_YES_BUTTON)
        return self.click_on_element(self._SELECT_PAPER_PUBLICATIONS_YES_BUTTON)

    def select_random_paper_publications(self):
        return self.click_on_element(random.choice(self.select_published_paper))

    def select_random_number_of_paper_publications(self):
        return self.click_on_element(random.choice(self.select_number_of_paper_published))

    def click_on_paper_publications(self):
        res1 = self.click_on_paper_publications_yes_button()
        res2 = self.select_random_paper_publications()
        res3 = self.select_random_number_of_paper_publications()
        time.sleep(2)
        return res1 and res2 and res3

    def click_on_seminar_yes_button(self):
        self.scroll_into_view(self._SELECT_SEMINAR_YES_BUTTON)
        return self.click_on_element(self._SELECT_SEMINAR_YES_BUTTON)

    def select_random_seminar(self):
        return self.click_on_element(random.choice(self.select_seminar))

    def select_random_number_of_seminars(self):
        return self.click_on_element(random.choice(self.select_number_of_seminar_published))

    def click_on_seminar(self):
        res1 = self.click_on_seminar_yes_button()
        res2 = self.select_random_seminar()
        res3 = self.select_random_number_of_seminars()
        time.sleep(2)
        return res1 and res2 and res3

    def click_on_internship_yes_button(self):
        self.scroll_into_view(self._SELECT_INTERNSHIP_YES_BUTTON)
        return self.click_on_element(self._SELECT_INTERNSHIP_YES_BUTTON)

    def select_random_internship(self):
        return self.click_on_element(random.choice(self.select_internship))

    def select_random_number_of_internships(self):
        return self.click_on_element(random.choice(self.select_number_of_internship))

    def click_on_internship(self):
        res1 = self.click_on_internship_yes_button()
        res2 = self.select_random_internship()
        res3 = self.select_random_number_of_internships()
        time.sleep(2)
        return res1 and res2 and res3

    def click_on_work_experience(self):
        res = self.click_on_element(random.choice(self.select_work_experience))
        time.sleep(2)
        return res

    def get_sat_aptitude_test_error_message(self):
        error_message = self.get_text_of_elements(self._SAT_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return (
                self.convert_list_to_string(error_message) == constants.SAT_APTITUDE_TEST_ERROR_MESSAGE
        )

    def click_on_sat_aptitude_test_and_validate(self, mark):
        self.click_on_element(self._SAT_APTITUDE_TEST_BUTTON)
        time.sleep(2)
        self.enter_field_input(self._INPUT_SAT_APTITUDE_TEST, mark)
        return self.get_sat_aptitude_test_error_message()

    def get_gre_aptitude_test_error_message(self):
        error_message = self.get_text_of_elements(self._GRE_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.GRE_APTITUDE_TEST_ERROR_MESSAGE

    def click_on_gre_aptitude_test_button(self):
        self.scroll_into_view(self._GRE_APTITUDE_TEST_BUTTON)
        return self.click_on_element(self._GRE_APTITUDE_TEST_BUTTON)

    def click_on_gre_aptitude_test_and_validate(self, mark):
        self.click_on_gre_aptitude_test_button()
        time.sleep(2)
        self.enter_field_input(self._INPUT_GRE_APTITUDE_TEST, mark)
        return self.get_gre_aptitude_test_error_message()

    def click_on_gmat_aptitude_test(self, ):
        self.scroll_into_view(self._GMAT_APTITUDE_TEST_BUTTON)
        return self.click_on_element(self._GMAT_APTITUDE_TEST_BUTTON)

    def get_gmat_aptitude_test_error_message(self):
        a = self.get_text_of_elements(self._GMAT_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(a))
        return (
                self.convert_list_to_string(a) == constants.GMAT_APTITUDE_TEST_ERROR_MESSAGE
        )

    def click_on_gmat_aptitude_test_and_validate(self, mark):
        self.click_on_gmat_aptitude_test()
        time.sleep(2)
        self.enter_field_input(self._INPUT_GMAT_APTITUDE_TEST, mark)
        return self.get_gmat_aptitude_test_error_message()

    def get_act_aptitude_test_error_message(self):
        error_message = self.get_text_of_elements(self._ACT_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.ACT_APTITUDE_TEST_ERROR_MESSAGE

    def click_on_act_aptitude_test(self, ):
        return self.click_on_element(self._ACT_APTITUDE_TEST_BUTTON)

    def click_on_act_aptitude_test_and_validate(self, mark):
        self.click_on_act_aptitude_test()
        time.sleep(2)
        self.enter_field_input(self._INPUT_ACT_APTITUDE_TEST, mark)
        return self.get_act_aptitude_test_error_message()

    def click_on_no_aptitude_test(self):
        time.sleep(2)
        return self.click_on_element(self._NO_APTITUDE_TEST)

    def get_isc_ielts_exam_error_message(self):
        error_message = self.get_text_of_elements(self._EXAM_ISC_IELTS_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.IELTS_EXAM_ERROR_MESSAGE

    def click_on_isc_ielts_exam_button(self):
        return self.click_on_element(self._SELECT_ISC_IELTS_BUTTON_LOCATOR)

    def click_on_isc_ielts_exam(self, mark):
        time.sleep(2)
        self.click_on_isc_ielts_exam_button()
        self.enter_field_input(self._INPUT_ISC_IELTS_EXAM_SCORE_LOCATOR, mark)
        return self.get_isc_ielts_exam_error_message()

    def get_isc_toefl_exam_error_message(self):
        a = self.get_text_of_elements(self._EXAM_ISC_TOEFL_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(a))
        return (
                self.convert_list_to_string(a) == constants.TOEFL_EXAM_ERROR_MESSAGE
        )

    def click_on_isc_toefl_exam_button(self):
        return self.click_on_element(self._SELECT_ISC_TOEFL_BUTTON_LOCATOR)

    def click_on_isc_toefl_exam(self, mark):
        time.sleep(1)
        self.click_on_isc_toefl_exam_button()
        self.enter_field_input(self._INPUT_ISC_TOEFL_EXAM_SCORE_LOCATOR, mark)
        return self.get_isc_toefl_exam_error_message()

    def get_isc_cae_exam_error_message(self):
        a = self.get_text_of_elements(self._EXAM_ISC_CAE_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(a))
        return (
                self.convert_list_to_string(a) == constants.CAE_EXAM_ERROR_MESSAGE
        )

    def click_on_isc_cae_exam_button(self):
        return self.click_on_element(self._SELECT_ISC_CAE_BUTTON_LOCATOR)

    def click_on_isc_cae_exam(self, mark):
        time.sleep(1)
        self.click_on_isc_cae_exam_button()
        self.enter_field_input(self._INPUT_ISC_CAE_EXAM_SCORE_LOCATOR, mark)
        return self.get_isc_cae_exam_error_message()

    def get_isc_pit_exam_error_message(self):
        error_message = self.get_text_of_elements(self._EXAM_ISC_PTE_SCORE_ERROR_MESSAGE)
        print(self.convert_list_to_string(error_message))
        return self.convert_list_to_string(error_message) == constants.PIT_EXAM_ERROR_MESSAGE

    def click_on_isc_pit_exam_button(self):
        return self.click_on_element(self._SELECT_ISC_PTE_BUTTON_LOCATOR)

    def click_on_isc_pit_exam(self, mark):
        time.sleep(1)
        self.click_on_isc_pit_exam_button()
        self.enter_field_input(self._INPUT_ISC_PTE_EXAM_SCORE_LOCATOR, mark)
        return self.get_isc_pit_exam_error_message()

    def click_on_no_exam(self):
        time.sleep(2)
        return self.click_on_element(self._NO_ISC_ENGLISH_TEST_LOCATOR)

    def click_on_submit_button(self):
        return self.click_on_element(self._SUBMIT_BUTTON_LOCATOR)
import os
import random
import time

from selenium.webdriver.common.by import By

import constants
from pages.base_page import BasePage


class ManageStudentProfilePage(BasePage):
    PATH = os.environ.get("")
    _PROFILE_TAB_LOCATOR = (
        By.CSS_SELECTOR,
        '.navbar-inner-wrapper-for-scroll [href="/dashboard/profile"]',
    )
    # ****************************  About  ******************************
    _ABOUT_LOCATOR = (By.XPATH, "//div[contains(text(),'About')]")
    _FIRST_NAME_FIELD_LOCATOR = (
        By.ID,
        "student_profile_about_section__first_name_field",
    )
    _LAST_NAME_FIELD_LOCATOR = (By.ID, "student_profile_about_section__last_name_field")
    _EMAIL_ADDRESS_FIELD_LOCATOR = (By.ID, "student_profile_about_section__email_field")
    _NUMBER_FIELD_LOCATOR = (By.CSS_SELECTOR, "[id='phone']")
    _GENDER_LOCATOR = (By.ID, "student_profile_about_section__gender_field")
    _GENDER_LIST_LOCATOR = (
        By.CSS_SELECTOR,
        "[aria-label='Options list'] [role='option']",
    )
    _MALE_GENDER_LOCATOR = (
        By.CSS_SELECTOR,
        "[aria-label='Options list'] [role='option'] [title='Male']",
    )
    _FEMALE_GENDER_LOCATOR = (
        By.CSS_SELECTOR,
        "[aria-label='Options list'] [role='option'] [title='Female']",
    )
    _OTHERS_GENDER_LOCATOR = (
        By.CSS_SELECTOR,
        "[aria-label='Options list'] [role='option'] [title='Others']",
    )
    _ADDRESS_FIELD_LOCATOR = (By.ID, "student_profile_about_section__address_field")
    _STATE_FIELD_LOCATOR = (By.ID, "student_profile_about_section__state_field")
    _DATE_OF_BIRTH_LOCATOR = (By.ID, "student_profile_about_section__dob_field")
    _NATIONALITY_FIELD_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_about_section__nationality_field [type='text']",
    )
    _NATIONALITY_LOCATOR = (By.CSS_SELECTOR, "[role='option']")
    _CITY_FIELD_LOCATOR = (By.ID, "student_profile_about_section__city_field")
    _ZIP_CODE_FIELD_LOCATOR = (By.ID, "student_profile_about_section__zipcode_field")
    _COUNTRY_FIELD_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_about_section__country_field [type='text']",
    )
    _COUNTRY_LOCATOR = (By.CSS_SELECTOR, "[role='option']")
    _SAVE_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(),'Save')]")
    _YEAR_DROP_DOWN_LOCATOR = (
        By.CSS_SELECTOR,
        "div.owl-dt-calendar-control div button",
    )
    _LEFT_ARROW_YEAR_LOCATOR = (
        By.CSS_SELECTOR,
        "owl-date-time-multi-year-view button:nth-child(1)",
    )
    _SELECT_YEAR_LOCATOR = (By.CSS_SELECTOR, "td.owl-dt-calendar-cell.owl-dt-year-2002")
    _SELECT_WRONG_YEAR_LOCATOR = (
        By.CSS_SELECTOR,
        "td.owl-dt-calendar-cell.owl-dt-year-2015",
    )
    _SELECT_MONTH_LOCATOR = (By.XPATH, "//span[contains(text(),'Nov')]")
    _SELECT_DATE_LOCATOR = (
        By.CSS_SELECTOR,
        "owl-date-time-month-view tr:nth-child(3) td.owl-dt-calendar-cell.owl-dt-day-5.ng-star-inserted",
    )
    _VERIFY_NAME_TEXT = (
        By.CSS_SELECTOR,
        "[class='break-all md:break-words text-h5 leading-h5 font-semibold text-gray-header']",
    )
    _VERIFY_GENDER_TEXT = (
        By.ID,
        "student_profile_about_section__gender_field",
    )
    # _VERIFY_DOB_TEXT = (By.CSS_SELECTOR, )
    _VERIFY_NATIONALITY_TEXT = (
        By.CSS_SELECTOR,
        "[class='break-all md:break-words text-md leading-md text-gray']",
    )
    _VERIFY_COUNTRY_TEXT = (
        By.CSS_SELECTOR,
        "[class='break-all md:break-words text-md leading-md text-gray']",
    )
    _VERIFY_PROFILE_COMPLETION = (
        By.CSS_SELECTOR,
        "[class='text-sm leading-sm font-semibold']",
    )
    _FIRST_NAME_ERROR_MSG = (
        By.XPATH,
        "//*[contains(text(),'First Name cannot be empty')]",
    )
    _LAST_NAME_ERROR_MSG = (
        By.XPATH,
        "//*[contains(text(),'Last Name cannot be empty')]",
    )
    _NUMBER_ERROR_MSG = (By.XPATH, "//*[contains(text(),'Phone number is invalid')]")
    _STATE_ERROR_MSG = (By.XPATH, "//*[contains(text(),'State cannot be empty')]")
    _CITY_ERROR_MSG = (
        By.XPATH,
        "//*[contains(text(),'City/Town/Village cannot be empty')]",
    )
    _STREET_ERROR_MSG = (
        By.XPATH,
        "//*[contains(text(),'Street Address cannot be empty')]",
    )
    _ZIPCODE_ERROR_MSG = (By.XPATH, "//*[contains(text(),'Zipcode cannot be empty')]")
    _CALENDER_ERROR_MSG = (
        By.XPATH,
        "//*[contains(text(),'Age should be at least 10 years')]",
    )
    # ****************************  Education  ******************************
    _MENU_OPTION_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="mat-menu-trigger ' 'saved_details__options_trigger ng-star-inserted"]',
    )
    _EDIT_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(),' Edit ')]")
    _DELETE_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(),' Delete ')]")
    # _DELETE_BUTTON_LOCATOR = (By.XPATH, "#mat-menu-panel-1 > div > span:nth-child(2)")
    _EDUCATION_LOCATOR = (By.XPATH, "//div[contains(text(),'Education')]")
    _ADD_SCHOOL_LOCATOR = (By.XPATH, "//span[contains(text(),'Add School')]")
    _INSTITUTION_NAME_LOCATOR = (
        By.ID,
        "student_profile_education_section__institute_name_field",
    )
    _DEGREE_LOCATOR = (
        By.CSS_SELECTOR,
        '#student_profile_education_section__degree_field [type="text"]',
    )
    _DROPDOWN_LOCATOR = (By.CSS_SELECTOR, '[role="listbox"]')
    _FIELD_OF_STUDY_LOCATOR = (
        By.CSS_SELECTOR,
        '#student_profile_education_section__field_of_study_field [type="text"]',
    )
    _SCORE_INPUT_LOCATOR = (
        By.ID,
        "student_profile_education_section__total_score_field",
    )
    _TYPE_OF_SCORE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_education_section__max_score_field",
    )
    _SELECT_GPA_SCORE = (By.CSS_SELECTOR, '[title="GPA(4)"]')
    _SELECT_CGPA_SCORE = (By.CSS_SELECTOR, '[title="CGPA(10)"]')
    _SELECT_PERCENTAGE_SCORE = (By.CSS_SELECTOR, '[title="Percentage (100)"]')
    _EDU_START_DATE_LOCATOR = (
        By.ID,
        "student_profile_education_section__start_date_field",
    )
    _EDU_END_DATE_LOCATOR = (By.ID, "student_profile_education_section__end_date_field")
    _VERIFY_INSTITUTE_NAME = (
        By.CSS_SELECTOR,
        '[class="composite-row row-1 ng-star-inserted"]',
    )
    _VERIFY_DEGREE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_education_section_0 > "
        "section > div > div.composite-row.row-2.ng-star-inserted > span:nth-child(1) > span",
    )
    _VERIFY_FIELD_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_education_section_0 > "
        "section > div > div.composite-row.row-2.ng-star-inserted > span:nth-child(2) > span",
    )
    _VERIFY_SCORE = (
        By.CSS_SELECTOR,
        '[class="student_profile_education_section_scores'
        ' row-separator ng-star-inserted"]',
    )

    _VERIFY_DATE = (
        By.CSS_SELECTOR,
        '[class="composite-row row-3 ng-star-inserted"] span.ng-star-inserted',
    )
    # _CLICK_ON_SAVE_BUTTON = (By.XPATH, "//span[contains(text(),'Save')]")      Require save button

    # ****************************  Experience  ******************************
    _EXPERIENCE_LOCATOR = (By.XPATH, "//div[contains(text(),'Experience')]")
    _ADD_EXPERIENCE_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'Add Experience')]",
    )
    _COMPANY_NAME_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        "[id='student_profile_experience_section__company_field']",
    )
    _CITY_NAME_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        "[id='student_profile_experience_section__city_field']",
    )
    _COUNTRY_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_experience_section__country_field input",
    )
    _COUNTRY_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, '[role="option"]')
    _TITLE_LOCATOR = (
        By.CSS_SELECTOR,
        "[id='student_profile_experience_section__title_field']",
    )
    _EMPLOYEE_TYPE_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_experience_section__employment_type_field input",
    )
    _EMPLOYEE_TYPE_LOCATOR = (
        By.XPATH,
        "//formly-field[2]/isc-reco-typeahead[1]/div[1]/ng-select[1]/div["
        "1]/div[1]/div[2]/input[1]",
    )
    _EMPLOYEE_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, '[role="option"]')
    _INDUSTRY_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        '#student_profile_experience_section__industry_field [type="text"]',
    )
    _INDUSTRY_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, '[role="option"]')
    _WORKING_HERE_CHECKBOX_LOCATOR = (
        By.CSS_SELECTOR,
        "student_profile_experience_section__currently_working_here_field - input",
    )
    # _CLICK_ON_SAVE_BUTTON = (By.XPATH, "//span[contains(text(),'Save')]")      Require save button
    _VERIFY_EXPERIENCE_COMPANY_NAME_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="composite-row row-2 ng-star-inserted"] '
        '[class= "student_profile_experience_section_default_data ng-star-inserted"]',
    )
    _VERIFY_EXPERIENCE_TITLE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="composite-row row-1 ng-star-inserted"] '
        '[class= "student_profile_experience_section_default_data ng-star-inserted"]',
    )
    _VERIFY_CITY_AND_COUNTRY_LOCATOR = (
        By.CSS_SELECTOR,
        '[class= "student_profile_experience_section_location |'
        ' composite_field__item_location row-separator ng-star-inserted"]',
    )
    _VERIFY_EMPLOYMENT_TYPE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="composite-row row-3 ng-star-inserted"] '
        '[class= "student_profile_experience_section_default_data ng-star-inserted"]',
    )
    _VERIFY_INDUSTRY_LOCATOR = (
        By.CSS_SELECTOR,
        '[class= "student_profile_experience_'
        'section_default_data row-separator ng-star-inserted"]',
    )
    _VERIFY_START_AND_END_DATE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class= "composite_field__item_duration '
        'student_profile_experience_section_duration ng-star-inserted"]',
    )
    _START_DATE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_experience_section__start_date_field",
    )
    _EXP_START_YEAR = (By.CSS_SELECTOR, '[aria-label="2019"]')
    _EXP_START_MONTH = (By.CSS_SELECTOR, '[aria-label="February 2019"]')
    _EXP_INCORRECT_START_YEAR = (By.CSS_SELECTOR, '[aria-label="2022"]')
    _EXP_INCORRECT_START_MONTH = (By.CSS_SELECTOR, '[aria-label="February 2012"]')
    _END_DATE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_experience_section__end_date_field",
    )
    _EXP_END_YEAR = (By.CSS_SELECTOR, '[aria-label="2021"]')
    _EXP_END_MONTH = (By.CSS_SELECTOR, '[aria-label="July 2021"]')
    _EXP_INCORRECT_END_YEAR = (By.CSS_SELECTOR, '[aria-label="2026"]')
    _EXP_INCORRECT_END_MONTH = (By.CSS_SELECTOR, '[aria-label="July 2026"]')
    _START_DATE_ERROR_MSG_LOCATOR = (
        By.CSS_SELECTOR,
        'formly-validation-message[class="ng-tns-c238-40"]',
    )
    _END_DATE_ERROR_MSG_LOCATOR = (
        By.CSS_SELECTOR,
        'formly-validation-message[class="ng-tns-c238-41"]',
    )
    # ****************************  Test score  ******************************
    _TEST_SCORES_LOCATOR = (By.XPATH, "//div[contains(text(),'Test Scores')]")
    _ADD_TEST_SCORE_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'Add Test Score')]",
    )
    _EXAM_TYPE_DROPDOWN_LOCATOR = (
        By.ID,
        "student_profile_test_scores_section__exam_type_field",
    )
    _ENGLISH_PROFICIENCY_DROPDOWN_LOCATOR = (
        By.CSS_SELECTOR,
        '[title="English Proficiency"]',
    )
    _ENTRANCE_EXAM_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, '[title="Entrance exam"]')
    _ENTRANCE_EXAM_TYPE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_test_scores_section__entrance_exam_type_field",
    )
    _GRE_EXAM_TYPE_LOCATOR = (By.CSS_SELECTOR, '[title="GRE"]')
    _ANALYTICAL_EXAM_INPUT_LOCATOR = (
        By.ID,
        "student_profile_test_scores_section__awa_field",
    )
    _QUANTITATIVE_REASONING_EXAM_INPUT_LOCATOR = (
        By.ID,
        "student_profile_test_scores_section__quant_field",
    )
    _VERBAL_REASONING_EXAM_INPUT_LOCATOR = (
        By.ID,
        "student_profile_test_scores_section__verbal_field",
    )

    _SAT_EXAM_TYPE_LOCATOR = (By.CSS_SELECTOR, '[title="SAT"]')
    _ACT_EXAM_TYPE_LOCATOR = (By.CSS_SELECTOR, '[title="ACT"]')
    _GMAT_EXAM_TYPE_LOCATOR = (By.CSS_SELECTOR, '[title="GMAT"]')
    _ENGLISH_EXAM_TYPE_DROPDOWN_LOCATOR = (
        By.ID,
        "student_profile_test_scores_section__entrance_exam_type_field",
    )
    _REVISED_TOEFL_PAPER_DELIVERED_TEST_LOCATOR = (
        By.CSS_SELECTOR,
        '[title="Revised TOEFL paper-delivered test"]',
    )
    _TOEFL_IBT_LOCATOR = (By.CSS_SELECTOR, '[title="TOEFL iBT"]')
    _IELTS_ACADEMIC_LOCATOR = (By.CSS_SELECTOR, '[title="IELTS Academic"]')
    _IELTS_GENERAL_TRAINING_LOCATOR = (
        By.CSS_SELECTOR,
        '[title="IELTS General Training"]',
    )
    _PERSON_PTE_LOCATOR = (By.CSS_SELECTOR, '[title="Pearson PTE"]')
    _CAMBRIDGE_ENGLISH_LOCATOR = (By.CSS_SELECTOR, '[title="Cambridge English"]')
    _KAPLAN_ENGLISH_LOCATOR = (By.CSS_SELECTOR, '[title="Kaplan English"]')
    _DATEPICKER_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_test_scores_section__exam_date_field",
    )
    _SELECT_TEST_MONTH_LOCATOR = (By.CSS_SELECTOR, '[aria-label="Previous month"]')
    _SELECT_TEST_DATE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="owl-dt-calendar-cell-content"]',
    )
    _LISTENING_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        '[id="student_profile_test_scores_section__listening_field"]',
    )
    _READING_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        '[id="student_profile_test_scores_section__reading_field"]',
    )
    _WRITING_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        '[id="student_profile_test_scores_section__writing_field"]',
    )
    _SELECT_DATE_LOCATOR2 = (By.CSS_SELECTOR, '[aria-label="June 8, 2021"]')

    _CANCEL_BUTTON_LOCATOR = (By.CSS_SELECTOR, "//span[contains(text(),'Cancel')]")
    _TOTAL_INPUT_LOCATOR = (
        By.ID,
        "student_profile_test_scores_section__total_score_field",
    )
    _VERIFY_EXAM_TYPE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="composite-row row-1 ng-star-inserted"]'
        ' [class = "student_profile_test_scores_section_default_data ng-star-inserted"]',
    )
    _VERIFY_SUB_EXAM_TYPE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="composite-row row-2 ng-star-inserted"]'
        ' [class = "student_profile_test_scores_section_default_data ng-star-inserted"]',
    )
    _VERIFY_LISTENING_EXAM_SCORE_TYPE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_test_scores_section_0 > section >"
        " div > div.composite-row.row-3.ng-star-inserted > span > div > span:nth-child(1)",
    )
    _VERIFY_READING_EXAM_SCORE_TYPE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_test_scores_section_0 > section > "
        "div > div.composite-row.row-3.ng-star-inserted > span > div > span:nth-child(4)",
    )
    _VERIFY_WRITING_EXAM_SCORE_TYPE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_test_scores_section_0 > section > div > "
        "div.composite-row.row-3.ng-star-inserted > span > div > span:nth-child(7)",
    )
    _VERIFY_LISTENING_EXAM_SCORE_VALUE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_test_scores_section_0 > section >"
        " div > div.composite-row.row-3.ng-star-inserted > span > div > span:nth-child(2)",
    )
    _VERIFY_READING_EXAM_SCORE_VALUE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_test_scores_section_0 > section > "
        "div > div.composite-row.row-3.ng-star-inserted > span > div > span:nth-child(5)",
    )
    _VERIFY_WRITING_EXAM_SCORE_VALUE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_test_scores_section_0 > "
        "section > div > div.composite-row.row-3.ng-star-inserted > span > div > span:nth-child(8)",
    )
    _VERIFY_SINGLE_EXAM_SCORE_VALUE_LOCATOR = (
        By.CSS_SELECTOR,
        "#student_profile_test_scores_section_0 > section > div > "
        "div.composite-row.row-3.ng-star-inserted > span > div > span.score_value.ng-star-inserted",
    )

    _SINGLE_ERROR_MSG_LOCATOR = (
        By.CSS_SELECTOR,
        'formly-validation-message[class="ng-tns-c237-26"]',
    )
    _PEN_MARK = (
        By.CSS_SELECTOR,
        "[class='bg-white rounded-full edit-circle cursor-pointer']",
    )
    Nationality = ["Albanian", "Iranian", "Afghan", "Chadian"]
    enter_nationality = random.choice(Nationality)
    Country = ["China", "Mexico", "Belgium", "India", "France"]
    enter_country = random.choice(Country)

    @property
    def check_page_url(self):
        return self.check_for_new_url(os.environ.get("STUDENT_PROFILE_URL"))

    @property
    def check_exp_page_url(self):
        return self.check_for_new_url(
            "https://student-dashboard-release."
            "ischoolconnect.com/dashboard/profile#experience"
        )

    @property
    def check_test_page_url(self):
        return self.check_for_new_url(
            "https://student-dashboard-release."
            "ischoolconnect.com/dashboard/profile#tests"
        )

    @property
    def click_on_profile_tab(self):
        return self.click_on_element(self._PROFILE_TAB_LOCATOR)

    @property
    def check_education_page_url(self):
        return self.check_for_new_url(
            "https://student-dashboard-release."
            "ischoolconnect.com/dashboard/profile#education"
        )

    @property
    def click_on_education_tab(self):
        return self.click_on_element(self._EDUCATION_LOCATOR)

    @property
    def click_on_about_button(self):
        return self.click_on_element(self._ABOUT_LOCATOR)

    def input_name_field(self, name):
        return self.enter_field_input(self._FIRST_NAME_FIELD_LOCATOR, name)

    def input_lastname_field(self, lastname):
        return self.enter_field_input(self._LAST_NAME_FIELD_LOCATOR, lastname)

    def input_email_field(self, email):
        return self.enter_field_input(self._EMAIL_ADDRESS_FIELD_LOCATOR, email)

    def input_number_field(self, number):
        return self.enter_field_input(self._NUMBER_FIELD_LOCATOR, number)

    @property
    def input_gender_field(self):
        res = self.scroll_into_view(self._GENDER_LOCATOR)
        res1 = self.click_on_element(self._GENDER_LOCATOR)
        res2 = self.click_on_element(self._MALE_GENDER_LOCATOR)
        return res, res1, res2

    @property
    def click_on_female_gender(self):
        return self.click_on_element(self._FEMALE_GENDER_LOCATOR)

    @property
    def input_date_of_birth_field(self):
        self.click_on_element(self._DATE_OF_BIRTH_LOCATOR)
        self.click_on_element(self._YEAR_DROP_DOWN_LOCATOR)
        time.sleep(1)
        self.click_on_element(self._LEFT_ARROW_YEAR_LOCATOR)
        self.click_on_element(self._SELECT_YEAR_LOCATOR)
        time.sleep(1)
        self.click_on_element(self._SELECT_MONTH_LOCATOR)
        time.sleep(1)
        self.click_on_element(self._SELECT_DATE_LOCATOR)
        return True

    def input_address_field(self, address):
        return self.enter_field_input(self._ADDRESS_FIELD_LOCATOR, address)

    def input_state_field(self, state):
        return self.enter_field_input(self._STATE_FIELD_LOCATOR, state)

    @property
    def input_nationality_field(self):
        res = self.enter_field_input(
            self._NATIONALITY_FIELD_LOCATOR, self.enter_nationality
        )
        res1 = self.click_on_element(self._NATIONALITY_LOCATOR)
        return res and res1

    def input_city_field(self, city):
        return self.enter_field_input(self._CITY_FIELD_LOCATOR, city)

    def input_zipcode_field(self, zipcode):
        return self.enter_field_input(self._ZIP_CODE_FIELD_LOCATOR, zipcode)

    @property
    def input_country_field(self):
        res = self.enter_field_input(self._COUNTRY_FIELD_LOCATOR, self.enter_country)
        res1 = self.click_on_element(self._COUNTRY_LOCATOR)
        return res and res1

    @property
    def click_save_button(self):
        return self.click_on_element(self._SAVE_BUTTON_LOCATOR)

    def student_form(
        self,
        student_first_name,
        student_last_name,
        email,
        number,
        address,
        state,
        city,
        zipcode,
    ):
        res1 = self.input_name_field(student_first_name)
        res2 = self.input_lastname_field(student_last_name)
        res3 = self.input_email_field(email)
        res4 = self.input_number_field(number)
        res5 = self.input_gender_field
        res6 = self.input_nationality_field
        res7 = self.input_address_field(address)
        res8 = self.input_state_field(state)
        res9 = self.input_city_field(city)
        res10 = self.input_zipcode_field(zipcode)
        res11 = self.input_country_field
        res12 = self.input_date_of_birth_field
        res13 = self.click_save_button
        time.sleep(2)
        return (
            res1,
            res2,
            res3,
            res4,
            res5,
            res6,
            res7,
            res8,
            res9,
            res10,
            res11,
            res12,
            res13,
        )

    # @property
    # def check_name_validation(self):
    #     self.scroll_into_view(self._VERIFY_NAME_TEXT)
    #     name = self.get_text_of_elements(self._VERIFY_NAME_TEXT)
    #     name_output = self.convert_list_to_string(name).strip(self.student_last_name)
    #     lastname = self.get_text_of_elements(self._VERIFY_NAME_TEXT)
    #     lastname_output = self.convert_list_to_string(lastname).strip("ajamadar")
    #     print(name_output), print(lastname_output)
    #     return name_output == "ajamadar", lastname_output == "student"

    def check_name_validation(self, student_first_name, student_last_name):
        time.sleep(2)
        print("i" + student_first_name, student_last_name)
        a = self.get_text_of_elements(self._VERIFY_NAME_TEXT)
        text_output = self.convert_list_to_string(a)
        return student_first_name in text_output and student_last_name in text_output

    def check_email_and_number_validation(self, stud_number):
        email = self.get_text_of_elements(self._EMAIL_ADDRESS_FIELD_LOCATOR)
        email_output = self.convert_list_to_string(email)
        number = self.get_text_of_elements(self._NUMBER_FIELD_LOCATOR)
        number_output = self.convert_list_to_string(number)
        print(email), print(number)
        return (
            email_output == constants.STUD_PROFILE_EMAIL,
            number_output == stud_number,
        )

    @property
    def check_gender_validation(self):
        self.scroll_into_view(self._GENDER_LOCATOR)
        gender = self.get_text_of_elements(self._GENDER_LOCATOR)
        gender_output = self.convert_list_to_string(gender)
        print(gender_output)
        return gender_output == "Male"

    @property
    def check_nationality_and_country_validation(self):
        nationality = self.get_text_of_elements(self._VERIFY_NATIONALITY_TEXT)
        nationality_output = self.convert_list_to_string(nationality)
        country = self.get_text_of_elements(self._VERIFY_COUNTRY_TEXT)
        country_output = self.convert_list_to_string(country)
        print(nationality_output), print(country_output)
        return nationality_output in self.Nationality, country_output in self.Country

    @property
    def check_profile_completion_validation(self):
        self.scroll_into_view(self._VERIFY_NAME_TEXT)
        profile_completion = self.get_text_of_elements(self._VERIFY_PROFILE_COMPLETION)
        profile_completion_output = self.convert_list_to_string(profile_completion)
        print(profile_completion_output)
        return profile_completion_output == "55 %"

    def student_form_negative_input_1(self, empty_name):
        self.input_name_field(empty_name)
        name_error_msg = self.get_text_of_elements(self._FIRST_NAME_ERROR_MSG)
        print(self.convert_list_to_string(name_error_msg))

        self.input_lastname_field(empty_name)
        lastname_error_msg = self.get_text_of_elements(self._LAST_NAME_ERROR_MSG)
        print(self.convert_list_to_string(lastname_error_msg))

        # self.input_number_field(empty_name)
        # number_error_msg = self.get_text_of_elements(self._NUMBER_ERROR_MSG)
        # print(self.convert_list_to_string(number_error_msg))

        return (
            self.convert_list_to_string(name_error_msg) == "First Name cannot be empty",
            self.convert_list_to_string(lastname_error_msg)
            == "Last Name cannot be empty",
            # self.convert_list_to_string(number_error_msg) == "Phone number is invalid",
        )

    def student_form_negative_input_2(self, empty_name):
        self.scroll_into_view(self._STATE_FIELD_LOCATOR)
        self.input_state_field(empty_name)
        state_error_msg = self.get_text_of_elements(self._STATE_ERROR_MSG)
        print(self.convert_list_to_string(state_error_msg))

        self.input_city_field(empty_name)
        city_error_msg = self.get_text_of_elements(self._CITY_ERROR_MSG)
        print(self.convert_list_to_string(city_error_msg))

        self.input_zipcode_field(empty_name)
        zipcode_error_msg = self.get_text_of_elements(self._ZIPCODE_ERROR_MSG)
        print(self.convert_list_to_string(zipcode_error_msg))

        return (
            self.convert_list_to_string(state_error_msg) == "State cannot be empty",
            self.convert_list_to_string(city_error_msg)
            == "City/Town/Village cannot be empty",
            self.convert_list_to_string(zipcode_error_msg) == "Zipcode cannot be empty",
        )

    @property
    def input_wrong_date_of_birth_field(self):
        self.click_on_element(self._DATE_OF_BIRTH_LOCATOR)
        self.click_on_element(self._YEAR_DROP_DOWN_LOCATOR)
        time.sleep(1)
        self.click_on_element(self._SELECT_WRONG_YEAR_LOCATOR)
        time.sleep(1)
        self.click_on_element(self._SELECT_MONTH_LOCATOR)
        time.sleep(1)
        self.click_on_element(self._SELECT_DATE_LOCATOR)
        return True

    def student_form_negative_input_3(self, max_char):
        self.input_address_field(max_char)
        street_error_msg = self.get_text_of_elements(self._STREET_ERROR_MSG)
        print(self.convert_list_to_string(street_error_msg))

        return (
            self.convert_list_to_string(street_error_msg)
            == "Street Address cannot be empty"
        )

    @property
    def student_form_negative_input_4(self):
        res = self.input_wrong_date_of_birth_field
        calendar_error_msg = self.get_text_of_elements(self._CALENDER_ERROR_MSG)
        print(self.convert_list_to_string(calendar_error_msg))

        return (
            res,
            self.convert_list_to_string(calendar_error_msg)
            == "Age should be at least 10 years",
        )

    @property
    def click_on_test_score_tab(self):
        return self.click_on_element(self._TEST_SCORES_LOCATOR)

    @property
    def click_on_add_test_score_button(self):
        res1 = self.scroll_to_down()
        res2 = self.click_on_element(self._ADD_TEST_SCORE_LOCATOR)
        return res1, res2

    @property
    def select_exam_date(self):
        res1 = self.click_on_element(self._DATEPICKER_INPUT_LOCATOR)
        res2 = self.click_on_element(self._SELECT_TEST_MONTH_LOCATOR)
        res3 = self.click_on_element(self._SELECT_TEST_DATE_LOCATOR)
        return res1 and res2 and res3

    def enter_listing_exam_score(self, score):
        return self.enter_field_input(self._LISTENING_INPUT_LOCATOR, score)

    def enter_reading_exam_score(self, score):
        return self.enter_field_input(self._READING_INPUT_LOCATOR, score)

    def enter_writing_exam_score(self, score):
        return self.enter_field_input(self._WRITING_INPUT_LOCATOR, score)

    @property
    def save_form(self):
        return self.click_on_element(self._SAVE_BUTTON_LOCATOR)

    @property
    def select_entrance_exam(self):
        res1 = self.click_on_element(self._EXAM_TYPE_DROPDOWN_LOCATOR)
        res2 = self.click_on_element(self._ENTRANCE_EXAM_DROPDOWN_LOCATOR)
        return res1 and res2

    @property
    def select_english_proficiency_exam(self):
        res1 = self.click_on_element(self._EXAM_TYPE_DROPDOWN_LOCATOR)
        res2 = self.click_on_element(self._ENGLISH_PROFICIENCY_DROPDOWN_LOCATOR)
        return res1 and res2

    def enter_total_score(self, score):
        return self.enter_field_input(self._TOTAL_INPUT_LOCATOR, score)

    @property
    def select_gre_exam(self):
        res1 = self.click_on_element(self._ENTRANCE_EXAM_TYPE_LOCATOR)
        res2 = self.click_on_element(self._GRE_EXAM_TYPE_LOCATOR)
        return res1 and res2

    @property
    def select_sat_exam(self):
        res1 = self.click_on_element(self._ENTRANCE_EXAM_TYPE_LOCATOR)
        res2 = self.click_on_element(self._SAT_EXAM_TYPE_LOCATOR)
        return res1 and res2

    @property
    def select_act_exam(self):
        res1 = self.click_on_element(self._ENTRANCE_EXAM_TYPE_LOCATOR)
        res2 = self.click_on_element(self._ACT_EXAM_TYPE_LOCATOR)
        return res1 and res2

    @property
    def select_gmat_exam(self):
        res1 = self.click_on_element(self._ENTRANCE_EXAM_TYPE_LOCATOR)
        res2 = self.click_on_element(self._GMAT_EXAM_TYPE_LOCATOR)
        return res1 and res2

    def enter_gre_scores(self, analytical, qr, vr):
        res1 = self.enter_field_input(self._ANALYTICAL_EXAM_INPUT_LOCATOR, analytical)
        res2 = self.enter_field_input(
            self._QUANTITATIVE_REASONING_EXAM_INPUT_LOCATOR, qr
        )
        res3 = self.enter_field_input(self._VERBAL_REASONING_EXAM_INPUT_LOCATOR, vr)
        return res1 and res2 and res3

    @property
    def select_tofel_ibt(self):
        res1 = self.click_on_element(self._ENGLISH_EXAM_TYPE_DROPDOWN_LOCATOR)
        res2 = self.click_on_element(self._TOEFL_IBT_LOCATOR)
        return res1 and res2

    @property
    def select_revised_tofel_paper(self):
        res1 = self.click_on_element(self._ENGLISH_EXAM_TYPE_DROPDOWN_LOCATOR)
        res2 = self.click_on_element(self._REVISED_TOEFL_PAPER_DELIVERED_TEST_LOCATOR)
        return res1 and res2

    @property
    def select_ielts_academic(self):
        res1 = self.click_on_element(self._ENGLISH_EXAM_TYPE_DROPDOWN_LOCATOR)
        res2 = self.click_on_element(self._IELTS_ACADEMIC_LOCATOR)
        return res1 and res2

    @property
    def select_ielts_general_training(self):
        res1 = self.click_on_element(self._ENGLISH_EXAM_TYPE_DROPDOWN_LOCATOR)
        res2 = self.click_on_element(self._IELTS_GENERAL_TRAINING_LOCATOR)
        return res1 and res2

    @property
    def select_person_pte(self):
        res1 = self.click_on_element(self._ENGLISH_EXAM_TYPE_DROPDOWN_LOCATOR)
        res2 = self.click_on_element(self._PERSON_PTE_LOCATOR)
        return res1 and res2

    @property
    def select_cambridge_english(self):
        res1 = self.click_on_element(self._ENGLISH_EXAM_TYPE_DROPDOWN_LOCATOR)
        res2 = self.click_on_element(self._CAMBRIDGE_ENGLISH_LOCATOR)
        return res1 and res2

    @property
    def select_kaplan_english(self):
        res1 = self.click_on_element(self._ENGLISH_EXAM_TYPE_DROPDOWN_LOCATOR)
        res2 = self.click_on_element(self._KAPLAN_ENGLISH_LOCATOR)
        return res1 and res2

    def verify_exam_type(self, exam_text_input):
        exam_text = self.get_text_of_elements(self._VERIFY_EXAM_TYPE_LOCATOR)
        print(self.convert_list_to_string(exam_text), exam_text_input)
        return self.convert_list_to_string(exam_text) == exam_text_input

    def verify_sub_exam_type(self, exam_text_input):
        exam_text = self.get_text_of_elements(self._VERIFY_SUB_EXAM_TYPE_LOCATOR)
        print(self.convert_list_to_string(exam_text), exam_text_input)
        return self.convert_list_to_string(exam_text) == exam_text_input

    def verify_single_score(self, input_score):
        exam_text = self.get_text_of_elements(
            self._VERIFY_SINGLE_EXAM_SCORE_VALUE_LOCATOR
        )
        print(self.convert_list_to_string(exam_text))
        return self.convert_list_to_string(exam_text) == input_score

    def verify_multiple_score(self, score1, score2, score3):
        listing = self.get_text_of_elements(
            self._VERIFY_LISTENING_EXAM_SCORE_TYPE_LOCATOR
        )
        print(self.convert_list_to_string(listing), score1)
        res1 = self.convert_list_to_string(listing) == score1
        reading = self.get_text_of_elements(
            self._VERIFY_READING_EXAM_SCORE_TYPE_LOCATOR
        )
        print(self.convert_list_to_string(reading), score2)
        res2 = self.convert_list_to_string(reading) == score2
        writing = self.get_text_of_elements(
            self._VERIFY_WRITING_EXAM_SCORE_TYPE_LOCATOR
        )
        print(self.convert_list_to_string(writing), score3)
        res3 = self.convert_list_to_string(writing) == score3
        return res1 and res2 and res3

    def verify_multiple_score_value(self, score1, score2, score3):
        listing = self.get_text_of_elements(
            self._VERIFY_LISTENING_EXAM_SCORE_VALUE_LOCATOR
        )
        print(self.convert_list_to_string(listing), score1)
        res1 = self.convert_list_to_string(listing) == score1
        reading = self.get_text_of_elements(
            self._VERIFY_READING_EXAM_SCORE_VALUE_LOCATOR
        )
        print(self.convert_list_to_string(reading), score2)
        res2 = self.convert_list_to_string(reading) == score2
        writing = self.get_text_of_elements(
            self._VERIFY_WRITING_EXAM_SCORE_VALUE_LOCATOR
        )
        print(self.convert_list_to_string(writing), score3)
        res3 = self.convert_list_to_string(writing) == score3
        return res1 and res2 and res3

    @property
    def go_to_experience_tab(self):
        return self.click_on_element(self._EXPERIENCE_LOCATOR)

    @property
    def check_experience_page_url(self):
        return self.check_for_new_url(
            "https://student-dashboard-release."
            "ischoolconnect.com/dashboard/profile#experience"
        )

    @property
    def click_on_add_experience(self):
        return self.click_on_element(self._ADD_EXPERIENCE_LOCATOR)

    def enter_company_name(self, company_name):
        return self.enter_field_input(self._COMPANY_NAME_INPUT_LOCATOR, company_name)

    def enter_city_name(self, city):
        return self.enter_field_input(self._CITY_NAME_INPUT_LOCATOR, city)

    def select_country(self, country):
        res3 = self.click_on_element(self._COUNTRY_INPUT_LOCATOR)
        res1 = self.enter_field_input(self._COUNTRY_INPUT_LOCATOR, country)
        res2 = self.click_on_element(self._COUNTRY_DROPDOWN_LOCATOR)
        return res1 and res2 and res3

    def enter_title(self, title):
        return self.enter_field_input(self._TITLE_LOCATOR, title)

    def select_employment_type(self, employment_type):
        res3 = self.click_on_element(self._EMPLOYEE_TYPE_INPUT_LOCATOR)
        res1 = self.enter_field_input(
            self._EMPLOYEE_TYPE_INPUT_LOCATOR, employment_type
        )
        res2 = self.click_on_element(self._EMPLOYEE_DROPDOWN_LOCATOR)
        return res1 and res2 and res3

    def select_industry(self, industry):
        res3 = self.click_on_element(self._INDUSTRY_INPUT_LOCATOR)
        # res3 = self.click_on_element(self._INDUSTRY_INPUT_LOCATOR)
        # name_field = self.selenium.find_element_by_css_selector('#student_profile_experience_section__industry_field [type="text"]')
        # time.sleep(0.9)
        # name_field.send_keys(str(industry))
        # self.selenium.find_element(self._INDUSTRY_INPUT_LOCATOR).send_keys(str(industry))
        res1 = self.enter_field_input(self._INDUSTRY_INPUT_LOCATOR, industry)
        res2 = self.click_on_element(self._INDUSTRY_DROPDOWN_LOCATOR)
        return res3 and res2 and res1

    @property
    def select_start_date(self):
        res1 = self.click_on_element(self._START_DATE_LOCATOR)
        res2 = self.click_on_element(self._EXP_START_YEAR)
        res3 = self.click_on_element(self._EXP_START_MONTH)
        return res1 and res2 and res3

    @property
    def select_end_date(self):
        res1 = self.click_on_element(self._END_DATE_LOCATOR)
        res2 = self.click_on_element(self._EXP_END_YEAR)
        res3 = self.click_on_element(self._EXP_END_MONTH)
        return res1 and res2 and res3

    @property
    def verify_start_date_error_msg(self):
        res1 = self.click_on_element(self._START_DATE_LOCATOR)
        res2 = self.click_on_element(self._EXP_INCORRECT_START_YEAR)
        res3 = self.click_on_element(self._EXP_INCORRECT_START_MONTH)
        return res1 and res2 and res3

    @property
    def check_working_here_checkbox(self):
        return self.click_on_element(self._WORKING_HERE_CHECKBOX_LOCATOR)

    def verify_experience_title(self, title):
        elem = self.get_text_of_elements(self._VERIFY_EXPERIENCE_TITLE_LOCATOR)
        title_output = self.convert_list_to_string(elem)
        print(title_output), print(title)
        return title_output == title

    def verify_experience_company_name(self, company):
        elem = self.get_text_of_elements(self._VERIFY_EXPERIENCE_COMPANY_NAME_LOCATOR)
        output = self.convert_list_to_string(elem)
        print(output), print(company)
        return output == company

    def verify_experience_city_and_country_name(self, city, country):
        elem = self.get_text_of_elements(self._VERIFY_CITY_AND_COUNTRY_LOCATOR)
        output = self.convert_list_to_string(elem)
        print(output), print(city, country)
        return output == city + " , " + country

    def verify_experience_employment_type_name(self, emp_type):
        elem = self.get_text_of_elements(self._VERIFY_EMPLOYMENT_TYPE_LOCATOR)
        output = self.convert_list_to_string(elem)
        print(output), print(emp_type)
        return output == emp_type

    def verify_experience_industry_name(self, industry):
        elem = self.get_text_of_elements(self._VERIFY_INDUSTRY_LOCATOR)
        output = self.convert_list_to_string(elem)
        print(output), print(industry)
        return output == industry

    @property
    def verify_experience_start_and_date(self):
        elem = self.get_text_of_elements(self._VERIFY_START_AND_END_DATE_LOCATOR)
        output = self.convert_list_to_string(elem)
        return output == "Feb 2019 - Jul 2021"

    @property
    def delete_entry(self):
        res1 = self.click_on_element(self._MENU_OPTION_LOCATOR)
        res2 = self.click_on_element(self._DELETE_BUTTON_LOCATOR)
        return res1 and res2

    @property
    def edit_entry(self):
        res1 = self.click_on_element(self._MENU_OPTION_LOCATOR)
        res2 = self.click_on_element(self._EDIT_BUTTON_LOCATOR)
        return res1 and res2

    @property
    def select_education_start_date(self):
        res1 = self.click_on_element(self._EDU_START_DATE_LOCATOR)
        res2 = self.click_on_element(self._EXP_START_YEAR)
        res3 = self.click_on_element(self._EXP_START_MONTH)
        return res1 and res2 and res3

    @property
    def select_education_end_date(self):
        res1 = self.click_on_element(self._EDU_END_DATE_LOCATOR)
        res2 = self.click_on_element(self._EXP_END_YEAR)
        res3 = self.click_on_element(self._EXP_END_MONTH)
        return res1 and res2 and res3

    def enter_institution_name(self, institute):
        return self.enter_field_input(self._INSTITUTION_NAME_LOCATOR, institute)

    def select_degree(self, degree):
        res1 = self.click_on_element(self._DEGREE_LOCATOR)
        res2 = self.enter_field_input(self._DEGREE_LOCATOR, degree)
        time.sleep(3)
        res3 = self.click_on_element(self._DROPDOWN_LOCATOR)
        return res1 and res2 and res3

    def select_field_of_study(self, fieldofstudy):
        res1 = self.click_on_element(self._FIELD_OF_STUDY_LOCATOR)
        res2 = self.enter_field_input(self._FIELD_OF_STUDY_LOCATOR, fieldofstudy)
        res3 = self.click_on_element(self._DROPDOWN_LOCATOR)
        return res1 and res2 and res3

    def enter_education_score(self, score):
        return self.enter_field_input(self._SCORE_INPUT_LOCATOR, score)

    @property
    def select_gpa(self):
        res1 = self.click_on_element(self._TYPE_OF_SCORE_LOCATOR)
        res2 = self.click_on_element(self._SELECT_GPA_SCORE)
        return res1 and res2

    @property
    def select_cgpa(self):
        res1 = self.click_on_element(self._TYPE_OF_SCORE_LOCATOR)
        res2 = self.click_on_element(self._SELECT_CGPA_SCORE)
        return res1 and res2

    @property
    def select_percentage(self):
        res1 = self.click_on_element(self._TYPE_OF_SCORE_LOCATOR)
        res2 = self.click_on_element(self._SELECT_PERCENTAGE_SCORE)
        return res1 and res2

    def verify_institute_name(self, institute):
        elem = self.get_text_of_elements(self._VERIFY_INSTITUTE_NAME)
        output = self.convert_list_to_string(elem)
        print(output), print(institute)
        return output == institute

    def verify_degree_name(self, degree):
        elem = self.get_text_of_elements(self._VERIFY_DEGREE_LOCATOR)
        output = self.convert_list_to_string(elem)
        print(output), print(degree)
        return output == degree

    def verify_field_of_study(self, fieldofstudy):
        elem = self.get_text_of_elements(self._VERIFY_FIELD_LOCATOR)
        output = self.convert_list_to_string(elem)
        print(output), print(fieldofstudy)
        return fieldofstudy in output

    def verify_score(self, score):
        elem = self.get_text_of_elements(self._VERIFY_SCORE)
        output = self.convert_list_to_string(elem)
        print(output), print(score)
        return score in output

    @property
    def verify_date(self):
        elem = self.get_text_of_elements(self._VERIFY_DATE)
        output = self.convert_list_to_string(elem)
        print(output)
        return output == "Feb 2019 - Jul 2021"

    @property
    def click_on_add_school(self):
        return self.click_on_element(self._ADD_SCHOOL_LOCATOR)

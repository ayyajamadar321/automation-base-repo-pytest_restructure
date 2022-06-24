import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import constants
from pages.base_page import BasePage


class ExploreSchoolPage(BasePage):
    _EXPLORE_SCHOOL_TAB_LOCATOR = (By.CSS_SELECTOR, 'a[href="/dashboard/search_by"]')
    _STUDENT_EXPLORE_SCHOOL_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="navbar-inner-wrapper-for-scroll"] a:nth-child(3)',
    )
    _SEARCH_INPUT_TEXT_BOX_LOCATOR = (By.ID, "search_box")
    _UNIVERSITY_NAME_LIST_LOCATOR = (By.CSS_SELECTOR, '[class="universityName"]')
    _CITY_STATE_LIST_LOCATOR = (By.CSS_SELECTOR, '[class="cityStateDiv"]')
    _COUNTRY_LIST_LOCATOR = (By.CSS_SELECTOR, '[class="countryDiv"]')
    _COURSE_NAME_LIST_LOCATOR = (By.CSS_SELECTOR, '[class= "main"] [class="name"]')
    _SCHOOL_NAME_LIST_LOCATOR = (By.CSS_SELECTOR, ".school span")
    _DEGREE_LIST_LOCATOR = (
        By.CSS_SELECTOR,
        "div.degree__name",
    )
    _DEGREE_YEAR_LIST_LOCATOR = (
        By.CSS_SELECTOR,
        "div.stats-and-action  div  div:nth-child(3) div",
    )
    _TUITION_FEE_LIST_LOCATOR = (
        By.CSS_SELECTOR,
        "div.stats-and-action div div:nth-child(2) div div",
    )
    _BEST_RANK_FILTER_BUTTON_LOCATOR = (By.XPATH, "//div[contains(text(),'Best Rank')]")
    _BEST_MATCH_FILTER_BUTTON_LOCATOR = (By.XPATH, "//div[contains(text(),'Best Match')]")
    _TUITION_FEE_FILTER_BUTTON_LOCATOR = (By.XPATH, "//div[contains(text(),'Tuition Fee')]")
    _TUITION_FEE_FILTER_LOCATOR = (By.XPATH, "//div[contains(text(),'Tuition Fee')]//i")
    _COMMISSION_FILTER_BUTTON_LOCATOR = (
        By.XPATH,
        "//schools-explore[1]/div[1]/div[3]/div[2]/div[5]",
    )

    _COMMISSION_FILTER_LOCATOR = (By.XPATH, "//div[contains(text(),'Commission')]//i")
    _CANADA_COUNTRY_LOCATOR = (By.XPATH, "//span[contains(text(),'Canada')]")
    _USA_COUNTRY_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'United State Of America')]",
    )
    _AGRICULTURE_DISCIPLINE_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'Agriculture')]",
    )
    _ARTS_DISCIPLINE_LOCATOR = (By.XPATH, "//span[contains(text(),'Arts')]")
    _MASTER_DEGREE_LOCATOR = (By.XPATH, "//span[contains(text(),'Masters')]")
    _BACHELORS_DEGREE_LOCATOR = (By.XPATH, "//span[contains(text(),'Bachelors')]")
    _MIN_TUITION_FEE_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'30,000 USD/year or less')]",
    )
    _MAX_TUITION_FEE_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'50,000 USD/year or less')]",
    )
    _SAM_OF_EDUCATION_APPROVE_LOCATOR = (By.XPATH, "//span[contains(text(),'Approve')]")
    _SAM_OF_EDUCATION_NOT_APPROVE_LOCATOR = (
        By.XPATH,
        "//div[contains(text(),'Not Approve')]",
    )
    _COMMISSION_RESULT_LOCATOR = (
        By.CSS_SELECTOR,
        "div.action.desktop.ng-star-inserted > div > div > div.label",
    )
    _COMMISSION_AMOUNT_RESULT_LOCATOR = (
        By.CSS_SELECTOR,
        "div.action.desktop.ng-star-inserted > div > div > div.value",
    )
    _NO_RESULT_FOUND_LOCATOR = (
        By.XPATH,
        "//h4[contains(text(),'No Matching Results')]",
    )
    _CLEAR_ALL_LINK_LOCATOR = (By.XPATH, "//span[contains(text(),'Clear all')]")
    _RESET_SEARCH_FIELD_LOCATOR = (
        By.CSS_SELECTOR,
        "[class='search__clear_button ng-star-inserted'] i",
    )
    _SEARCH_COUNTRY_FILTER_LOCATOR = (By.XPATH, "//div[@class='search_by-bar desktop']/input")
    _SEARCH_COUNTRY_FILTER_RESULT_LOCATOR = (
        By.CSS_SELECTOR,
        "div.child-wrapper.ng-star-inserted div:nth-child(3) mat-checkbox",
    )
    BROWSE_COURSE_ADD_TO_FAVOURITES_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "isc-school-item:nth-child(1) isc-course-item:nth-child(1) div.action.desktop.showFavorite "
        "isc-shortlist-button span.mat-button-wrapper span",
    )
    BROWSE_COURSE_APPLY_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "isc-school-item:nth-child(1) isc-course-item:nth-child(1) div.action.desktop.showFavorite > isc-apply-button "
        "> button > span.mat-button-wrapper",
    )
    _APPLICATION_CYCLE_YEAR_BUTTON_LOCATOR = (By.XPATH, "//*[contains(text(),'2023')]")
    _APPLICATION_CYCLE_SEASON_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[for='application_cycle_season-0']")
    _APPLICATION_CYCLE_APPLY_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#save_button > span.mat-button-wrapper")
    _APPLICATION_CROSS_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        ".student_application_close_details",
    )
    _CANCEL_APPLICATION_CONFIRMATION_LOCATOR = (By.ID, "yes_button")
    _STUDENT_DASHBOARD_BUTTON_LOCATOR = (By.CSS_SELECTOR, "nav.navbar-content a:nth-child(1)")
    _SEARCH_FROM_YOUR_FAVORITES_LOCATOR = (By.XPATH, "//input[@placeholder='Search from your favorites.']")
    _STUDENT_DASHBOARD_ADDED_TO_FAVORITE_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "button span.mat-button-wrapper span",
    )
    _STUDENT_DASHBOARD_APPLIED_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "isc-apply-button button span:nth-child(1)",
    )

    # *************** kaplan *******************
    # _PARTNERSHIP_FILTER_RESULT_LOCATOR = (By.CSS_SELECTOR, ".isc-partner")
    # _PARTNERSHIP_UNIVERSITY_FILTER_LOCATOR = (
    #     By.XPATH,
    #     "//span[contains(text(),'University')]",
    # )
    _PARTNERSHIP_PUBLIC_UNIVERSITY_FILTER_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'Public University')]",
    )
    # _PARTNERSHIP_POLYTECHNIC_INSTITUTE_FILTER_LOCATOR = (
    #     By.XPATH,
    #     "//span[contains(text(),'Polytechnic Institute')]",
    # )
    _PARTNERSHIP_TYPE_LOGO_LOCATOR = (
        By.CSS_SELECTOR,
        "[class='mat-tooltip-trigger isc-partner ng-star-inserted']",
    )
    _ADVANCED_KAPLAN_LEVEL_FILTER_LOCATOR = (
        By.CSS_SELECTOR,
        "filter-group div div:nth-child(7) div.list mat-radio-button:nth-child(6)",
    )
    _ALL_KAPLAN_LEVEL_FILTER_LOCATOR = (
        By.CSS_SELECTOR,
        "filter-group div:nth-child(7) div.list mat-radio-button:nth-child(1)",
    )
    _KAPLAN_LEVEL_FILTER_RESULT_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > div > div.value")
    _KAPLAN_COMMISSION_FILTER_BUTTON_LOCATOR = (
        By.XPATH,
        "//schools-explore[1]/div[1]/div[3]/div[2]/div[4]",
    )
    # *************** isc *********************
    _ACCEPTANCE_RATE_FILTER_BUTTON_LOCATOR = (
        By.XPATH,
        "//div[contains(text(),' Acceptance Rate ')]",
    )
    _ACCEPTANCE_RATE_FILTER_UP_AND_DOWN_LOCATOR = (
        By.XPATH,
        "//div[contains(text(),' Acceptance Rate ')]//i",
    )
    _ACCEPTANCE_RATE_FILTER_RESULT_LOCATOR = (
        By.XPATH,
        "//div[@class='stat ng-star-inserted']//div[contains(text(),'Acceptance Rate')]",
    )
    _ACCEPTANCE_RATE_PERCENTAGE_RESULT_LOCATOR = (
        By.CSS_SELECTOR,
        "div.stats.desktop.ng-star-inserted > div:nth-child(2) > div > div.value",
    )
    _ISC_COMMISSION_FILTER_BUTTON_LOCATOR = (
        By.XPATH,
        "//schools-explore[1]/div[1]/div[3]/div[2]/div[5]",
    )
    _ISC_PARTNER_FILTER_LOCATOR = (
        By.XPATH,
        "//filter-group//div[5]/div[2]/div[1]/div/mat-checkbox/label/span[2]",
    )
    _ISC_NON_PARTNER_FILTER_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'Non Partner')]",
    )
    _ISC_RANK_TEXT_RESULT_FILTER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(1) > div >div.value")
    _UNIVERSITY_LOGO_LOCATOR = (By.CSS_SELECTOR, "isc-school-item:nth-child(1) img")

    def click_on_explore_school_tab(self):
        return self.click_on_element(self._EXPLORE_SCHOOL_TAB_LOCATOR)

    def click_on_student_explore_school(self):
        return self.click_on_element(self._STUDENT_EXPLORE_SCHOOL_LOCATOR)

    def click_on_search_bar(self):
        return self.click_on_element(self._SEARCH_INPUT_TEXT_BOX_LOCATOR)

    def enter_search_input(self, k):
        return self.enter_field_input(self._SEARCH_INPUT_TEXT_BOX_LOCATOR, k)

    def enter_filter_search_input(self, k):
        return self.enter_field_input(self._SEARCH_COUNTRY_FILTER_LOCATOR, k)

    def clear_filter_button(self, ):
        return self.click_on_element(self._CLEAR_ALL_LINK_LOCATOR)

    def click_on_the_university_logo(self):
        return self.click_on_element(self._UNIVERSITY_LOGO_LOCATOR)

    def is_logo_displayed(self):
        """Check to see if main logo is available"""
        return self.check_page_element(self._PARTNERSHIP_TYPE_LOGO_LOCATOR)

    def verify_search_result_using_course(self, search):
        time.sleep(3)
        result = True
        for k, v in search.items():
            self.enter_search_input(k)
            time.sleep(3)
            text_output = self.get_text_of_elements(self._COURSE_NAME_LIST_LOCATOR)
            print(text_output)
            i = len(text_output)
            for elem in range(i):
                if v[0] in text_output or v[1] in text_output or v[2] in text_output:
                    print(text_output)
                    result = True
                else:
                    result = False
        return result

    def verify_search_result_using_university(self, search):
        result = True
        for k, v in search.items():
            self.enter_search_input(k)
            time.sleep(3)
            text_output = self.get_text_of_elements(self._UNIVERSITY_NAME_LIST_LOCATOR)
            print(text_output)
            i = len(text_output)
            for elem in range(i):
                if v[0] in text_output or v[1] in text_output or v[2] in text_output:
                    print(text_output)
                    result = True
                else:
                    result = False
        return result

    def verify_search_result_using_country(self, search):
        result = True
        for k, v in search.items():
            self.enter_search_input(k)
            time.sleep(3)
            text_output = self.get_text_of_elements(self._CITY_STATE_LIST_LOCATOR)
            print(text_output)
            i = len(text_output)
            for elem in range(i):
                if v[0] in text_output or v[1] in text_output or v[2] in text_output:
                    print(text_output)
                    result = True
                else:
                    result = False
        return result

    def verify_negative_search_result(self, text, no_match):
        self.enter_search_input(text)
        time.sleep(3)
        text_output = self.get_text_of_elements(self._NO_RESULT_FOUND_LOCATOR)
        print(self.convert_list_to_string(text_output))
        return self.convert_list_to_string(text_output) == no_match

    # ----- best rank changed logic
    def click_on_best_rank_filter_button(self):
        return self.click_on_element(self._BEST_RANK_FILTER_BUTTON_LOCATOR)

    def get_list_of_universities(self, universities):
        text_output = self.get_text_of_elements(self._UNIVERSITY_NAME_LIST_LOCATOR)
        print(text_output)
        print(self.convert_list_to_string(text_output[0]))
        return self.convert_list_to_string(text_output[0]) == universities

    def verify_best_rank_result_using_input(self, search, universities):
        self.enter_search_input(search)
        self.click_on_best_rank_filter_button()
        time.sleep(3)
        return self.get_list_of_universities(universities)

    # ----- best match changed logic
    def click_on_best_match_filter_button(self):
        return self.click_on_element(self._BEST_MATCH_FILTER_BUTTON_LOCATOR)

    def get_list_of_courses(self, courses):
        text_output = self.get_text_of_elements(self._COURSE_NAME_LIST_LOCATOR)
        print(text_output)
        print(self.convert_list_to_string(text_output[0]))
        return self.convert_list_to_string(text_output[0]) == courses

    def verify_best_match_result_using_input(self, search, courses):
        self.enter_search_input(search)
        self.click_on_best_match_filter_button()
        time.sleep(3)
        return self.get_list_of_courses(courses)

    # -------- acceptance rate logic
    def click_on_acceptance_rate_filter_button(self):
        return self.click_on_element(self._ACCEPTANCE_RATE_FILTER_BUTTON_LOCATOR)

    def get_list_of_acceptance_rate(self):
        acceptance_rate_output = self.get_text_of_elements(
            self._ACCEPTANCE_RATE_PERCENTAGE_RESULT_LOCATOR
        )
        print(self.convert_list_to_string(acceptance_rate_output))
        return self.convert_list_to_string(acceptance_rate_output[0].strip("%")) == str(100)

    def verify_acceptance_rate_result_using_input(self, search, universities):
        self.enter_search_input(search)
        self.click_on_acceptance_rate_filter_button()
        time.sleep(3)
        res1 = self.get_list_of_universities(universities)
        res2 = self.get_list_of_acceptance_rate()
        return res1 and res2

    # -------- commission logic
    def click_on_isc_commission_filter(self):
        return self.click_on_element(self._COMMISSION_FILTER_BUTTON_LOCATOR)

    def get_list_of_commissions(self, commission):
        commission_text_output = self.get_text_of_elements(
            self._COMMISSION_RESULT_LOCATOR
        )
        print(self.convert_list_to_string(commission_text_output))
        return self.convert_list_to_string(commission_text_output) == commission

    def verify_isc_commission_result_using_input(self, search, university, commission):
        self.enter_search_input(search)
        self.click_on_isc_commission_filter()
        time.sleep(3)
        res1 = self.get_list_of_universities(university)
        res2 = self.get_list_of_commissions(commission)
        return res1 and res2

    def click_on_kaplan_commission_filter(self):
        return self.click_on_element(self._KAPLAN_COMMISSION_FILTER_BUTTON_LOCATOR)

    def verify_kaplan_commission_result_using_input(self, search, university, commission):
        self.enter_search_input(search)
        self.click_on_kaplan_commission_filter()
        time.sleep(3)
        res1 = self.get_list_of_universities(university)
        res2 = self.get_list_of_commissions(commission)
        return res1 and res2

    def reset_search_field(self):
        return self.click_on_element(self._RESET_SEARCH_FIELD_LOCATOR)

    def search_country_in_filter_search_input(self, enter_country):
        return self.enter_field_input(self._SEARCH_COUNTRY_FILTER_LOCATOR, enter_country)

    def get_list_of_countries(self, country):
        text_output = self.get_text_of_elements(self._COUNTRY_LIST_LOCATOR)
        print(self.convert_list_to_string(text_output[0]))
        return self.convert_list_to_string(text_output[0]) == country

    def verify_country_result(self, enter_country, result):
        time.sleep(2)
        self.reset_search_field()
        self.click_on_best_match_filter_button()
        self.click_on_element(self._CANADA_COUNTRY_LOCATOR)
        time.sleep(2)
        self.search_country_in_filter_search_input(enter_country)
        self.click_on_element(self._SEARCH_COUNTRY_FILTER_RESULT_LOCATOR)
        time.sleep(2)
        res = self.get_list_of_countries(result)
        return res

    def click_on_agriculture_discipline(self):
        return self.click_on_element(self._AGRICULTURE_DISCIPLINE_LOCATOR)

    def verify_course_result(self, course):
        self.scroll_into_view(self._COURSE_NAME_LIST_LOCATOR)
        self.click_on_agriculture_discipline()
        self.scroll_into_view(self._SEARCH_INPUT_TEXT_BOX_LOCATOR)
        res = self.get_list_of_courses(course)
        return res

    def select_bachelors_degree_filter(self):
        return self.click_on_element(self._BACHELORS_DEGREE_LOCATOR)

    def get_list_of_degree(self, degree):
        degree_output = self.get_text_of_elements(self._DEGREE_LIST_LOCATOR)
        print(self.convert_list_to_string(degree_output))
        return self.convert_list_to_string(degree_output[0]) == degree

    def verify_degree_result(self, degree):
        self.scroll_into_view(self._BACHELORS_DEGREE_LOCATOR)
        self.click_on_element(self._MASTER_DEGREE_LOCATOR)
        self.scroll_into_view(self._SEARCH_INPUT_TEXT_BOX_LOCATOR)
        res = self.get_list_of_degree(degree)
        return res

    def get_list_of_tuition_fee(self):
        tuition_fee_output = self.get_text_of_elements(self._TUITION_FEE_LIST_LOCATOR)
        print(self.convert_list_to_string(tuition_fee_output))
        return self.convert_list_to_string(tuition_fee_output[0].strip("CAD")) < str(30000)

    def click_on_maximum_tuition_fee_button(self):
        self.scroll_into_view(self._MAX_TUITION_FEE_LOCATOR)
        return self.click_on_element(self._MAX_TUITION_FEE_LOCATOR)

    def click_on_minimum_tuition_fee_button(self):
        self.scroll_into_view(self._MIN_TUITION_FEE_LOCATOR)
        return self.click_on_element(self._MIN_TUITION_FEE_LOCATOR)

    def verify_tuition_fee_result(self, university):
        self.click_on_minimum_tuition_fee_button()
        self.scroll_into_view(self._SEARCH_INPUT_TEXT_BOX_LOCATOR)
        res1 = self.get_list_of_universities(university)
        res2 = self.get_list_of_tuition_fee()
        return res1 and res2

    def click_on_public_university_filter_locator(self):
        self.scroll_into_view(self._PARTNERSHIP_PUBLIC_UNIVERSITY_FILTER_LOCATOR)
        return self.click_on_element(self._PARTNERSHIP_PUBLIC_UNIVERSITY_FILTER_LOCATOR)

    def verify_kaplan_partnership_type(self, university):
        self.click_on_public_university_filter_locator()
        self.scroll_into_view(self._SEARCH_INPUT_TEXT_BOX_LOCATOR)
        res1 = self.get_list_of_universities(university)
        res2 = self.is_logo_displayed()
        return res1 and res2

    def click_on_partner_filter_locator(self):
        self.scroll_into_view(self._ISC_PARTNER_FILTER_LOCATOR)
        return self.click_on_element(self._ISC_PARTNER_FILTER_LOCATOR)

    def verify_isc_partnership_type(self, university):
        self.click_on_partner_filter_locator()
        self.scroll_into_view(self._SEARCH_INPUT_TEXT_BOX_LOCATOR)
        return self.get_list_of_universities(university)

    def verify_Kaplan_level(self, university):  # self.output_universities[0]
        self.scroll_into_view(self._ALL_KAPLAN_LEVEL_FILTER_LOCATOR)
        self.click_on_element(self._ALL_KAPLAN_LEVEL_FILTER_LOCATOR)
        self.scroll_into_view(self._SEARCH_INPUT_TEXT_BOX_LOCATOR)
        text_output = self.get_text_of_elements(self._UNIVERSITY_NAME_LIST_LOCATOR)
        print(self.convert_list_to_string(text_output))
        kaplan_level = self.get_text_of_elements(self._KAPLAN_LEVEL_FILTER_RESULT_LOCATOR)
        print(self.convert_list_to_string(kaplan_level))
        return (
            self.convert_list_to_string(text_output[0])
            == university,
            self.convert_list_to_string(kaplan_level[0]) == "-",
        )

    def click_add_to_favorites_and_apply(self):
        self.scroll_into_view(self.BROWSE_COURSE_ADD_TO_FAVOURITES_BUTTON_LOCATOR)
        res1 = self.click_on_element(self.BROWSE_COURSE_ADD_TO_FAVOURITES_BUTTON_LOCATOR)
        time.sleep(2)
        res2 = self.apply_on_application
        return res1 and res2

    def apply_on_application(self):
        res1 = self.click_on_element(self.BROWSE_COURSE_APPLY_BUTTON_LOCATOR)
        res2 = self.click_on_element(self._APPLICATION_CYCLE_YEAR_BUTTON_LOCATOR)
        res3 = self.click_on_element(self._APPLICATION_CYCLE_SEASON_BUTTON_LOCATOR)
        res4 = self.click_on_element(self._APPLICATION_CYCLE_APPLY_BUTTON_LOCATOR)
        time.sleep(2)
        return res1 and res2 and res3 and res4

    def mouse_hover(self, discipline):  # self.output_discipline[1]
        self.click_on_element(self._STUDENT_DASHBOARD_BUTTON_LOCATOR)
        self.scroll_into_view(self._SEARCH_FROM_YOUR_FAVORITES_LOCATOR)
        self.enter_field_input(
            self._SEARCH_FROM_YOUR_FAVORITES_LOCATOR, discipline
        )
        time.sleep(3)
        hover_ele = self.selenium.find_element_by_css_selector("div.titles div")
        action = ActionChains(self.selenium)
        action.move_to_element(hover_ele).perform()
        time.sleep(3)
        return True

    def verify_dashboard_added_to_favorites_and_applied(self):
        text_output_added_to_favorites = self.get_text_of_elements(
            self._STUDENT_DASHBOARD_ADDED_TO_FAVORITE_BUTTON_LOCATOR
        )
        print(self.convert_list_to_string(text_output_added_to_favorites))
        text_output_applied = self.get_text_of_elements(self._STUDENT_DASHBOARD_APPLIED_BUTTON_LOCATOR)
        print(self.convert_list_to_string(text_output_applied))
        return (
            self.convert_list_to_string(text_output_added_to_favorites[0])
            == constants.ADDED_TO_FAVORITES,
            self.convert_list_to_string(text_output_applied[0]) == constants.APPLIED
        )

    def click_dashboard_add_to_favorites_and_apply(self):
        self.click_on_element(self._STUDENT_DASHBOARD_APPLIED_BUTTON_LOCATOR)
        self.click_on_element(self._CANCEL_APPLICATION_CONFIRMATION_LOCATOR)
        time.sleep(5)
        hover_ele = self.selenium.find_element_by_css_selector("div.titles div")
        action = ActionChains(self.selenium)
        action.move_to_element(hover_ele).perform()
        self.click_on_element(self._STUDENT_DASHBOARD_ADDED_TO_FAVORITE_BUTTON_LOCATOR)
        time.sleep(2)
        return True

    def check_commission_result(self, university):  # self.output_universities[6]
        # self.click_on_element(self._COMMISSION_BUTTON_LOCATOR)
        time.sleep(2)
        return self.get_list_of_universities(university)

    def check_isc_commission_result(self, university):  # self.output_universities[7]
        self.click_on_element(self._ISC_COMMISSION_FILTER_BUTTON_LOCATOR)
        time.sleep(2)
        return self.get_list_of_universities(university)

    def check_no_commission_result(self, university):  # self.output_universities[7]
        time.sleep(3)
        return self.get_list_of_universities(university)

    def verify_clear_filter(self, university):
        time.sleep(2)
        return self.get_list_of_universities(university)

    def check_the_university_name_in_url(self, university_name):
        time.sleep(2)
        url = self.selenium.current_url
        print(url)
        return university_name in url

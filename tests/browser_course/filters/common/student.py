import os
import allure
import pytest
from pages.authentication.login_page import LoginPage
from pages.browser_course.explore_school_page import ExploreSchoolPage
from tests.conftest import BaseTestClass


@allure.epic("Browse Course")
@allure.feature("Filters")
@allure.suite("Browse Course Student Login")
@allure.description("Test cases for browse course filters")
class StudentFilterByClass(BaseTestClass):

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.explore_school_instance = ExploreSchoolPage(self.driver)

    output_courses = ["Arts", "Architecture", "Computer Science", "Integrated Wood Design", "Horticulture",
                      "Horticultural Science - Urban Ecosystems"]
    output_countries = ["british columbia", "Canada"]
    output_universities = ["Los Medanos College", "Harvard University", "Arizona State University - Tempe",
                           "George Mason University", "University of Northern British Columbia",
                           "University of British Columbia - Vancouver", "University of Bridgeport",
                           "California State University - Stanislaus", "University of North Carolina - Greensboro",
                           "International Culinary Institute of America"]
    output_discipline = ["Computer Science", "Northern and Rural Community Planning"]

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        link = os.getenv("STUDENT_LOGIN_LINK")
        print(link)
        self.login_page_tab_instance.go_to_page(link)

    @allure.title("Validate student url")
    @allure.severity(allure.severity_level.MINOR)
    def test_01_url_displayed_properly(self):
        assert self.login_page_tab_instance.get_current_url()

    @allure.title("Enter correct email id, password and click on sign in button should redirect to student dashboard")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_enter_correct_credentials(self):
        email = os.getenv("STUDENT_LOGIN")
        password = os.getenv("STUDENT_PASSWORD")
        self.login_page_tab_instance.refresh()
        assert self.login_page_tab_instance.sign_in(email, password)

    @allure.title("Validate student dashboard url")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_check_student_dashboard_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("STUDENT_DASHBOARD_BASE_URL")
        )

    @allure.title("Clicking on closed button should close cookies consent")
    @allure.severity(allure.severity_level.MINOR)
    def test_04_close_cookies_consent(self):
        assert self.login_page_tab_instance.close_cookies_model()

    @allure.title("Click on browse course tab should redirect user to browse course")
    @allure.severity(allure.severity_level.MINOR)
    def test_05_go_to_explore_school_tab(self):
        assert self.explore_school_instance.click_on_student_explore_school()

    @allure.title("Clicking on best rank button should show best rank university")
    @allure.severity(allure.severity_level.MINOR)
    def test_06_check_best_rank_filter(self):
        assert self.explore_school_instance.verify_best_rank_result_using_input(
            self.output_courses[2], self.output_universities[1] or self.output_universities[2]
        )

    @allure.title("Clicking on best match button should show best match university")
    @allure.severity(allure.severity_level.MINOR)
    def test_07_check_best_match_filter(self):
        assert self.explore_school_instance.verify_best_match_result_using_input(
            self.output_courses[2], self.output_courses[2]
        )

    @allure.title(
        "Clicking on acceptance rate button should show acceptance rate")
    @allure.severity(allure.severity_level.MINOR)
    def test_08_check_acceptance_rate_filter(self):
        if os.getenv("CLIENT") == "kaplan":
            pass
        else:
            assert self.explore_school_instance.verify_acceptance_rate_result_using_input(
                self.output_courses[2], self.output_universities[0]
            )

    @allure.title("Clicking on country checkbox should show appropriate country results")
    @allure.severity(allure.severity_level.MINOR)
    def test_09_check_country_filter(self):
        assert self.explore_school_instance.verify_country_result(self.output_countries[0], self.output_countries[1])

    @allure.title("Clicking on course checkbox should show appropriate course results")
    @allure.severity(allure.severity_level.MINOR)
    def test_10_check_course_filter(self):
        assert self.explore_school_instance.verify_course_result(self.output_courses[3] or self.output_courses[4])

    @allure.title("Clicking on degree checkbox should show appropriate degree results")
    @allure.severity(allure.severity_level.MINOR)
    def test_11_check_degree_filter(self):
        assert self.explore_school_instance.verify_degree_result("Masters")

    @allure.title("Clicking on tuition fee checkbox should show tuition fee results")
    @allure.severity(allure.severity_level.MINOR)
    def test_12_check_tuition_fee_filter(self):
        assert self.explore_school_instance.verify_tuition_fee_result(
            self.output_universities[4] or self.output_universities[5])

    @allure.title(
        "Clicking on partnership checkbox should show partnership type")
    @allure.severity(allure.severity_level.MINOR)
    def test_13_check_partnership_type_filter(self):
        if os.getenv("CLIENT") == "kaplan":
            assert self.explore_school_instance.verify_kaplan_partnership_type(self.output_universities[6])
        else:
            assert self.explore_school_instance.verify_isc_partnership_type(self.output_universities[4])

    @allure.title("Clicking on clear filter button should clear all the selected entity")
    @allure.severity(allure.severity_level.MINOR)
    def test_14_click_on_clear_filter_working(self):
        assert self.explore_school_instance.clear_filter_button()

    @allure.title("Click on sign out button should redirected to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_15_sign_out(self):
        assert self.login_page_tab_instance.sign_out()

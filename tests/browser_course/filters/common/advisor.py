import os
import allure
import pytest
import constants
from pages.authentication.login_page import LoginPage
from pages.browser_course.explore_school_page import ExploreSchoolPage
from tests.conftest import BaseTestClass


@allure.epic("Browse Course")
@allure.feature("Filters")
@allure.suite("Browse Course Advisor Login")
@allure.description("Test cases for browse course filters")
class AdvisorOwnerFilterByClass(BaseTestClass):

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
        link = os.getenv("LOGIN_LINK")
        print(link)
        self.login_page_tab_instance.go_to_page(link)

    @allure.title("Validate correct advisor owner url is displayed")
    @allure.severity(allure.severity_level.MINOR)
    def test_01_url_displayed_properly(self):
        assert self.login_page_tab_instance.get_current_url()

    @allure.title(
        "Entering correct account owner name and password, and clicking on sign in button should "
        "redirect user to manage division screen"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_enter_correct_credentials(self):
        email = os.getenv("ADVISOR_LOGIN")
        password = os.getenv("ADVISOR_PASSWORD")
        self.login_page_tab_instance.refresh()
        assert self.login_page_tab_instance.sign_in(email, password)

    @allure.title("Validate correct student dashboard url is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_check_student_dashboard_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-students"
        )

    @allure.title("Clicking on closed button should close cookies consent")
    @allure.severity(allure.severity_level.MINOR)
    def test_04_close_cookies_consent(self):
        assert self.login_page_tab_instance.close_cookies_model()

    @allure.title("Clicking on browse course tab should redirect to browse course")
    @allure.severity(allure.severity_level.MINOR)
    def test_05_go_to_explore_school_tab(self):
        assert self.explore_school_instance.click_on_explore_school_tab()

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

    @allure.title("Clicking on commission button should show commission")
    @allure.severity(allure.severity_level.MINOR)
    def test_09_check_commission_filter(self):
        if os.getenv("CLIENT") == "kaplan":
            assert self.explore_school_instance.verify_kaplan_commission_result_using_input(
                self.output_courses[0], self.output_universities[3], constants.COMMISSION
            )
        else:
            assert self.explore_school_instance.verify_isc_commission_result_using_input(
                self.output_courses[0], self.output_universities[9], constants.COMMISSION
            )

    @allure.title("Clicking on country checkbox should show appropriate country results")
    @allure.severity(allure.severity_level.MINOR)
    def test_10_check_country_filter(self):
        assert self.explore_school_instance.verify_country_result(self.output_countries[0], self.output_countries[1])

    @allure.title("Clicking on course checkbox should show appropriate course results")
    @allure.severity(allure.severity_level.MINOR)
    def test_11_check_course_filter(self):
        assert self.explore_school_instance.verify_course_result(self.output_courses[3] or self.output_courses[4])

    @allure.title("Clicking on degree checkbox should show appropriate degree results")
    @allure.severity(allure.severity_level.MINOR)
    def test_12_check_degree_filter(self):
        assert self.explore_school_instance.verify_degree_result("Masters")

    @allure.title("Clicking on tuition fee checkbox should show tuition fee results")
    @allure.severity(allure.severity_level.MINOR)
    def test_13_check_tuition_fee_filter(self):
        assert self.explore_school_instance.verify_tuition_fee_result(
            self.output_universities[4] or self.output_universities[5])

    @allure.title(
        "Clicking on partnership checkbox should show partnership type")
    @allure.severity(allure.severity_level.MINOR)
    def test_14_check_partnership_type_filter(self):
        if os.getenv("CLIENT") == "kaplan":
            assert self.explore_school_instance.verify_kaplan_partnership_type(self.output_universities[6])
        else:
            assert self.explore_school_instance.verify_isc_partnership_type(self.output_universities[4])

    @allure.title("Clicking on clear filter button should clear all the selected entity")
    @allure.severity(allure.severity_level.MINOR)
    def test_15_click_on_clear_filter_working(self):
        assert self.explore_school_instance.clear_filter_button()

    @allure.title("Click on sign out button should redirected to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_16_sign_out(self):
        assert self.login_page_tab_instance.sign_out()

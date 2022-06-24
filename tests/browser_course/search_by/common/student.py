import os
import allure
import constants
import pytest
from pages.authentication.login_page import LoginPage
from pages.browser_course.explore_school_page import ExploreSchoolPage
from tests.conftest import BaseTestClass


@allure.epic("Browse Course")
@allure.feature("Search By Functionality")
@allure.suite("Browse Course Student Login")
@allure.description("Test cases for search by functionality")
class StudentSearchByClass(BaseTestClass):

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.explore_school_instance = ExploreSchoolPage(self.driver)

    discipline = {
        "Biology": ["Biology", "Biology", "Biology"],
        "Computer Science": [
            "Computer Science",
            "Computer Science",
            "Computer Science",
        ],
        "Biomedical": ["Biomedical", "Biomedical Studies", "Biomedical Engineering"],
    }
    university = {
        "Pace University": [
            "Pace University - New York",
            "Pace University - White Plains",
            "Pace University - Pleasantville",
        ]
    }
    country = {
        "London": [
            "Spitalfields, London",
            "London, North East England",
            "London, London",
        ]
    }

    kaplan_country = {
        "Canada": [
            "Peterborough,  Ontario",
            "Redwood City, California",
            "Vancouver,  British Columbia",
        ]
    }
    search = "abcxyz"

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

    @allure.title("Entering discipline in search_by should show discipline results")
    @allure.severity(allure.severity_level.MINOR)
    def test_06_check_search_discipline(self):
        assert self.explore_school_instance.verify_search_result_using_course(
            self.discipline
        )

    @allure.title("Entering university in search_by should show university results")
    @allure.severity(allure.severity_level.MINOR)
    def test_07_check_search_university(self):
        assert self.explore_school_instance.verify_search_result_using_university(
            self.university
        )

    @allure.title("Entering country in search_by should show country results")
    @allure.severity(allure.severity_level.MINOR)
    def test_08_check_search_country(self):
        if os.getenv("CLIENT") == "kaplan":
            assert self.explore_school_instance.verify_search_result_using_country(
                self.kaplan_country
            )
        else:
            assert self.explore_school_instance.verify_search_result_using_country(
                self.country
            )

    @allure.title("Entering invalid data in search_by should show 'no results'")
    @allure.severity(allure.severity_level.MINOR)
    def test_09_check_search_for_invalid_data(self):
        assert self.explore_school_instance.verify_negative_search_result(self.search, constants.NO_MATCH)

    @allure.title("Click on sign out button should redirected to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_sign_out(self):
        assert self.login_page_tab_instance.student_sign_out()

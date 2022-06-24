import os
import allure
import pytest
from pages.authentication.login_page import LoginPage
from pages.browser_course.explore_school_page import ExploreSchoolPage
from tests.conftest import BaseTestClass


@allure.epic("Browse Course")
@allure.feature("Navigate To School Profile")
@allure.suite("Browse Course Advisor Login")
@allure.description("Test cases for navigate to school profile page")
class AdvisorOwnerNavigateSchoolProfileClass(BaseTestClass):
    """Test for Class Home Page"""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.explore_school_instance = ExploreSchoolPage(self.driver)

    output_universities = ["Harvard University", "Arizona State University - Tempe", ]

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

    @allure.title("Clicking on university logo should redirect to appropriate university")
    @allure.severity(allure.severity_level.MINOR)
    def test_06_click_on_university(self):
        assert self.explore_school_instance.click_on_the_university_logo()

    @allure.title("Validate the university URL on school profile page")
    @allure.severity(allure.severity_level.MINOR)
    def test_07_check_the_university_name_in_url_on_school_profile(self):
        assert self.explore_school_instance.check_the_university_name_in_url(
            self.output_universities[1] or self.output_universities[2])

    @allure.title("Click on sign out button should redirected to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_sign_out(self):
        assert self.login_page_tab_instance.sign_out()

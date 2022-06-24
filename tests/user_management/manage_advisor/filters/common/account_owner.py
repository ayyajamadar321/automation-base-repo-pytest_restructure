# ****************** Work in progress *********************
import os
import allure
import pytest
from pages.authentication.login_page import LoginPage
from pages.user_management.manage_advisor_page import ManageAdvisorPage
from pages.user_management.manage_division_page import ManageDivisionPage
from tests.conftest import BaseTestClass


@allure.epic("User Management")
@allure.feature("Filters")
@allure.suite("User Management Account Owner Login")
@allure.description("Test cases for filters")
class AdvisorFilterClass(BaseTestClass):

    status = {1: "Active", 2: "Partial", 3: "Inactive", 4: "Disabled"}
    division_name = "test division"

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_instance = LoginPage(self.driver)
        self.div_manage_page_instance = ManageDivisionPage(self.driver)
        self.adv_manage_page_instance = ManageAdvisorPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        self.login_page_instance.go_to_page(os.environ.get("LOGIN_LINK"))

    @allure.title(
        "Entering correct email id, and password should take user to manage division page"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_01_enter_correct_credentials(self):
        email = os.getenv("ACCOUNT_OWNER_LOGIN")
        password = os.getenv("ACCOUNT_OWNER_PASSWORD")
        self.login_page_instance.refresh()
        assert self.login_page_instance.sign_in(email, password)

    @allure.title("Validate cookies consent is present and closed it")
    @allure.severity(allure.severity_level.MINOR)
    def test_02_close_cookies_consent(self):
        assert self.login_page_instance.close_cookies_model()

    @allure.title(
        "Clicking on manage advisor icon should redirect to manage advisor page"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_go_to_manage_advisor_page(self):
        assert self.div_manage_page_instance.go_to_manage_advisor_page()

    @allure.title(
        "selecting filter for status should show result only for that filters"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04_check_status_filter_is_working(self):
        assert self.adv_manage_page_instance.check_for_filters(self.status)

    @allure.title(
        "Selecting filter for division should show result for that division only"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_05_check_division_filter_is_working(self):
        assert self.adv_manage_page_instance.apply_and_verify_division_filter(self.division_name)

    @allure.title("Click on sign out button and user is redirected to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_sign_out(self):
        assert self.user_login_page.sign_out()

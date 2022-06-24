# ****************** Work in progress *********************
import os
import allure
import pytest
from pages.authentication.login_page import LoginPage
from pages.user_management.manage_division_page import ManageDivisionPage
from tests.conftest import BaseTestClass


@allure.epic("User Management")
@allure.feature("Filters")
@allure.suite("User Management Account Owner Login")
@allure.description("Test cases for filters")
class DivisionFilterClass(BaseTestClass):

    status = {1: "Active", 2: "Partial", 3: "Inactive", 4: "Disabled"}

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_instance = LoginPage(self.driver)
        self.div_manage_page_instance = ManageDivisionPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        self.login_page_instance.go_to_page(os.environ.get("LOGIN_LINK"))

    @allure.title("Enter correct email id, password and click on sign in button")
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

    @allure.title("Select all the status filter one by one and check properly")
    @allure.severity(allure.severity_level.MINOR)
    def test_04_check_status_filter_is_working(self):
        assert self.div_manage_page_instance.check_for_filters(self.status)

    @allure.title("Click on sign out button and user is redirected to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_sign_out(self):
        assert self.login_page_instance.sign_out()

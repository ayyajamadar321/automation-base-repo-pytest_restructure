import os

import allure
import pytest

import constants
from pages.authentication.login_page import LoginPage
from tests.conftest import BaseTestClass


@allure.epic("Authentication")
@allure.suite("Division Owner Login")
@allure.feature("Login")
@allure.description("Test cases for login via division owner")
class DivisionOwnerLoginClass(BaseTestClass):
    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        link = os.getenv("LOGIN_LINK")
        print(link)
        self.login_page_tab_instance.go_to_page(link)

    @allure.title("Validate correct division url is displayed")
    @allure.severity(allure.severity_level.MINOR)
    def test_01_url_displayed_properly(self):
        assert self.login_page_tab_instance.get_current_url()

    @allure.title("Validate correct page title is displayed")
    @allure.severity(allure.severity_level.MINOR)
    def test_02_title_displayed_properly(self):
        assert self.login_page_tab_instance.check_title_text_display()

    @allure.title(
        "Clicking on sign in button without entering any data should show an error message"
    )
    @allure.severity(allure.severity_level.BLOCKER)
    def test_03_for_empty_error_msg(self):
        self.login_page_tab_instance.click_on_sign_in_button()
        assert self.login_page_tab_instance.check_empty_error_message()

    @allure.title(
        "Entering invalid data in user name and password, and clicking on sign in button should show an"
        " error message"
    )
    @allure.severity(allure.severity_level.BLOCKER)
    def test_04_enter_incorrect_credentials(self):
        invalid_email = constants.INVALID_LOGIN
        invalid_password = constants.INVALID_PASSWORD
        self.login_page_tab_instance.sign_in(invalid_email, invalid_password)
        assert self.login_page_tab_instance.check_incorrect_error_message()

    @allure.title(
        "Entering correct account owner name and password, and clicking on sign in button should "
        "redirect to advisor dashboard"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_05_enter_correct_credentials(self):
        email = os.getenv("DIVISION_OWNER_LOGIN")
        password = os.getenv("DIVISION_OWNER_PASSWORD")
        self.login_page_tab_instance.refresh()
        assert self.login_page_tab_instance.sign_in(email, password)

    @allure.title("Validate correct advisor dashboard url is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_06_check_division_dashboard_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-advisors"
        )

    @allure.title("Clicking on close button should close the cookies consent")
    @allure.severity(allure.severity_level.MINOR)
    def test_07_close_cookies_consent(self):
        assert self.login_page_tab_instance.close_cookies()

    @allure.title("Click on sign out button should redirect to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_sign_out(self):
        assert self.login_page_tab_instance.sign_out()

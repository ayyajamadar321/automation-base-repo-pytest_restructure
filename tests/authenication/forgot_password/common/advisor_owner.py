import os
import allure
import pytest
import constants
from pages.authentication.forgot_password_page import ForgotPasswordPage
from pages.authentication.login_page import LoginPage
from tests.conftest import BaseTestClass


@allure.epic("Authentication")
@allure.feature("Forgot Password")
@allure.suite("Advisor Login")
@allure.description("Test cases for forgot password functionality")
class AdvisorOwnerForgotPasswordClass(BaseTestClass):
    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.forgot_password_page_instance = ForgotPasswordPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        link = os.getenv("LOGIN_LINK")
        print(link)
        self.login_page_tab_instance.go_to_page(link)

    @allure.title("Validate url is correct")
    @allure.severity(allure.severity_level.MINOR)
    def test_01_url_displayed_properly(self):
        assert self.login_page_tab_instance.get_current_url()

    @allure.title("Validate correct page title is displayed")
    @allure.severity(allure.severity_level.MINOR)
    def test_02_title_displayed_properly(self):
        assert self.login_page_tab_instance.check_title_text_display()

    @allure.title(
        "Clicking on forgot password button should redirect to forgot_password page"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_click_on_forgot_password(self):
        assert self.forgot_password_page_instance.click_on_forgot_password_link()

    @allure.title(
        "Entering invalid data in user name and password, and clicking on forget password button "
        "should show an error message"
    )
    @allure.severity(allure.severity_level.MINOR)
    def test_04_enter_incorrect_credentials(self):
        invalid_email = constants.INVALID_LOGIN
        assert self.forgot_password_page_instance.enter_invalid_email_id(invalid_email)

    @allure.title("Clicking on the reset password button")
    @allure.severity(allure.severity_level.MINOR)
    def test_05_click_on_sent_reset_instruction(self):
        assert self.forgot_password_page_instance.click_on_password_reset_button()

    @allure.title("Validating error message for invalid input")
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_validate_error_message(self):
        assert self.forgot_password_page_instance.check_incorrect_error_message()

    @allure.title("Entering valid email id in input field")
    @allure.severity(allure.severity_level.MINOR)
    def test_07_enter_correct_credentials(self):
        email = os.getenv("AUTOMATION_ADVISOR_LOGIN")
        assert self.forgot_password_page_instance.enter_correct_email_id(email)

    @allure.title("Clicking on the reset password button should sent a email to user")
    @allure.severity(allure.severity_level.MINOR)
    def test_08_click_on_sent_reset_instruction(self):
        assert self.forgot_password_page_instance.click_on_password_reset_button()

    @allure.title("Validating the text message appeared on screen")
    @allure.severity(allure.severity_level.NORMAL)
    def test_09_validate_password_reset_email_sent_text(self):
        assert (
            self.forgot_password_page_instance.validate_the_password_reset_email_sent_text()
        )

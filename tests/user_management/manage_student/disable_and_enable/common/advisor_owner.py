import os
import allure
import pytest

import constants
from pages.authentication.login_page import LoginPage
from pages.user_management.manage_advisor_page import ManageAdvisorPage
from pages.user_management.manage_student_page import ManageStudentPage
from tests.conftest import BaseTestClass


@allure.epic("User Management")
@allure.feature("Disable And Enable Functionality")
@allure.suite("User Management Advisor Owner Login")
@allure.description("Test cases for disable and enable user")
class DisableAndEnableStudentClass00(BaseTestClass):
    """Test for Class Home Page"""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.manage_student_instance = ManageStudentPage(self.driver)
        self.manage_advisor_instance = ManageAdvisorPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        link = os.getenv("LOGIN_LINK")
        print(link)
        self.login_page_tab_instance.go_to_page(link)

    @allure.title("Validate advisor url is correct")
    @allure.severity(allure.severity_level.MINOR)
    def test_01_url_displayed_properly(self):
        assert self.login_page_tab_instance.get_current_url()

    @allure.title("Validate page title is correct")
    @allure.severity(allure.severity_level.MINOR)
    def test_02_title_displayed_properly(self):
        assert self.login_page_tab_instance.check_title_text_display()

    @allure.title("Enter correct email id, password and click on sign in button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_enter_correct_credentials(self):
        email = os.environ.get("AUTOMATION_ADVISOR_LOGIN")
        password = os.environ.get("AUTOMATION_ADVISOR_PASSWORD")
        self.login_page_tab_instance.refresh()
        assert self.login_page_tab_instance.sign_in(email, password)

    @allure.title("Validate students management screen url is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04_check_manage_student_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-students"
        )

    @allure.title("Clicking on close button should close the cookies consent")
    @allure.severity(allure.severity_level.MINOR)
    def test_05_close_cookies_consent(self):
        assert self.login_page_tab_instance.close_cookies_model()

    @allure.title("Entering student email in search_by should show student details.")
    @allure.severity(allure.severity_level.MINOR)
    def test_06_search_for_newly_added_student(self):
        email = os.environ.get("DISABLE_STUDENT_EMAIL")
        assert self.manage_student_instance.search_for_student(email)

    @allure.title("Click on the action button should open action modal")
    @allure.severity(allure.severity_level.MINOR)
    def test_07_click_on_action_button(self):
        assert self.manage_student_instance.click_on_action_button()

    @allure.title("Clicking on disable button should disable the student")
    @allure.severity(allure.severity_level.MINOR)
    def test_08_click_on_disable_student_button(self):
        assert self.manage_advisor_instance.disable_student_details()

    @allure.title("Status should be disabled for disabled student")
    @allure.severity(allure.severity_level.MINOR)
    def test_09_validate_for_updated_student_details(self):
        assert self.manage_advisor_instance.check_for_student_status_name("Disabled")

    @allure.title("Click on sign out button should redirected to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_sign_out(self):
        assert self.login_page_tab_instance.sign_out()


@allure.suite("Disable and Enable student")
@allure.feature("User Management")
@allure.description("Disable/Enable student and validate using advisor login")
class DisableAndEnableStudentClass01(BaseTestClass):
    """Test for Class Home Page"""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.manage_student_instance = ManageStudentPage(self.driver)
        self.manage_advisor_instance = ManageAdvisorPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        link = os.getenv("STUDENT_LOGIN_LINK")
        print(link)
        self.login_page_tab_instance.go_to_page(link)

    @allure.title("Check student url is correct")
    @allure.severity(allure.severity_level.MINOR)
    def test_01_url_displayed_properly(self):
        assert self.login_page_tab_instance.get_current_url()

    @allure.title("Entering correct email id and password and clicking on sign in "
                  "button should redirect user to dashboard")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_enter_correct_credentials(self):
        email = os.environ.get("DISABLE_STUDENT_EMAIL")
        password = os.environ.get("DISABLE_STUDENT_PASSWORD")
        assert self.login_page_tab_instance.sign_in(email, password)

    @allure.title("Error message should appear at the top of the login page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_check_for_disable_advisor(self):
        assert self.manage_advisor_instance.check_disable_user_login_text(
            constants.Alert_MESSAGE
        )


@allure.suite("Disable and Enable student")
@allure.feature("User Management")
@allure.description("Disable/Enable student and validate using advisor login")
class DisableAndEnableStudentClass02(BaseTestClass):
    """Test for Class Home Page"""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.manage_student_instance = ManageStudentPage(self.driver)
        self.manage_advisor_instance = ManageAdvisorPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        link = os.getenv("LOGIN_LINK")
        print(link)
        self.login_page_tab_instance.go_to_page(link)

    @allure.title("Validate advisor url is correct")
    @allure.severity(allure.severity_level.MINOR)
    def test_01_url_displayed_properly(self):
        assert self.login_page_tab_instance.get_current_url()

    @allure.title("Validate page title is correct")
    @allure.severity(allure.severity_level.MINOR)
    def test_02_title_displayed_properly(self):
        assert self.login_page_tab_instance.check_title_text_display()

    @allure.title("Enter correct email id, password and clicking on sign in button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_enter_correct_credentials(self):
        email = os.environ.get("AUTOMATION_ADVISOR_LOGIN")
        password = os.environ.get("AUTOMATION_ADVISOR_PASSWORD")
        self.login_page_tab_instance.refresh()
        assert self.login_page_tab_instance.sign_in(email, password)

    @allure.title("Validate students management screen url is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04_check_manage_student_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-students"
        )

    @allure.title("Clicking on close button should close the cookies consent")
    @allure.severity(allure.severity_level.MINOR)
    def test_05_close_cookies_consent(self):
        assert self.login_page_tab_instance.close_cookies_model()

    @allure.title("Entering disable student email id should show student details")
    @allure.severity(allure.severity_level.MINOR)
    def test_06_search_for_newly_added_student(self):
        email = os.environ.get("DISABLE_STUDENT_EMAIL")
        assert self.manage_student_instance.search_for_student(email)

    @allure.title("Click on the action button should show action modal")
    @allure.severity(allure.severity_level.MINOR)
    def test_07_click_on_action_button(self):
        assert self.manage_student_instance.click_on_action_button()

    @allure.title("Clicking on enable button should student status")
    @allure.severity(allure.severity_level.MINOR)
    def test_08_click_on_enable_student_button(self):
        assert self.manage_advisor_instance.enable_student()

    @allure.title("Validate updated student details to enabled")
    @allure.severity(allure.severity_level.MINOR)
    def test_09_validate_for_updated_student_details(self):
        assert self.manage_advisor_instance.check_for_student_status_name("Induction")

    @allure.title("Clicking on sign out button should redirect to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_sign_out(self):
        assert self.login_page_tab_instance.sign_out()


@allure.suite("Disable and Enable student")
@allure.feature("User Management")
@allure.description("Disable/Enable student and validate using advisor login")
class DisableAndEnableStudentClass03(BaseTestClass):
    """Test for Class Home Page"""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.manage_student_instance = ManageStudentPage(self.driver)
        self.manage_advisor_instance = ManageAdvisorPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        link = os.getenv("STUDENT_LOGIN_LINK")
        print(link)
        self.login_page_tab_instance.go_to_page(link)

    @allure.title("Validate student url is correct")
    @allure.severity(allure.severity_level.MINOR)
    def test_01_url_displayed_properly(self):
        assert self.login_page_tab_instance.get_current_url()

    @allure.title("Entering correct email id and password and clicking on sign in "
                  "button should redirect user to dashboard")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_enter_correct_credentials(self):
        email = os.environ.get("DISABLE_STUDENT_EMAIL")
        password = os.environ.get("DISABLE_STUDENT_PASSWORD")
        assert self.login_page_tab_instance.sign_in(email, password)

    @allure.title("Clicking on close button should close the cookies consent")
    @allure.severity(allure.severity_level.MINOR)
    def test_03_close_cookies_consent(self):
        assert self.login_page_tab_instance.close_cookies_model()

    @allure.title("Clicking on sign out button should redirect to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_sign_out(self):
        assert self.login_page_tab_instance.student_sign_out()

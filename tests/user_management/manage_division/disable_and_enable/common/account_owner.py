import os
import allure
import constants
import pytest
from pages.authentication.login_page import LoginPage
from pages.user_management.manage_advisor_page import ManageAdvisorPage
from pages.user_management.manage_division_page import ManageDivisionPage
from tests.conftest import BaseTestClass


@allure.epic("User Management")
@allure.feature("Disable And Enable Functionality")
@allure.suite("User Management Account Owner Login")
@allure.description("Test cases for disable and enable user")
class DisableAndEnableDivisionClass00(BaseTestClass):
    """Test for disable division"""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_instance = LoginPage(self.driver)
        self.dash_page_instance = ManageDivisionPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        self.login_page_instance.go_to_page(os.environ.get("LOGIN_LINK"))

    @allure.title(
        "Login with correct account owner credential should redirect user to manage division screen"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_login_with_account_owner(self):
        email = os.environ.get("ACCOUNT_OWNER_LOGIN")
        password = os.environ.get("ACCOUNT_OWNER_PASSWORD")
        assert self.login_page_instance.sign_in(email, password)

    @allure.title("Click on sign in button redirect user to division management screen")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_check_division_dashboard_url(self):
        assert self.login_page_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-divisions"
        )

    @allure.title("Validate cookies consent is present and closed it")
    @allure.severity(allure.severity_level.MINOR)
    def test_03_close_cookies_consent(self):
        assert self.login_page_instance.close_cookies()

    @allure.title(
        "Search for a division by email should show correct result in listing"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_search_for_added_division(self):
        email_id = os.environ.get("DISABLE_DIVISION_EMAIL")
        assert self.dash_page_instance.search_by_email(email_id)

    @allure.title("Clicking on action button should show disable and edit option")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_05_disable_division_details(self):
        assert self.dash_page_instance.click_on_action_butn()

    @allure.title("Clicking on disable button should disable the user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_06_click_on_disable_button(self):
        assert self.dash_page_instance.disable_division_details()

    @allure.title(
        "Clicking on disable button should update status from enable to disable"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_check_for_updated_division_details(self):
        assert self.dash_page_instance.check_for_status_name("DISABLED")

    @allure.title("Clicking on sign out should redirect user to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_sign_out(self):
        assert self.login_page_instance.sign_out()


@allure.suite("Manage division screen")
@allure.feature("Login with disable division")
@allure.description("Login with division owner and check for error message")
class DisableAndEnableDivisionClass01(BaseTestClass):
    """Test for Class Home Page"""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_instance = LoginPage(self.driver)
        self.dash_page_instance = ManageDivisionPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_visit_login_page(self):
        self.login_page_instance.go_to_page(os.environ.get("LOGIN_LINK"))

    @allure.title("Login with disabled division owner")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_login_with_division_owner(self):
        email = os.environ.get("DISABLE_DIVISION_EMAIL")
        password = os.environ.get("DISABLE_DIVISION_PASSWORD")
        assert self.login_page_instance.sign_in(email, password)

    @allure.title("For disable division owner, it should show 403 page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_add_new_division(self):
        assert self.dash_page_instance.check_disable_user_login_text(constants.Alert_MESSAGE)


@allure.suite("Manage division screen")
@allure.feature("Enable the disabled division owner from account owner")
@allure.description("Login with account owner and enable division")
class DisableAndEnableDivisionClass02(BaseTestClass):
    """Test for Class Home Page"""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_instance = LoginPage(self.driver)
        self.dash_page_instance = ManageDivisionPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        self.login_page_instance.go_to_page(os.environ.get("LOGIN_LINK"))

    @allure.title(
        "Login with correct account owner credential should redirect user to manage division screen"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_login_with_account_owner(self):
        email = os.environ.get("ACCOUNT_OWNER_LOGIN")
        password = os.environ.get("ACCOUNT_OWNER_PASSWORD")
        assert self.login_page_instance.sign_in(email, password)

    @allure.title("Click on sign in button redirect user to division management screen")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_check_division_dashboard_url(self):
        assert self.login_page_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-divisions"
        )

    @allure.title("Validate cookies consent is present and closed it")
    @allure.severity(allure.severity_level.MINOR)
    def test_03_close_cookies_consent(self):
        assert self.login_page_instance.close_cookies()

    @allure.title(
        "Search for a division by email should show correct result in listing"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_search_for_added_division(self):
        email_id = os.environ.get("DISABLE_DIVISION_EMAIL")
        assert self.dash_page_instance.search_by_email(email_id)

    @allure.title("Clicking on action button should show enable option")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_05_enable_division_details(self):
        assert self.dash_page_instance.click_on_action_butn()

    @allure.title(
        "Clicking on disable button should update status from enable to disable"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_06_enable_disabled_division(self):
        assert self.dash_page_instance.enable_division()

    @allure.title(
        "Clicking on disable button should update status from disable to unable"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_07_check_for_updated_division_details(self):
        assert self.dash_page_instance.check_for_status_name("ACTIVE")

    @allure.title("Clicking on sign out should redirect user to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_sign_out(self):
        assert self.login_page_instance.sign_out()


@allure.suite("Manage division screen")
@allure.feature("Login with enabled division owner")
@allure.description(
    "Login with division owner and check manage advisor page is visible"
)
class DisableAndEnableDivisionClass03(BaseTestClass):

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_instance = LoginPage(self.driver)
        self.dash_page_instance = ManageDivisionPage(self.driver)
        self.adv_manage_page_instance = ManageAdvisorPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_visit_login_page(self):
        self.login_page_instance.go_to_page(os.environ.get("LOGIN_LINK"))

    @allure.title(
        "Login with enabled division owner should redirect to manage advisor page"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_login_with_division_owner(self):
        email = os.environ.get("DISABLE_DIVISION_EMAIL")
        password = os.environ.get("DISABLE_DIVISION_PASSWORD")
        assert self.login_page_instance.sign_in(email, password)

    @allure.title("Click on sign in button redirect user to advisor management screen")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_check_student_dashboard_url(self):
        assert self.login_page_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-advisors"
        )

    @allure.title("Clicking on sounds good button, should close cookies navbar")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_close_cookies_model(self):
        assert self.login_page_instance.close_cookies_model()

    @allure.title("Clicking on sign out should redirect user to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_sign_out(self):
        assert self.login_page_instance.sign_out()

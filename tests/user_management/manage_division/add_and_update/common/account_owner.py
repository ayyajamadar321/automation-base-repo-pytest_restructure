import os
import random
from datetime import datetime
import allure
import pytest
from faker import Faker
from pages.authentication.login_page import LoginPage
from pages.user_management.manage_division_page import ManageDivisionPage
from tests.conftest import BaseTestClass


fake = Faker()
division_name = fake.first_name()
division_number = "0971555" + str(random.randint(1111, 9999))
update_division_name = "Abc" + fake.first_name()
update_division_number = "0987666" + str(random.randint(1111, 9999))
fname = fake.first_name()
lname = fake.last_name()
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
email_id = f"abc.def{now}@ischoolconnect.com"
number = "88" + str(random.randint(10000000, 99999999))


@allure.epic("User Management")
@allure.feature("Create And Update Functionality")
@allure.suite("User Management Account Owner Login")
@allure.description("Test cases for create and update user")
class CreateAndUpdateDivisionOwnerClass(BaseTestClass):
    @pytest.fixture(autouse=True)
    def _setup(self):
        self.user_login_page_instance = LoginPage(self.driver)
        self.div_manage_page_instance = ManageDivisionPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        self.user_login_page_instance.go_to_page(os.environ.get("LOGIN_LINK"))

    @allure.title("`Enter correct email id, password and click on sign in button`")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_login_with_account_owner(self):
        email = os.getenv("ACCOUNT_OWNER_LOGIN")
        password = os.getenv("ACCOUNT_OWNER_PASSWORD")
        assert self.user_login_page_instance.sign_in(email, password)

    @allure.title("Click on sign in button redirect user to advisor management screen")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_check_division_dashboard_url(self):
        assert self.user_login_page_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-divisions"
        )

    @allure.title("Validate cookies consent is present and closed it")
    @allure.severity(allure.severity_level.MINOR)
    def test_03_close_cookies_consent(self):
        assert self.user_login_page_instance.close_cookies()

    @allure.title(
        "Click on add division and enter division name, number,first name, last name, and email"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04_enter_details_in_create_division_model(self):
        assert self.div_manage_page_instance.create_division(
            division_name,
            division_number,
            fname,
            lname,
            email_id,
        )

    @allure.title("Click on save button and check division is created")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_05_click_on_save_button_new_division(self):
        assert self.div_manage_page_instance.click_on_save_button()

    @allure.title("Enter new division email id in search_by")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_06_search_for_newly_added_advisor(self):
        assert self.div_manage_page_instance.search_by_email(email_id)

    @allure.title("Verify division name is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_07_check_for_newly_added_division_name(self):
        assert self.div_manage_page_instance.check_for_division_name(division_name)

    @allure.title("Verify division number is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_08_check_for_newly_added_division_number(self):
        assert self.div_manage_page_instance.check_for_division_number(division_number)

    @allure.title("Verify first name and last name is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_09_check_for_newly_added_division_fname_and_lname(self):
        assert self.div_manage_page_instance.check_for_admin_name(fname, lname)

    @allure.title("Verify email is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_10_check_for_newly_added_division_email(self):
        assert self.div_manage_page_instance.check_for_admin_email(email_id)

    @allure.title("Click on action button and check edit option is visible")
    @allure.severity(allure.severity_level.NORMAL)
    def test_11_open_action_items(self):
        assert self.div_manage_page_instance.click_on_action_butn()

    @allure.title("Click on edit button and check edit model is visible")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_12_open_edit_division_model(self):
        assert self.div_manage_page_instance.click_on_edit_butn()

    @allure.title("Update division name, number and close edit model")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_13_update_division_details(self):
        assert self.div_manage_page_instance.edit_division_details(
            update_division_name, update_division_number
        )

    @allure.title("Search for updated division")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_14_update_division_details(self):
        assert self.div_manage_page_instance.search_by_email(email_id)

    @allure.title("Check division name is updated")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_15_check_for_updated_division_details(self):
        assert self.div_manage_page_instance.check_for_division_name(update_division_name)

    @allure.title("Check division number is updated")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_16_update_division_number(self):
        assert self.div_manage_page_instance.check_for_division_number(update_division_number)

    @allure.title("Check division first and last name is updated")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_17_update_division_firstname_and_lastname(self):
        assert self.div_manage_page_instance.check_for_admin_name(fname, lname)

    @allure.title("Check division email id is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_18_update_division_details(self):
        assert self.div_manage_page_instance.check_for_admin_email(email_id)

    @allure.title("Click on sign out button and user is redirected to login page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_19_sign_out(self):
        assert self.user_login_page_instance.sign_out()

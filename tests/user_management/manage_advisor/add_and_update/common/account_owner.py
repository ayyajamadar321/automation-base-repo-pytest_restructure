import os
import random
from datetime import datetime
import allure
import pytest
from faker import Faker

from pages.authentication.login_page import LoginPage
from pages.user_management.manage_advisor_page import ManageAdvisorPage
from pages.user_management.manage_division_page import ManageDivisionPage
from tests.conftest import BaseTestClass

fake = Faker()
advisor_fname = fake.first_name()
advisor_lname = fake.last_name()
number = "0981234" + str(random.randint(1111, 9999))
updated_number = "0981234" + str(random.randint(1111, 9999))
division_name = "mumbai division"
update_division_name = "hydrabad division"
fname = fake.name()
lname = " Test"
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
email_id = f"abc.def{now}@ischoolconnect.com"


@allure.epic("User Management")
@allure.feature("Create And Update Functionality")
@allure.suite("User Management Account Owner Login")
@allure.description("Test cases for create and update user")
class CreateAndUpdateAdvisorOwnerClass(BaseTestClass):
    @pytest.fixture(autouse=True)
    def _setup(self):
        self.user_login_page_instance = LoginPage(self.driver)
        self.div_manage_page_instance = ManageDivisionPage(self.driver)
        self.adv_manage_page_instance = ManageAdvisorPage(self.driver)

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

    @allure.title("Click on sign in button redirect user to division management screen")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_check_division_dashboard_url(self):
        assert self.user_login_page_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-divisions"
        )

    @allure.title("Validate cookies consent is present and closed it")
    @allure.severity(allure.severity_level.MINOR)
    def test_03_close_cookies_consent(self):
        assert self.user_login_page_instance.close_cookies()

    @allure.title(
        "Clicking on manage advisor icon should redirect to manage advisor page"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04_go_to_manage_advisor_page(self):
        assert self.div_manage_page_instance.go_to_manage_advisor_page()

    @allure.title(
        "Clicking on add advisor should open create advisor model and allow to enter advisor name, number,"
        "first name, last name, email in the model"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_05_enter_details_in_create_advisor_model(self):
        assert self.adv_manage_page_instance.create_advisor(
            advisor_fname, advisor_lname, email_id, number
        )

    @allure.title(
        "Entering new advisor's email id in search_by should show only result related to this email id"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_06_search_for_newly_added_advisor(self):
        assert self.adv_manage_page_instance.search_for_advisor(email_id)

    @allure.title("Verify division name is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_07_check_for_newly_added_division_name(self):
        assert self.adv_manage_page_instance.check_for_division_name()

    @allure.title("Verify advisor number is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_08_check_for_newly_added_advisor_number(self):
        assert self.adv_manage_page_instance.check_for_advisor_number(number)

    @allure.title("Verify first name and last name is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_09_check_for_newly_added_division_fname_and_lname(self):
        assert self.adv_manage_page_instance.check_for_advisor_name(advisor_fname, advisor_lname)

    @allure.title("Verify email is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_10_check_for_newly_added_division_email(self):
        assert self.adv_manage_page_instance.check_for_advisor_email(email_id)

    @allure.title("Clicking on action button and should show edit option ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_11_open_action_items(self):
        assert self.adv_manage_page_instance.click_on_action_butn()

    @allure.title("Clicking on edit button should open edit model")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_12_open_edit_division_model(self):
        assert self.adv_manage_page_instance.click_on_edit_butn()

    @allure.title(
        "Entering firstname, last name , number and division name and clicking on save button should update"
        " and close the edit model"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_13_update_advisor_details(self):
        assert self.adv_manage_page_instance.edit_advisor_details(
            fname, lname, updated_number, update_division_name
        )

    @allure.title(
        "Entering updated advisor's email id in search_by should show only result related to this email id"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_14_update_division_details(self):
        assert self.adv_manage_page_instance.search_for_advisor(email_id)

    @allure.title("Validate updated advisor's name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_15_check_for_updated_division_details(self):
        assert self.adv_manage_page_instance.check_for_division_name()

    @allure.title("Validate updated advisor's number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_16_update_division_number(self):
        assert self.adv_manage_page_instance.check_for_advisor_number(updated_number)

    @allure.title("validate updated advisor's first and last name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_17_update_division_firstname_and_lastname(self):
        assert self.adv_manage_page_instance.check_for_advisor_name(fname, lname)

    @allure.title("validate updated advisor's email id")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_18_update_division_details(self):
        assert self.adv_manage_page_instance.check_for_advisor_email(email_id)

    @allure.title("Click on sign out button and user is redirected to login page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_19_sign_out(self):
        assert self.user_login_page_instance.sign_out()

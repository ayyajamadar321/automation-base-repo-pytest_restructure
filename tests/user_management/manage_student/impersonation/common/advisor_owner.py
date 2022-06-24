import os
import random
from datetime import datetime
import allure
import pytest
from faker import Faker

import constants
from pages.authentication.login_page import LoginPage
from pages.user_management.manage_student_page import ManageStudentPage
from tests.conftest import BaseTestClass


@allure.epic("User Management")
@allure.feature("Impersonation")
@allure.suite("User Management Advisor Owner Login")
@allure.description("Test cases for impersonation")
class ImpersonateStudentClass(BaseTestClass):
    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.manage_student_instance = ManageStudentPage(self.driver)

    fake = Faker()
    fname = fake.first_name()
    lname = fake.last_name()
    stud_number = "0987654" + str(random.randint(1111, 9999))
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    email = f"stu.dent{now}@ischoolconnect.com"
    identifier = fake.word()
    wrong_phone_number = "098765"
    wrong_identifier = "abc xyz"

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

    @allure.title("Click on sign with correct email id, password should reflect to student dashboard")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_enter_correct_credentials(self):
        email = os.environ.get("AUTOMATION_ADVISOR_LOGIN")
        password = os.environ.get("AUTOMATION_ADVISOR_PASSWORD")
        self.login_page_tab_instance.refresh()
        assert self.login_page_tab_instance.sign_in(email, password)

    @allure.title("Click on sign in button should redirect to student screen")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04_check_manage_student_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-students"
        )

    @allure.title("Clicking on close button should close the cookies consent")
    @allure.severity(allure.severity_level.MINOR)
    def test_05_close_cookies_consent(self):
        assert self.login_page_tab_instance.close_cookies_model()

    @allure.title("Search newly created student using email id should show student below")
    @allure.severity(allure.severity_level.MINOR)
    def test_06_search_for_existing_student(self):
        assert self.manage_student_instance.search_for_student(constants.STUD_PROFILE_EMAIL)

    @allure.title("Click on the action button should  open option modal")
    @allure.severity(allure.severity_level.MINOR)
    def test_07_click_on_action_button(self):
        assert self.manage_student_instance.click_on_action_button()

    @allure.title("Click on impersonation button should open impersonation modal")
    @allure.severity(allure.severity_level.MINOR)
    def test_08_click_on_the_impersonation_button(self):
        assert self.manage_student_instance.click_on_impersonate_button()

    @allure.title("Click on OK button should redirect to student dashboard")
    @allure.severity(allure.severity_level.MINOR)
    def test_09_click_ok_button_impersonation_model(self):
        assert self.manage_student_instance.ok_button_impersonate_model()

    @allure.title("Validate student dashboard screen url is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_10_check_division_dashboard_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("STUDENT_DASHBOARD_BASE_URL")
        )

    @allure.title("Click on return to impersonation should redirect to advisor dashboard")
    @allure.severity(allure.severity_level.MINOR)
    def test_11_click_on_return_to_impersonation(self):
        assert self.manage_student_instance.click_on_return_to_impersonate_button()

    @allure.title("Validate students management screen url is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_12_check_student_dashboard_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-students"
        )

    @allure.title("Clicking on sign out button should redirect to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_13_sign_out(self):
        assert self.login_page_tab_instance.sign_out()

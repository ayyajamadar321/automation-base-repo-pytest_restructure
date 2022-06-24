import os
import random
from datetime import datetime
import allure
import pytest
from faker import Faker
from pages.authentication.login_page import LoginPage
from pages.user_management.manage_student_page import ManageStudentPage
from tests.conftest import BaseTestClass


@allure.epic("User Management")
@allure.feature("Access level")
@allure.suite("User Management Advisor Owner Login")
@allure.description("Test cases for access level")
class ChangeAccessStudentClass(BaseTestClass):
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

    @allure.title(
        "Clicking on add student button should open student form. Fill all the details and click on the create"
        "should create new student"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_create_student(self):
        assert self.manage_student_instance.create_student_without_advisor(
            self.fname, self.lname, self.email, self.stud_number, self.identifier
        )

    @allure.title("Search newly created student using email id should show student below")
    @allure.severity(allure.severity_level.MINOR)
    def test_07_search_for_newly_added_student(self):
        assert self.manage_student_instance.search_for_student(self.email)

    @allure.title("Click on the action button should  open option modal")
    @allure.severity(allure.severity_level.MINOR)
    def test_08_click_on_action_button(self):
        assert self.manage_student_instance.click_on_action_button()

    @allure.title("Click on the change access level button should open access level dropdown")
    @allure.severity(allure.severity_level.MINOR)
    def test_09_click_on_change_access_level(self):
        assert self.manage_student_instance.click_on_change_access_level_button()

    @allure.title("Drop down should show all the access levels")
    @allure.severity(allure.severity_level.MINOR)
    def test_10_click_on_access_level_drop_down(self):
        assert self.manage_student_instance.click_on_change_access_level_dropdown()

    @allure.title("Search new access level should show searched access level")
    @allure.severity(allure.severity_level.MINOR)
    def test_11_choose_access_level(self):
        assert self.manage_student_instance.choose_other_access_level()

    @allure.title("Click on save button popup should appear")
    @allure.severity(allure.severity_level.MINOR)
    def test_12_click_on_save_button(self):
        assert self.manage_student_instance.click_on_change_access_level_save_button()

    @allure.title("Validate access level changed successfully")
    @allure.severity(allure.severity_level.MINOR)
    def test_13_validate_access_level(self):
        assert self.manage_student_instance.validate_access_level_text()

    @allure.title("Clicking on sign out button should redirect to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_14_sign_out(self):
        assert self.login_page_tab_instance.sign_out()

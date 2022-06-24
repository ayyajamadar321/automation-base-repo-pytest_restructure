import os
import allure
import pytest

import constants
from pages.authentication.login_page import LoginPage
from pages.recommendations_engine.recommandation_wizard_page import RecommendationWizardPage
from pages.recommendations_engine.recommendation_page import RecommendationCoursePage
from pages.recommendations_engine.recommendation_report_page import RecommendationReportPage
from tests.conftest import BaseTestClass


@allure.epic("Recommendation")
@allure.feature("Edit Recommendations")
@allure.suite("Recommendation Advisor Login")
@allure.description("Test cases for edit recommendations")
class AdvisorOwnerEditRecommendationsClass(BaseTestClass):

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.recommendation_course_instance = RecommendationCoursePage(self.driver)
        self.recommendation_wizard_instance = RecommendationWizardPage(self.driver)
        self.recommendation_report_instance = RecommendationReportPage(self.driver)

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        link = os.getenv("LOGIN_LINK")
        print(link)
        self.login_page_tab_instance.go_to_page(link)

    @allure.title("Validate student url")
    @allure.severity(allure.severity_level.MINOR)
    def test_01_url_displayed_properly(self):
        assert self.login_page_tab_instance.get_current_url()

    @allure.title("Entering correct email id, password and click on sign in button should "
                  "redirect to student dashboard")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_enter_correct_credentials(self):
        email = os.getenv("AUTOMATION_ADVISOR_LOGIN")
        password = os.getenv("AUTOMATION_ADVISOR_PASSWORD")
        self.login_page_tab_instance.refresh()
        assert self.login_page_tab_instance.sign_in(email, password)

    @allure.title("Validate student dashboard screen url")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_check_student_dashboard_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-students"
        )

    @allure.title("Clicking on close button should close cookies consent")
    @allure.severity(allure.severity_level.MINOR)
    def test_04_close_cookies_consent(self):
        assert self.login_page_tab_instance.close_cookies_model()

    @allure.title("Clicking on recommendation button should reflect to recommendation search_by")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_check_recommendations_button(self):
        assert self.recommendation_course_instance.click_on_recommendations_button()

    @allure.title("Entering invalid email id in email input should show error")
    @allure.severity(allure.severity_level.MINOR)
    def test_06_check_error_message_for_invalid_email(self):
        assert self.recommendation_course_instance.text_input_recommendations(constants.INVALID_LOGIN)
        assert self.recommendation_wizard_instance.check_invalid_email_error_message()

    @allure.title("Entering valid email id in email input and click on the start recommendations should redirect to "
                  "recommendation wizard")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_check_text_field_recommendations(self):
        self.login_page_tab_instance.refresh()
        assert self.recommendation_course_instance.text_input_recommendations(constants.STUD_PROFILE_EMAIL)
        assert (
            self.recommendation_course_instance.click_on_start_recommendations_button()
        )

    @allure.title("Validate recommendations report screen url")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_08_check_student_dashboard_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "recommend-courses/report"
        )

    @allure.title("Clicking on view recommendations should redirect to recommendations report screen url")
    @allure.severity(allure.severity_level.NORMAL)
    def test_09_check_verify_recommendations_courses(self):
        assert self.recommendation_report_instance.check_for_dream_bucket_text_output()
        assert self.recommendation_report_instance.check_for_output_university_course()

    @allure.title("Clicking on edit recommendation should open edit recommendation modal")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_check_on_edit_recommendations(self):
        assert self.recommendation_report_instance.click_on_edit_button()

    @allure.title("Clicking on ok button should user able to add or delete the university")
    @allure.severity(allure.severity_level.NORMAL)
    def test_11_check_on_edit_recommendations_ok_btn(self):
        assert self.recommendation_report_instance.click_on_edit_ok_button()

    @allure.title("Clicking on delete button should feedback modal")
    @allure.severity(allure.severity_level.NORMAL)
    def test_12_check_delete_btn(self):
        assert self.recommendation_report_instance.click_on_delete_button()

    @allure.title("Clicking on dropdown should open dropdown options")
    @allure.severity(allure.severity_level.NORMAL)
    def test_13_check_feedback_field(self):
        assert self.recommendation_report_instance.click_on_feedback_field()

    @allure.title("Clicking on save button should save feedback")
    @allure.severity(allure.severity_level.NORMAL)
    def test_14_check_save_feedback_button(self):
        assert self.recommendation_report_instance.click_on_feedback_save_button()

    @allure.title("Clicking on save button should save all edited recommendations")
    @allure.severity(allure.severity_level.NORMAL)
    def test_15_click_on_save_button(self):
        assert self.recommendation_report_instance.click_on_save_button()

    @allure.title("Clicking on sign out button should redirect to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_16_sign_out(self):
        assert self.login_page_tab_instance.sign_out()
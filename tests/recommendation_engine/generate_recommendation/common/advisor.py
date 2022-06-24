import os
import random
import allure
import constants
import pytest
from pages.authentication.login_page import LoginPage
from pages.recommendations_engine.kaplan_reco_page import KaplanRecoPage
from pages.recommendations_engine.recommandation_wizard_page import (
    RecommendationWizardPage,
)
from pages.recommendations_engine.recommendation_page import RecommendationCoursePage
from pages.recommendations_engine.recommendation_report_page import RecommendationReportPage
from tests.conftest import BaseTestClass


@allure.epic("Recommendation")
@allure.feature("Generate Recommendations")
@allure.suite("Recommendation Advisor Login")
@allure.description("Test cases for generate recommendations")
class AdvisorOwnerRecommendationsClass(BaseTestClass):

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.recommendation_course_instance = RecommendationCoursePage(self.driver)
        self.recommendation_wizard_instance = RecommendationWizardPage(self.driver)
        self.recommendation_report_instance = RecommendationReportPage(self.driver)
        self.kaplan_recommendation_wizard_instance = KaplanRecoPage(self.driver)

    email = "abc" + str(random.randint(1111, 9999)) + "@qwert.com"
    num = str(random.randint(1, 4))
    Specialization = ["Computer Science", "Computer Programing"]

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=0)
    def test_00_visit_login_page(self):
        link = os.getenv("LOGIN_LINK")
        print(link)
        self.login_page_tab_instance.go_to_page(link)

    @allure.title("Validating student url")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=1)
    def test_01_url_displayed_properly(self):
        method_list = [method for method in dir(AdvisorOwnerRecommendationsClass) if method.startswith('__') is False]
        print(method_list)
        assert self.login_page_tab_instance.get_current_url()

    @allure.title("Entering correct email id, password and click on sign in button should "
                  "redirect to student dashboard")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=2)
    def test_02_enter_correct_credentials(self):
        email = os.getenv("ADVISOR_LOGIN")
        password = os.getenv("ADVISOR_PASSWORD")
        self.login_page_tab_instance.refresh()
        assert self.login_page_tab_instance.sign_in(email, password)

    @allure.title("Validating student dashboard screen url")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=3)
    def test_03_check_student_dashboard_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("MANAGE_USER_BASE_URL") + "manage-students"
        )

    @allure.title("Clicking on close button should close cookies consent")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=4)
    def test_04_close_cookies_consent(self):
        assert self.login_page_tab_instance.close_cookies_model()

    @allure.title("Clicking on recommendation button should reflect to recommendation search_by")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=5)
    def test_05_check_recommendations_button(self):
        assert self.recommendation_course_instance.click_on_recommendations_button()

    @allure.title("Entering invalid email id in email input should show error")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=6)
    def test_06_check_error_message_for_invalid_email(self):
        assert self.recommendation_course_instance.text_input_recommendations(constants.INVALID_LOGIN)
        assert self.recommendation_wizard_instance.check_invalid_email_error_message()

    @allure.title("Entering valid email id in email input and click on the start recommendations should redirect to "
                  "generate recommendation button")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=7)
    def test_07_check_text_field_recommendations(self):
        self.login_page_tab_instance.refresh()
        assert self.recommendation_course_instance.text_input_recommendations(self.email)

    @allure.title(
        "Clicking on generate recommendations should redirect to recommendation wizard")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=8)
    def test_08_check_start_and_generate_recommendations(self):
        assert self.recommendation_course_instance.click_on_start_recommendations_button()
        assert self.recommendation_wizard_instance.click_on_generate_recommendations()

    @allure.title("Clicking on the Year and Season should get selected respectively")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=12)
    def test_12_choose_year_and_season(self):
        assert self.recommendation_wizard_instance.click_on_year()
        assert self.recommendation_wizard_instance.click_on_season()

    @allure.title("Clicking on sign out button should redirected to login page")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=25)
    def test_25_sign_out(self):
        assert self.login_page_tab_instance.sign_out()

import os
import random
import allure
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
@allure.suite("Recommendation Student Login")
@allure.description("Test cases for generate recommendations")
class StudentRecommendationsClass(BaseTestClass):

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.login_page_tab_instance = LoginPage(self.driver)
        self.recommendation_course_instance = RecommendationCoursePage(self.driver)
        self.recommendation_wizard_instance = RecommendationWizardPage(self.driver)
        self.recommendation_report_instance = RecommendationReportPage(self.driver)
        self.kaplan_recommendation_wizard_instance = KaplanRecoPage(self.driver)

    email = "abc" + str(random.randint(1111, 9999)) + "@qwert.com"
    num = str(random.randint(1, 4))
    Specialization = ["Agricultural Engineering", "Agricultural Science"]

    @allure.title("Go to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_00_visit_login_page(self):
        link = os.getenv("STUDENT_LOGIN_LINK")
        print(link)
        self.login_page_tab_instance.go_to_page(link)

    @allure.title("Validate student url")
    @allure.severity(allure.severity_level.MINOR)
    def test_01_url_displayed_properly(self):
        assert self.login_page_tab_instance.get_current_url()

    @allure.title("Entering correct email id, password and click on sign in button "
                  "should redirect to student dashboard")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_enter_correct_credentials(self):
        email = os.getenv("STUDENT_LOGIN")
        password = os.getenv("STUDENT_PASSWORD")
        self.login_page_tab_instance.refresh()
        assert self.login_page_tab_instance.sign_in(email, password)

    @allure.title("Validate student dashboard screen url")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_check_student_dashboard_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(os.getenv("STUDENT_DASHBOARD_BASE_URL"))

    @allure.title("Clicking on close button should close cookies consent")
    @allure.severity(allure.severity_level.MINOR)
    def test_04_close_cookies_consent(self):
        assert self.login_page_tab_instance.close_cookies_model()

    @allure.title("Clicking on recommendation button should reflect to recommendation search_by")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_click_on_recommendations_button(self):
        assert self.recommendation_course_instance.click_on_student_recommendations_button()

    @allure.title("Clicking on refine profile should redirect user to recommendation wizard page")
    @allure.severity(allure.severity_level.MINOR)
    def test_06_click_on_refine_profile(self):
        assert self.recommendation_course_instance.click_on_refine_profile_button()

    @allure.title("Entering degree in search_by should show degree results")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_select_degree_of_study(self):
        assert self.recommendation_wizard_instance.select_master_degree()

    # @allure.title("Entering specialization in field should show specialization in dropdown")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_08_select_preferred_specialization(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.isc_enter_agriculture_engineering_specialization(
    #             self.Specialization[0])
    #         assert self.recommendation_wizard_instance.isc_enter_agriculture_science_specialization(
    #             self.Specialization[1])
    #     else:
    #         assert self.kaplan_recommendation_wizard_instance.kaplan_enter_agriculture_engineering_specialization(
    #             self.Specialization[0])
    #         assert self.kaplan_recommendation_wizard_instance.kaplan_enter_agriculture_science_specialization(
    #             self.Specialization[1])

    @allure.title("Clicking on the Year and Season should get selected respectively")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_enter_year_and_season(self):
        assert self.recommendation_wizard_instance.click_on_year()
        assert self.recommendation_wizard_instance.click_on_season()

    # @allure.title("Clicking on next button should redirect user to next page")
    # @allure.severity(allure.severity_level.MINOR)
    # def test_11_click_on_next_button(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_next_button()
    #     else:
    #         pass

    # covering below test case in advisor
    # @allure.title("Enter invalid data in the text field should show error message")
    # @allure.severity(allure.severity_level.MINOR)
    # def test_12_check_wrong_score_and_validation(self):
    #     assert self.recommendation_wizard_instance.click_on_isc_GPA_and_validate()
    #     assert self.recommendation_wizard_instance.click_on_CGPA_and_validate()
    #     assert (
    #         self.recommendation_wizard_instance.click_on_percentage_highSchool_score()
    #     )

    # @allure.title("Entering under grad score in input field")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_13_enter_undergrad_score_score(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_isc_undergrad_Score(3.5)
    #     else:
    #         assert self.kaplan_recommendation_wizard_instance.enter_kaplan_undergrad_specialization("Agriculture")
    #         assert self.kaplan_recommendation_wizard_instance.enter_kaplan_undergrad_score(4)

    # @allure.title("Clicking on certifications should open specific certification and number of certification")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_14_check_certifications(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_certifications()
    #     else:
    #         pass

    # @allure.title("clicking on research paper should open appropriate options")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_15_research_paper(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_paper_publications()
    #     else:
    #         pass

    # @allure.title("Clicking on seminar should open appropriate options")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_16_seminar(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_seminar()
    #     else:
    #         pass

    # @allure.title("Clicking on internship should open appropriate options")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_17_internship(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_internship()
    #     else:
    #         pass

    # @allure.title("Clicking on experience should open appropriate options")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_18_work_experience(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_work_experience()
    #     else:
    #         pass

    # @allure.title("Clicking on next button should redirect user to next page")
    # @allure.severity(allure.severity_level.MINOR)
    # def test_19_click_on_next_button(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_next_button()
    #     else:
    #         pass

    # @allure.title("Clicking on aptitude test and entering invalid score should show error message")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_20_check_aptitude_test_and_validate(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_gre_aptitude_test_and_validate(500)
    #         assert self.recommendation_wizard_instance.click_on_gmat_aptitude_test_and_validate(900)
    #         assert self.recommendation_wizard_instance.click_on_no_aptitude_test()
    #     else:
    #         pass

    # @allure.title("Clicking on english proficiency tests and entering invalid score should show error message")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_21_check_proficiency_indicator_test_and_validation(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_isc_ielts_exam(18)
    #         assert self.recommendation_wizard_instance.click_on_isc_toefl_exam(720)
    #         assert self.recommendation_wizard_instance.click_on_isc_cae_exam(259)
    #         assert self.recommendation_wizard_instance.click_on_isc_pit_exam(101)
    #         assert self.recommendation_wizard_instance.click_on_no_exam()
    #     else:
    #         assert self.kaplan_recommendation_wizard_instance.click_on_kaplan_english_test_button()
    #         assert self.kaplan_recommendation_wizard_instance.click_on_kaplan_ielts_exam(15)
    #         assert self.kaplan_recommendation_wizard_instance.click_on_kaplan_toefl_exam(150)
    #         assert self.kaplan_recommendation_wizard_instance.click_on_kaplan_kite_exam(900)
    #         assert self.kaplan_recommendation_wizard_instance.click_on_kaplan_cae_exam(300)
    #         assert self.kaplan_recommendation_wizard_instance.enter_kaplan_ielts_exam_score(9)

    # @allure.title("Clicking on next button should redirect user to next page")
    # @allure.severity(allure.severity_level.MINOR)
    # def test_22_click_on_next_button(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_next_button()
    #     else:
    #         pass

    # @allure.title("Entering invalid data in the budget field should show error message")
    # @allure.severity(allure.severity_level.MINOR)
    # def test_23_check_budget_error_msg(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_budget_field(1500000)
    #         assert self.recommendation_wizard_instance.check_budget_error_message()
    #     else:
    #         assert self.kaplan_recommendation_wizard_instance.click_on_budget_field(1000000)
    #         assert self.kaplan_recommendation_wizard_instance.check_budget_error_message()

    # @allure.title("Enter budget(valid) in budget input field should accept the data")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_24_enter_budget(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.enter_input_in_budget_field(50000)
    #     else:
    #         assert self.kaplan_recommendation_wizard_instance.enter_input_in_budget_field(50000)

    # @allure.title("Clicking on the submit button should reflect to the recommendation result page")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_25_check_submit_button(self):
    #     if os.getenv("CLIENT") == "isc":
    #         assert self.recommendation_wizard_instance.click_on_submit_button()
    #     else:
    #         assert self.kaplan_recommendation_wizard_instance.click_on_submit_button()

    @allure.title("Clicking on submit button should redirect to recommendations report screen url")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_26_check_student_dashboard_url(self):
        assert self.login_page_tab_instance.check_dashboard_url(
            os.getenv("STUDENT_DASHBOARD_BASE_URL") + "/recommend-courses/report"
        )

    @allure.title("Validate recommendation courses")
    @allure.severity(allure.severity_level.NORMAL)
    def test_27_check_verify_recommendations_courses(self):
        assert self.recommendation_report_instance.check_for_dream_bucket_text_output()
        assert self.recommendation_report_instance.check_for_output_agriculture_university_course()

    @allure.title("Click on sign out button should redirected to login page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_28_sign_out(self):
        assert self.login_page_tab_instance.student_sign_out()
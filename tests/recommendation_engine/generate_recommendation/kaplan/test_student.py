import allure

from tests.recommendation_engine.generate_recommendation.common.student import StudentRecommendationsClass


class TestKaplanStudentRecommendationsClass(StudentRecommendationsClass):
    @allure.title("Entering specialization in field should show specialization in dropdown")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_select_preferred_specialization(self):
        assert self.kaplan_recommendation_wizard_instance.kaplan_enter_agriculture_engineering_specialization(
            self.Specialization[0])
        assert self.kaplan_recommendation_wizard_instance.kaplan_enter_agriculture_science_specialization(
            self.Specialization[1])

    @allure.title("Entering under grad score in input field")
    @allure.severity(allure.severity_level.NORMAL)
    def test_13_enter_undergrad_score_score(self):
        assert self.kaplan_recommendation_wizard_instance.enter_kaplan_undergrad_specialization("Agriculture")
        assert self.kaplan_recommendation_wizard_instance.enter_kaplan_undergrad_score(4)

    @allure.title("Clicking on english proficiency tests and entering invalid score should show error message")
    @allure.severity(allure.severity_level.NORMAL)
    def test_21_check_proficiency_indicator_test_and_validation(self):
        assert self.kaplan_recommendation_wizard_instance.click_on_kaplan_english_test_button()
        assert self.kaplan_recommendation_wizard_instance.click_on_kaplan_ielts_exam(15)
        assert self.kaplan_recommendation_wizard_instance.click_on_kaplan_toefl_exam(150)
        assert self.kaplan_recommendation_wizard_instance.click_on_kaplan_kite_exam(900)
        assert self.kaplan_recommendation_wizard_instance.click_on_kaplan_cae_exam(300)
        assert self.kaplan_recommendation_wizard_instance.enter_kaplan_ielts_exam_score(9)

    @allure.title("Entering invalid data in the budget field should show error message")
    @allure.severity(allure.severity_level.MINOR)
    def test_23_check_budget_error_msg(self):
        assert self.kaplan_recommendation_wizard_instance.click_on_budget_field(1000000)
        assert self.kaplan_recommendation_wizard_instance.check_budget_error_message()

    @allure.title("Enter budget(valid) in budget input field should accept the data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_24_enter_budget(self):
        assert self.kaplan_recommendation_wizard_instance.enter_input_in_budget_field(50000)

    @allure.title("Clicking on the submit button should reflect to the recommendation result page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_25_check_submit_button(self):
        assert self.kaplan_recommendation_wizard_instance.click_on_submit_button()

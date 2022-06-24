import os
import allure
import pytest

from tests.recommendation_engine.generate_recommendation.common.advisor import AdvisorOwnerRecommendationsClass


class TestKaplanAdvisorRecommendationsClass(AdvisorOwnerRecommendationsClass):
    @allure.title("Clicking on country of study should get selected")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=9)
    def test_09_select_country_of_study(self):
        assert self.kaplan_recommendation_wizard_instance.click_on_country_of_study()

    @allure.title("Clicking on degree should degree selected")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=10)
    def test_10_select_degree_of_study(self):
        assert self.recommendation_wizard_instance.select_bachelors_degree()

    @allure.title("Entering specialization in field should show specialization in dropdown")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=11)
    def test_11_select_preferred_specialization(self):
        assert self.kaplan_recommendation_wizard_instance.kaplan_enter_computer_science_specialization(
            self.Specialization[0])

    @allure.title("Entering invalid data in the text field should show error message")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=13)
    def test_13_validation_high_school(self):
        assert self.kaplan_recommendation_wizard_instance.click_on_gpa_and_validate("101")
        assert self.kaplan_recommendation_wizard_instance.click_on_cgpa_and_validate()
        assert self.kaplan_recommendation_wizard_instance.click_on_percentage_high_school_score()

    @allure.title("Entering high school score in input field")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=14)
    def test_14_enter_valid_high_school_score(self):
        assert self.kaplan_recommendation_wizard_instance.click_on_kaplan_high_school_Score(4)

    @allure.title("Clicking on the certification should select the appropriate certification")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=15)
    def test_15_click_on_certifications(self):
        assert self.kaplan_recommendation_wizard_instance.click_and_apply_kaplan_level()

    @allure.title("Entering invalid data in the budget field should show error message")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=16)
    def test_16_check_budget_error_msg(self):
        assert self.kaplan_recommendation_wizard_instance.click_on_budget_field(1000000)
        assert self.kaplan_recommendation_wizard_instance.check_budget_error_message()

    @allure.title("Entering budget(valid) in budget input field should accept the data")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=17)
    def test_17_enter_budget(self):
        assert self.kaplan_recommendation_wizard_instance.enter_input_in_budget_field(50000)

    @allure.title("Clicking on the submit button should reflect user to the recommendation result page")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=18)
    def test_18_check_submit_button(self):
        assert self.kaplan_recommendation_wizard_instance.click_on_submit_button()

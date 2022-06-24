import allure
import pytest
from tests.recommendation_engine.generate_recommendation.common.advisor import AdvisorOwnerRecommendationsClass


class TestIscAdvisorRecommendationsClass(AdvisorOwnerRecommendationsClass):

    @allure.title("Clicking on country of study should get selected")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=9)
    def test_09_select_country_of_study(self):
        method_list = [method for method in dir(TestIscAdvisorRecommendationsClass) if method.startswith('__') is False]
        print(method_list)
        assert self.recommendation_wizard_instance.click_on_country_of_study()
        assert self.recommendation_wizard_instance.check_multiple_option_enable_for_country()

    @allure.title("Clicking on degree should degree selected")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=10)
    def test_10_select_degree_of_study(self):
        assert self.recommendation_wizard_instance.select_bachelors_degree()
        assert self.recommendation_wizard_instance.check_option_enable_for_degree()

    @allure.title("Entering specialization in field should show specialization in dropdown")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=11)
    def test_11_select_preferred_specialization(self):
        assert self.recommendation_wizard_instance.isc_enter_computer_science_specialization(self.Specialization[0])

    @allure.title("Clicking on next button should redirect user to next page")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=13)
    def test_13_click_on_next_button(self):
        assert self.recommendation_wizard_instance.click_on_next_button()

    @allure.title("Entering invalid data in the text field should show error message")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=14)
    def test_14_validation_high_school(self):
        assert self.recommendation_wizard_instance.click_on_gpa_and_validate("105")
        assert self.recommendation_wizard_instance.click_on_cgpa_and_validate()
        assert self.recommendation_wizard_instance.click_on_percentage_high_school_score()

    @allure.title("Entering high school score in input field")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=15)
    def test_15_enter_valid_high_school_score(self):
        assert self.recommendation_wizard_instance.click_on_isc_high_school_Score(4)

    @allure.title("Clicking on the certification should select the appropriate certification")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=16)
    def test_16_click_on_certifications(self):
        assert self.recommendation_wizard_instance.click_on_certifications()

    @allure.title("Clicking on next button should redirect user to next page")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=17)
    def test_17_click_on_next_button(self):
        assert self.recommendation_wizard_instance.click_on_next_button()

    @allure.title("Entering invalid data in aptitude test input should show error message")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=18)
    def test_18_check_aptitude_test_and_validate(self):
        assert self.recommendation_wizard_instance.click_on_sat_aptitude_test_and_validate(2000)
        assert self.recommendation_wizard_instance.click_on_act_aptitude_test_and_validate(37)
        assert self.recommendation_wizard_instance.click_on_no_aptitude_test()

    @allure.title("Entering invalid data in proficiency indicator test input field should show error message")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=19)
    def test_19_check_proficiency_indicator_test_and_validation(self):
        assert self.recommendation_wizard_instance.click_on_isc_ielts_exam(15)
        assert self.recommendation_wizard_instance.click_on_isc_toefl_exam(700)
        assert self.recommendation_wizard_instance.click_on_isc_cae_exam(250)
        assert self.recommendation_wizard_instance.click_on_isc_pit_exam(100)
        assert self.recommendation_wizard_instance.click_on_no_exam()

    @allure.title("Clicking on next button should redirect user to next page")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=20)
    def test_20_click_on_next_button(self):
        assert self.recommendation_wizard_instance.click_on_next_button()

    @allure.title("Entering invalid data in the budget field should show error message")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=21)
    def test_21_check_budget_error_msg(self):
        assert self.recommendation_wizard_instance.click_on_budget_field(1500000)
        assert self.recommendation_wizard_instance.check_budget_error_message()

    @allure.title("Entering budget(valid) in budget input field should accept the data")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=22)
    def test_22_enter_budget(self):
        assert self.recommendation_wizard_instance.enter_input_in_budget_field(50000)

    @allure.title("Clicking on the submit button should reflect user to the recommendation result page")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=23)
    def test_23_check_submit_button(self):
        assert self.recommendation_wizard_instance.click_on_submit_button()

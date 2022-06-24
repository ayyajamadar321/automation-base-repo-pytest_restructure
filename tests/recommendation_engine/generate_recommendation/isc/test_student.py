import allure

from tests.recommendation_engine.generate_recommendation.common.student import StudentRecommendationsClass


class TestIscStudentRecommendationsClass(StudentRecommendationsClass):
    @allure.title("Entering specialization in field should show specialization in dropdown")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_select_preferred_specialization(self):
        assert self.recommendation_wizard_instance.isc_enter_agriculture_engineering_specialization(
            self.Specialization[0])
        assert self.recommendation_wizard_instance.isc_enter_agriculture_science_specialization(
            self.Specialization[1])

    @allure.title("Clicking on next button should redirect user to next page")
    @allure.severity(allure.severity_level.MINOR)
    def test_11_click_on_next_button(self):
        assert self.recommendation_wizard_instance.click_on_next_button()

    @allure.title("Entering under grad score in input field")
    @allure.severity(allure.severity_level.NORMAL)
    def test_13_enter_undergrad_score_score(self):
        assert self.recommendation_wizard_instance.click_on_isc_undergrad_Score(3.5)

    @allure.title("Clicking on certifications should open specific certification and number of certification")
    @allure.severity(allure.severity_level.NORMAL)
    def test_14_check_certifications(self):
        assert self.recommendation_wizard_instance.click_on_certifications()

    @allure.title("clicking on research paper should open appropriate options")
    @allure.severity(allure.severity_level.NORMAL)
    def test_15_research_paper(self):
        assert self.recommendation_wizard_instance.click_on_paper_publications()

    @allure.title("Clicking on seminar should open appropriate options")
    @allure.severity(allure.severity_level.NORMAL)
    def test_16_seminar(self):
        assert self.recommendation_wizard_instance.click_on_seminar()

    @allure.title("Clicking on internship should open appropriate options")
    @allure.severity(allure.severity_level.NORMAL)
    def test_17_internship(self):
        assert self.recommendation_wizard_instance.click_on_internship()

    @allure.title("Clicking on experience should open appropriate options")
    @allure.severity(allure.severity_level.NORMAL)
    def test_18_work_experience(self):
        assert self.recommendation_wizard_instance.click_on_work_experience()

    @allure.title("Clicking on next button should redirect user to next page")
    @allure.severity(allure.severity_level.MINOR)
    def test_19_click_on_next_button(self):
        assert self.recommendation_wizard_instance.click_on_next_button()

    @allure.title("Clicking on aptitude test and entering invalid score should show error message")
    @allure.severity(allure.severity_level.NORMAL)
    def test_20_check_aptitude_test_and_validate(self):
        assert self.recommendation_wizard_instance.click_on_gre_aptitude_test_and_validate(500)
        assert self.recommendation_wizard_instance.click_on_gmat_aptitude_test_and_validate(900)
        assert self.recommendation_wizard_instance.click_on_no_aptitude_test()

    @allure.title("Clicking on english proficiency tests and entering invalid score should show error message")
    @allure.severity(allure.severity_level.NORMAL)
    def test_21_check_proficiency_indicator_test_and_validation(self):
        assert self.recommendation_wizard_instance.click_on_isc_ielts_exam(18)
        assert self.recommendation_wizard_instance.click_on_isc_toefl_exam(720)
        assert self.recommendation_wizard_instance.click_on_isc_cae_exam(259)
        assert self.recommendation_wizard_instance.click_on_isc_pit_exam(101)
        assert self.recommendation_wizard_instance.click_on_no_exam()

    @allure.title("Clicking on next button should redirect user to next page")
    @allure.severity(allure.severity_level.MINOR)
    def test_22_click_on_next_button(self):
        assert self.recommendation_wizard_instance.click_on_next_button()

    @allure.title("Entering invalid data in the budget field should show error message")
    @allure.severity(allure.severity_level.MINOR)
    def test_23_check_budget_error_msg(self):
        assert self.recommendation_wizard_instance.click_on_budget_field(1500000)
        assert self.recommendation_wizard_instance.check_budget_error_message()

    @allure.title("Enter budget(valid) in budget input field should accept the data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_24_enter_budget(self):
        assert self.recommendation_wizard_instance.enter_input_in_budget_field(50000)

    @allure.title("Clicking on the submit button should reflect to the recommendation result page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_25_check_submit_button(self):
        assert self.recommendation_wizard_instance.click_on_submit_button()
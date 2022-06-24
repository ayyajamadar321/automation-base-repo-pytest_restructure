import time
from selenium.webdriver.common.by import By
import constants
from pages.base_page import BasePage


class RecommendationCoursePage(BasePage):
    _RECOMMENDATIONS_LOCATOR = (
        By.CSS_SELECTOR,
        '[href="/dashboard/recommend-courses/search"]',
    )
    _STUDENT_RECOMMENDATIONS_LOCATOR = (By.LINK_TEXT, "Recommendations")
    _REFINE_PROFILE_LOCATOR = (By.CSS_SELECTOR, "#refine_profile_button i")
    _SEARCH_USER_INPUT_RECOMMENDATIONS_LOCATOR = (By.CSS_SELECTOR, "#student_email")
    _START_RECOMMENDATIONS_LOCATOR = (
        By.CSS_SELECTOR,
        'button[color="primary"]',
    )
    _CHECK_RESULT_UNIVERSITY_LOCATOR = (
        By.XPATH,
        "//span[contains(text(),'Pace University')]",
    )
    _CHECK_DREAM_TEXT_LOCATOR = (By.CSS_SELECTOR, '[class="title text-dream"]')
    _CHECK_SAFE_TEXT_LOCATOR = (By.CSS_SELECTOR, '[class="title text-safe"]')

    def click_on_recommendations_button(self):
        return self.click_on_element(self._RECOMMENDATIONS_LOCATOR)

    def text_input_recommendations(self, email):
        time.sleep(2)
        return self.enter_field_input(
            self._SEARCH_USER_INPUT_RECOMMENDATIONS_LOCATOR, email
        )

    def click_on_start_recommendations_button(self):
        time.sleep(5)
        return self.click_on_element(self._START_RECOMMENDATIONS_LOCATOR)

    def check_for_dream_text(self):
        time.sleep(2)
        a = self.get_text_of_elements(self._CHECK_DREAM_TEXT_LOCATOR)
        print(self.convert_list_to_string(a))
        res1 = self.convert_list_to_string(a) == constants.DREAM_BUCKET
        return res1

    def check_for_safe_text(self):
        self.scroll_into_view(self._CHECK_SAFE_TEXT_LOCATOR)
        a = self.get_text_of_elements(self._CHECK_SAFE_TEXT_LOCATOR)
        print(self.convert_list_to_string(a))
        res1 = self.convert_list_to_string(a) == constants.SAFE_BUCKET
        return res1

    '''Student reco'''

    def click_on_student_recommendations_button(self):
        return self.click_on_element(self._STUDENT_RECOMMENDATIONS_LOCATOR)

    def click_on_refine_profile_button(self):
        return self.click_on_element(self._REFINE_PROFILE_LOCATOR)

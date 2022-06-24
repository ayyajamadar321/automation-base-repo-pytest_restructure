"""
__________________________________________________
Base Page that provides basic page functionality
__________________________________________________
"""
import logging
import os
import random
import time
from random import randint

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from urllib3.connectionpool import xrange

logger = logging.getLogger("automation")
logger.setLevel(logging.DEBUG)


class BasePage:
    EXIT_PATH_URL = ""
    _timeout = 50
    _COMPANY_LOGO_LOCATOR = (By.CSS_SELECTOR, "img.header-logo")
    _ALL_CDN_SCRIPT_LOGOS_LOCATOR = (By.CSS_SELECTOR, "script[src]")
    _FOCUS_TAG_LOCATOR = (By.CSS_SELECTOR, "body")
    _LOCATOR = (By.CSS_SELECTOR, 'div[class*="row"]')
    _LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'a[href^="/login/"]')
    _LEADING_MODAL_CLOSE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button.leadinModal-close")
    _SOUNDS_GOOD_BUTN_LOCATOR = (
        By.XPATH,
        "/html/body/div[1]/div/a",
    )
    _LANDING_PAGE_SOUNDS_GOOD_BUTN_LOCATOR = (
        By.CSS_SELECTOR,
        "body > div:nth-child(1) div a",
    )

    def __init__(self, *args):
        self.selenium = args[0]

    def is_isc_logo_displayed(self):
        """Check to see if main logo is available"""
        return self.check_page_element(self._COMPANY_LOGO_LOCATOR)

    def is_current_page(self):
        """Checks if the currently opened page is as expected"""
        try:
            WebDriverWait(self.selenium, self._timeout).until(
                EC.presence_of_all_elements_located(self._ALL_CDN_SCRIPT_LOGOS_LOCATOR)
            )
            elem_js = EC.presence_of_all_elements_located(
                self._ALL_CDN_SCRIPT_LOGOS_LOCATOR
            ).__call__(self.selenium)
            for each_js in elem_js:
                logger.debug(
                    "ELEM JS IS %s %s",
                    str(each_js.tag_name),
                    str(each_js.get_attribute("src")),
                )
            return True
        except AssertionError as exc:
            print("EXC : ", exc)
        return False

    def go_to_page(self, link):
        """Instructs webdriver make a GET request to the page URL.
        This method is blocking until the entire page loads.
        """
        return self.selenium.get(link)

    def refresh(self):
        self.selenium.refresh()

    def maximize(self):
        self.selenium.maximize_window()

    def go_to(self, path):
        self.selenium.get(path)

    def get_current_url(self,):
        url = self.selenium.current_url
        print(url)
        # url = url[url.find(".com/") + 4:]
        # print("Getting the url= ", url)
        return url

    def browser_title(self):
        """Returns the title of the browser window after page load."""
        WebDriverWait(self.selenium, self._timeout).until(lambda s: self.selenium.title)
        return self.selenium.title

    def get_page_source(self, locator=_FOCUS_TAG_LOCATOR):
        """Returns the text contained within the locator tag."""
        # String of element[0]
        return str(self.get_text_of_elements(locator)[0])

    def click_on_element(self, locator=None, index=None):
        """Generic function for clicking elements. (Range index version)"""
        click_result = False
        try:
            WebDriverWait(self.selenium, self._timeout).until(
                EC.presence_of_element_located(locator)
            )
            WebDriverWait(self.selenium, self._timeout).until(
                EC.element_to_be_clickable(locator)
            )
            button_link = self.selenium.find_elements(*locator)
            if index is None:
                if len(button_link) > 1:
                    index = randint(0, len(button_link) - 1)
                else:
                    index = 0
            time.sleep(0.5)
            self.get_text_of_elements()
            button_link[index].click()
            click_result = True
            return click_result
        finally:
            print()

    def get_length_of_element(self, locator=None):
        """Generic function to get the count of occurance of an element"""
        try:
            WebDriverWait(self.selenium, self._timeout).until(
                EC.presence_of_element_located(locator)
            )
            button_link = self.selenium.find_elements(*locator)
            length_of_element = len(button_link)
            return length_of_element
        finally:
            print()

    def click_on_non_click_able(self, locator=_FOCUS_TAG_LOCATOR, index=None):
        click_result = False
        try:
            WebDriverWait(self.selenium, self._timeout).until(
                EC.presence_of_element_located(locator)
            )
            time.sleep(0.3)
            button_link = self.selenium.find_elements(*locator)
            if index is None:
                if len(button_link) > 1:
                    index = randint(0, len(button_link) - 1)
                else:
                    index = 0
            clicker = button_link[index]
            time.sleep(1)
            clicker.click()
            click_result = True
            return click_result
        finally:
            print(click_result)

    def send_enter_keys_to_element(self, locator=None, index=None):
        """Specialized function for clicking elements. (Range index Enter version)"""
        click_result = False
        try:
            WebDriverWait(self.selenium, self._timeout).until(
                EC.presence_of_element_located(locator)
            )
            WebDriverWait(self.selenium, self._timeout).until(
                EC.visibility_of_element_located(locator)
            )
            button_link = self.selenium.find_elements(*locator)
            if index is None:
                if len(button_link) > 1:
                    index = randint(0, len(button_link) - 1)
                else:
                    index = 0
            #
            #     POSSIBLE COMBINATIONS OF CLICKING
            #
            # self.selenium.find_element(*self._FOCUS_TAG_LOCATOR).click()
            # self.selenium.find_element(*self._FOCUS_TAG_LOCATOR).send_keys(Keys.ENTER)
            # self.selenium.find_element(*self._FOCUS_TAG_LOCATOR).send_keys(Keys.RETURN)
            # self.selenium.find_element(*self._FOCUS_TAG_LOCATOR).send_keys("\n")
            # self.selenium.find_element(*self._FOCUS_TAG_LOCATOR).send_keys(Keys.CONTROL+Keys.RETURN)
            # self.selenium.find_element(*self._FOCUS_TAG_LOCATOR).send_keys(Keys.CONTROL+Keys.ENTER)
            time.sleep(0.6)
            button_link[index].send_keys(Keys.ENTER)
            click_result = True
            return click_result
        finally:
            print(click_result)

    def select_from_drop_down(
        self,
        list_option_locator=_FOCUS_TAG_LOCATOR,
        list_option_attribute="class",
        index=None,
    ):
        """
        Method 2 select option from Dropdown & return selection attribute
        """
        element_ids = None
        try:
            self.check_page_element(list_option_locator)
            element_ids = self.get_attribute_of_elements(
                list_option_locator, list_option_attribute
            )
            if index is None:
                if len(element_ids) > 1:
                    index = randint(0, len(element_ids) - 1)
                else:
                    index = 0
            if len(element_ids) > 0:
                self.click_on_non_click_able(list_option_locator, index)
                return element_ids[index]
        finally:
            print(element_ids[index])

    def enter_field_input(
        self, input_locator=_FOCUS_TAG_LOCATOR, values="No Input", index=None
    ):
        """Generic Input function to enter passed values into field element"""
        fill_result = False
        try:
            WebDriverWait(self.selenium, self._timeout).until(
                EC.presence_of_element_located(input_locator)
            )  # Present?
            WebDriverWait(self.selenium, self._timeout).until(
                EC.visibility_of_element_located(input_locator)
            )  # Visible?
            name_field = self.selenium.find_elements(*input_locator)
            if index is None:
                if len(name_field) > 1:
                    index = randint(0, len(name_field) - 1)
                else:
                    index = 0
            time.sleep(0.9)
            name_field[index].send_keys(Keys.CONTROL + "a")
            name_field[index].send_keys(Keys.BACKSPACE)
            name_field[index].send_keys(str(values))
            fill_result = True
            return fill_result
        except AssertionError as e:
            print("\n Got exception, which is apparently : ")
            print("\n", e)
        finally:
            print(fill_result)
        return fill_result

    def enter_multiple_field_input(
        self,
        input_locator=_LOCATOR,
        values="",
        key_action=None,
    ):
        """Generic Form-field Input function
        To enter passed values into given selected fields
        """
        input_field = None
        ipf_length = 0
        try:
            WebDriverWait(self.selenium, self._timeout).until(
                EC.presence_of_element_located(input_locator)
            )  # Present?
            WebDriverWait(self.selenium, self._timeout).until(
                EC.element_to_be_clickable(input_locator)
            )  # Clickable?
            input_field = self.selenium.find_elements(*input_locator)
            if input_field is not None:
                ipf_length = len(input_field)
                for i in range(ipf_length):
                    input_field[i].send_keys(Keys.CONTROL + "a")
                    input_field[i].send_keys(Keys.BACKSPACE)
                    input_field[i].send_keys(values[i])
                    if key_action:
                        time.sleep(0.5)
                        input_field[i].send_keys(key_action)
                        return values[:ipf_length]
        finally:
            print(values[:ipf_length])
        return values[:ipf_length]

    def get_text_of_elements(self, locator=_FOCUS_TAG_LOCATOR):
        """Returns list of text of element/s"""
        WebDriverWait(self.selenium, self._timeout).until(
            EC.presence_of_element_located(locator)
        )
        WebDriverWait(self.selenium, self._timeout).until(
            EC.visibility_of_element_located(locator)
        )
        time.sleep(0.5)
        element = self.selenium.find_elements(*locator)
        if element is not None:
            element_texts = [elem.text for elem in element]

            return element_texts

    def get_attribute_of_elements(
        self, locator=_FOCUS_TAG_LOCATOR, attribute_name="class"
    ):
        WebDriverWait(self.selenium, self._timeout).until(
            EC.presence_of_element_located(locator)
        )
        time.sleep(0.2)
        elements = self.selenium.find_elements(*locator)
        element_attributes = [elem.get_attribute(attribute_name) for elem in elements]
        return element_attributes

    def get_page_element(self, locator=_FOCUS_TAG_LOCATOR):
        WebDriverWait(self.selenium, self._timeout).until(
            EC.presence_of_element_located(locator)
        )
        self.wait_it_out(2)
        web_element = self.selenium.find_element(*locator)
        return web_element

    def get_page_elements(self, locator=_FOCUS_TAG_LOCATOR):
        WebDriverWait(self.selenium, self._timeout).until(
            EC.presence_of_element_located(locator)
        )
        self.wait_it_out(2)
        web_elements = self.selenium.find_elements(*locator)
        return web_elements

    def check_page_element(self, locator=_LOCATOR, timeout=None):
        """Check to see if given WebElement is in place, present and visible"""
        check_result = False
        try:
            if timeout is None:
                timeout = self._timeout
            WebDriverWait(self.selenium, timeout).until(
                EC.presence_of_element_located(locator)
            )
            WebDriverWait(self.selenium, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.wait_it_out(3)
            element = self.selenium.find_element(*locator)
            if element is not None:
                if element.tag_name is not None:
                    if element.text is not None:
                        check_result = True
                        return check_result
            return check_result
        finally:
            print(check_result)

    def click_on_back_button(self):
        self.selenium.back()

    def check_same_page_link_works(
        self,
        sp_link_locator=None,
        required_string="https://ischoolconnect.com",
        index=None,
    ):
        """Check if the Linked Page opens up in the Same Tab"""
        check_result = False
        try:
            self.click_on_element(sp_link_locator, index)
            self.selenium.switch_to_window(self.selenium.current_window_handle)
            self.wait_it_out(5)
            check_result = bool(self.check_for_new_url(required_string, interval=2))
            # if self.check_for_new_url(required_string, interval=2):
            #     check_result = True
            # else:
            #     # print("\n SPL")
            #     # print("\n REQ: ", required_string)
            #     # print("\n URL: ", self.selenium.current_url)
            #     # print("\n")
            #     check_result = False
            return check_result
        finally:
            print()

    def check_new_page_link_works(
        self, np_link_locator=None, required_string="ischoolconnect", index=None
    ):
        """Check if the Linked Page opens up in a New Tab"""
        check_result = False
        try:
            # assert self.is_current_page
            time.sleep(0.5)
            self.click_on_element(np_link_locator, index)
            self.selenium.switch_to_window(self.selenium.window_handles[0])
            self.selenium.close()
            self.selenium.switch_to_window(self.selenium.window_handles[0])
            self.maximize()
            if self.check_for_new_url(required_string, interval=2):
                check_result = True
            else:
                # print("\n NPL")
                # print("REQ: ", required_string)
                # print("URL: ", str(self.selenium.current_url))
                check_result = False
            return check_result
        finally:
            print(check_result)

    def check_for_new_url(
        self, expected_url_string=EXIT_PATH_URL, interval=0.5, max_limit=_timeout
    ):
        """Generic Method to check until a new url is loaded, at given interval (in seconds)"""
        check_result = False
        cycle = 0.0
        max_limit = float(max_limit)
        try:
            while check_result is False and expected_url_string is not None:
                time.sleep(interval)
                cycle += interval
                current_page_url = str(self.selenium.current_url)
                if expected_url_string in current_page_url:
                    check_result = True
                    # print("\n\n We are now at URL : ", current_page_url)
                    self.wait_it_out(1)
                    return check_result
                if cycle > max_limit:
                    # print("\n Failed")
                    print("\n We want URL : ", expected_url_string)
                    print("\n We are now at URL : ", current_page_url)
                    return check_result
        finally:
            print()

    def check_new_window_link_works(
        self, nw_link_locator=None, required_string="ischoolconnect", index=None
    ):
        """Check if the Linked Page opens up in a New window"""
        check_result = False
        try:
            # assert self.is_current_page
            time.sleep(0.5)
            if index is None:
                index = self.select_random_index(nw_link_locator)
            time.sleep(3)
            self.click_on_element(nw_link_locator, index)
            self.selenium.switch_to_window(self.selenium.window_handles[1])
            time.sleep(2)
            # print(self.selenium.current_url)
            if self.check_for_new_url(required_string, interval=2):
                self.wait_it_out(1)
                check_result = True
            else:
                # print("\n NWL")
                # print("REQ: ", required_string)
                # print("URL: ", str(self.selenium.current_url))
                check_result = False
            self.selenium.close()
            self.selenium.switch_to_window(self.selenium.window_handles[0])
            return check_result
        except AssertionError as exception_case:
            print("\nException : ", exception_case)

        finally:
            print(check_result)

    def select_random_index(self, card_locator=_FOCUS_TAG_LOCATOR):
        card_list = self.get_page_elements(card_locator)
        self.wait_it_out(1)
        card_count = len(card_list)
        if card_count > 1:
            index = randint(0, card_count - 1)
        else:
            index = 0
        return index

    def scroll_into_view(self, locator, index=0, scroll_val=150):
        self.check_page_element(locator, timeout=25)
        self.wait_it_out(1)
        elem = self.selenium.find_elements(*locator)
        if index is None:
            index = self.select_random_index(locator)
        self.selenium.execute_script(
            "return arguments[0].scrollIntoView();", elem[index]
        )
        self.selenium.execute_script("window.scrollBy(0, -" + str(scroll_val) + ");")

    def switch_to_new_window(self, wait_quantum=1, timeout=10):
        check_result = False
        window_count = 0
        window_wait = 0
        try:
            while window_count < 2 or window_wait == timeout:
                self.wait_it_out(wait_quantum)
                window_wait += wait_quantum
                window_count = len(self.selenium.window_handles)
            if window_wait >= timeout:
                check_result = False
            else:
                self.selenium.switch_to_window(self.selenium.window_handles[1])
                check_result = True
        except AssertionError as exp:
            print("\n\nException : ", exp)
            return check_result
        return check_result

    def switch_to_old_window(self):
        check_result = False
        try:
            before_count = len(self.selenium.window_handles)
            self.selenium.close()
            self.wait_it_out(3)
            self.selenium.switch_to_window(self.selenium.window_handles[0])
            after_count = len(self.selenium.window_handles)
            check_result = bool(before_count > after_count)
            return check_result
            # if before_count > after_count:
            #     check_result = True
            # else:
            #     check_result = False
        except AssertionError as exp:
            print("\n\nException : ", exp)
            return check_result

    @classmethod
    def wait_it_out(cls, seconds=1.0):
        time.sleep(seconds)
        return True

    def click_on_browser_back_button(self):
        self.selenium.back()

    def click_on_browser_forward_button(self):
        self.selenium.forward()

    def print_page_source(self):
        source = self.get_text_of_elements()
        for text in source:
            print(text, "\n")
            assert source is not None

    def scroll_to_top(self):
        self.selenium.find_element(By.TAG_NAME, "body").send_keys(
            Keys.CONTROL + Keys.HOME
        )

    def scroll_to_down(self):
        self.selenium.find_element(By.TAG_NAME, "body").send_keys(
            Keys.CONTROL + Keys.END
        )

    def select_using_select(self, locator, value):
        Select(self.selenium.find_element(*locator)).select_by_value(value)
        return True

    def verify_form_errors(self, locator, count):
        form_errors = WebDriverWait(self.selenium.instance, 5).until(
            EC.visibility_of_all_elements_located(locator)
        )
        assert len(form_errors) == count, "The amount of errors is not equal to " + str(
            count
        )

    def test_images_for_200_response(self, url):
        self.selenium.get(url)
        example_images = self.selenium.find_elements(By.TAG_NAME, "img")
        for image in example_images:
            print(image)
            current_link = image.get_attribute("src")
            print(current_link)
            r = requests.get(current_link)
            try:
                assert r.status_code == 200
            except AssertionError as e:
                print(current_link + " delivered response code of " + r.status_code)
                return e

    def convert_list_to_string(self, list):
        str1 = ""
        for ele in list:
            str1 += ele
        return str1

    def listtostring(self, s):
        # initialize an empty string
        str1 = " "
        # return string
        return str1.join(s)

    def rand_x_digit_num(self, x, leading_zeroes=True):
        """Return an X digit number, leading_zeroes returns a string, otherwise int"""
        if not leading_zeroes:
            # wrap with str() for uniform results
            return random.randint(10 ** (x - 1), 10 ** x - 1)
        else:
            if x > 6000:
                return "".join([str(random.randint(0, 9)) for i in xrange(x)])
            else:
                return "{0:0{x}d}".format(random.randint(0, 10 ** x - 1), x=x)

    def close_leading_modal(self):
        return self.click_on_element(self._LEADING_MODAL_CLOSE_BUTTON_LOCATOR)

    def close_cookies_model(self):
        return self.click_on_element(self._SOUNDS_GOOD_BUTN_LOCATOR)

    # def hover_on_element(self, locator=None, locator1=None):
    #     """Generic function for hover on elements. (Range index version)"""
    #     hover_element = self.selenium.find_element(locator)
    #     action = ActionChains(self.selenium)
    #     action.move_to_element(hover_element).perform()
    #     action.click(hover_element)
    #     button_link = self.selenium.find_element(locator1)
    #     action.move_to_element(button_link).perform()
    #     button_link.click()
    #     click_result = True
    #     return click_result

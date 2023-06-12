from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from retry import retry
import requests
import logging
import time

logger = logging.getLogger(__name__)


class Browser(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @retry(TimeoutException, tries=2, delay=10, logger=logger)
    def navigate(self, url):
        self.driver.get(url)

    def get_page_title(self):
        return self.driver.title

    def get_current_page_url(self):
        return self.driver.current_url

    def back_to_previous_page(self):
        return self.driver.back()

    def get_clickable_element(self, locator):
        return self.wait.until(
            expected_conditions.element_to_be_clickable((locator))
        )

    def click_on_element(self, locator):
        clickable_element = self.get_clickable_element(locator)
        clickable_element.click()

    def click_on_not_visible_element(self, locator):
        self.driver.execute_script("arguments[0].click();",
                                   self.get_clickable_element(locator))
        time.sleep(2)

    def wait_invisibility_of_element(self, locator):
        return self.wait.until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def wait_visibility_of_element(self, locator):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def get_http_request(self, url):
        return requests.get(url)

    @retry(TimeoutException, tries=5, delay=10, logger=logger)
    def get_elements_list(self, locator):
        """Gets a list of WebElements given a locator.

        Parameters
        ----------
        locator : tuple, mandatory
            Contains the locator type and the web elements' dom identifier.
        Returns
        ------
        The web elements list.

        Throws
        ------
        TimeOutException:
            If the web elements are not present in DOM.
        """
        dom_identifier = locator[1]
        try:
            elements_list = self.wait.until(
                expected_conditions.presence_of_all_elements_located(locator)
            )
            return elements_list
        except TimeoutException:
            raise TimeoutException(
                f'Elements with locator {dom_identifier} not found.')

    def get_element_from_list_by_text(self, elements_list, element_text):
        for element in elements_list:
            if element.get_attribute("innerText") == element_text:
                return element

    def get_open_windows_number(self):
        return len(self.driver.window_handles)

    def switch_to_recent_open_tab(self):
        self.driver.switch_to_window(self.driver.window_handles[1])

    def close_browser_tab(self):
        self.switch_to_recent_open_tab()
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def clear_toast_cookie_local_storage(self):
        self.driver.execute_script(
            "window.localStorage.removeItem('isCookieDisclaimerDismissed');")

    def get_element_attribute(self, element, attr):
        return element.get_attribute(attr)

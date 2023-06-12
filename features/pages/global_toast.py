from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base import Browser
import logging

logger = logging.getLogger(__name__)


class GlobalToast(Browser):

    def __init__(self, driver):
        super().__init__(driver)

        # locators
        self._global_toast_bar = (By.CSS_SELECTOR, '.global-toast')
        self._global_toast_subscribe_button = (
            By.CSS_SELECTOR, '.global-toast-action__subscribe')
        self._dismiss_newsletter_button = (
            By.CSS_SELECTOR, '.global-toast-action__dismiss--newsletter')
        self._toast_cookie_button = (
            By.CSS_SELECTOR, '.global-toast-action__dismiss--cookie_disclaimer')

    def close_toast_cookie_toast(self):
        try:
            self.click_on_element(self._toast_cookie_button)
        except TimeoutException as te:
            logger.warning(
                'Element ' + self._toast_cookie_button[1] + ' not found')
            raise te

    def validate_global_toast_closed(self):
        return self.wait_invisibility_of_element(self._global_toast_bar)

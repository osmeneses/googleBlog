from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import logging
from .base import Browser

logger = logging.getLogger(__name__)


class MarketSelectorModalFeatures(Browser):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 5)
        # locators
        self._modal_close_button = (
            By.CLASS_NAME, 'market-selector-modal__close-icon')
        self._modal_mask = (By.CLASS_NAME, 'modal__mask')

    def click_on_modal_close_button(self):
        modal_close_button = self.get_modal_close_button()
        if modal_close_button is not None:
            modal_close_button.click()
            self.wait_invisibility_of_element(self._modal_mask)

    def get_modal_close_button(self):
        try:
            modal_close_button = self.get_clickable_element(
                self._modal_close_button)
            return modal_close_button
        except TimeoutException:
            logger.warning(
                'Element ' + self._modal_close_button[1] + ' not found')
            return None

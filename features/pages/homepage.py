from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base import Browser
from .settings import EDITORIAL_TYPES, SPOTLIGHT_EYEBROWS
import logging

logger = logging.getLogger(__name__)


class HomePage(Browser):

    def __init__(self, driver):
        super().__init__(driver)

        # locators
        self._spotlight_eyebrow = '.spotlight__eyebrow'
        self._spotlight_text = '.spotlight__text-link'
        self._spotlight_image = '.spotlight__image-anchor'
        self._featured_card = (By.CSS_SELECTOR, '.card--highlight-featured')
        self._featured_card_title = '.card--highlight-featured .card__title'
        self._featured_card_editorial_type = \
            '.card--highlight-featured .card__body-editorial-type'
        self._default_card = (
            By.CSS_SELECTOR, '.card--highlight-default')
        self._default_card_title = '.card--highlight-default .card__title'
        self._default_card_editorial_type = \
            '.card--highlight-default .card__body-editorial-type'
        self._open_tool_card_link = (By.CSS_SELECTOR, '.external-link')
        self._see_all_tools_button = (By.CSS_SELECTOR, '.page-section__cta')


    def is_spotlight_eyebrow_present(self):
        try:
            spotlight_eyebrow_text = self.driver.find_element(
                By.CSS_SELECTOR, self._spotlight_eyebrow).text
            return spotlight_eyebrow_text in SPOTLIGHT_EYEBROWS
        except TimeoutException as te:
            logger.error(
                'Element ' + self._spotlight_eyebrow + ' not found')
            raise te

    def click_spotlight_text(self):
        try:
            spotlight_text_element = self.driver.find_element(
                By.CSS_SELECTOR, self._spotlight_text)
            return self.get_http_request(
                spotlight_text_element.get_attribute("href"))
        except AttributeError as ae:
            logger.error(
                f'No spotlight text found')
            raise ae

    def click_spotlight_image(self):
        try:
            spotlight_image_element = self.driver.find_element(
                By.CSS_SELECTOR, self._spotlight_image)
            return self.get_http_request(
                spotlight_image_element.get_attribute("href"))
        except AttributeError as ae:
            logger.error(
                f'No spotlight image found')
            raise ae

    def click_featured_card(self):
        self.click_on_not_visible_element(self._featured_card)

    def featured_card_title_present(self):
        try:
            featured_card_title = self.driver.find_element(
                By.CSS_SELECTOR, self._featured_card_title)
            return featured_card_title is not None
        except TimeoutException:
            logger.warning(
                'Element ' + self._featured_card_title + ' not found')
            return None

    def featured_card_editorial_type_present(self):
        try:
            featured_card_editorial_type = self.driver.find_element(
                By.CSS_SELECTOR, self._featured_card_editorial_type).text
            return featured_card_editorial_type in EDITORIAL_TYPES
        except TimeoutException:
            logger.warning(
                'Element ' + self._featured_card_editorial_type + ' not found')
            return None

    def click_default_card(self):
        self.click_on_not_visible_element(self._default_card)

    def default_card_title_present(self):
        try:
            default_card_title = self.driver.find_element(
                By.CSS_SELECTOR, self._default_card_title)
            return default_card_title is not None
        except TimeoutException:
            logger.warning(
                'Element ' + self._default_card_title + ' not found')
            return None

    def default_card_editorial_type_present(self):
        try:
            default_card_editorial_type = self.driver.find_element(
                By.CSS_SELECTOR, self._default_card_editorial_type).text
            return default_card_editorial_type in EDITORIAL_TYPES
        except TimeoutException:
            logger.warning(
                'Element ' + self._default_card_editorial_type + ' not found')
            return None

    def click_open_tool_card_link(self):
        try:
            self.click_on_not_visible_element(self._open_tool_card_link)
            return True
        except TimeoutException as te:
            logger.info('No Open link elements found in Homepage')
            raise te

    def click_see_all_tools_button(self):
        self.click_on_not_visible_element(self._see_all_tools_button)

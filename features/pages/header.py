from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from .base import Browser
import logging

logger = logging.getLogger(__name__)


class HeaderFeatures(Browser):

    def __init__(self, driver):
        super().__init__(driver)

        # locators
        self._global_header_logo = (
            By.CLASS_NAME, '.twgn.twgn-logo-bar__twgn-logo.twgn-logo')
        self._global_header_logo_light = (
            By.CLASS_NAME, 'global-header__logo--light')
        self._market_selector_dropdown = (
            By.CSS_SELECTOR, '.global-header__select-wrapper select.locale-select.js-locale-select-element')
        self._menu_nav_item = (
            By.CSS_SELECTOR, '.global-navigation__link')
        self._submenu_nav_item = (
            By.CSS_SELECTOR, '.global-navigation-submenu__link')
        self._search_icon = (
            By.CSS_SELECTOR, 'button[data-item-id = "search"]')
        self._search_bar = (
            By.CLASS_NAME, '.twgn.twgn-placeholder.twgn-search__query')


    def click_on_global_header_logo(self):
        """Tries to perform a click on the standard TwG logo(blue)
        and if it gets a timeout exception, then it tries to perform
        a click on the light TwG logo (white).  If none logo is visible
        and clickable, then a TimeOut Exception will be thrown.
        """
        try:
            self.click_on_element(self._global_header_logo)
        except TimeoutException:
            self.click_on_element(self._global_header_logo_light)

    def get_global_header_logo(self):
        return self.get_clickable_element(self._global_header_logo)

    def get_market_selector_dropdown(self):
        return self.get_clickable_element(self._market_selector_dropdown)

    def click_on_market_selector_dropdown(self):
        self.click_on_element(self._market_selector_dropdown)

    def select_locale_on_market_selector_dropdown(self, locale_name):
        market_selector = Select(self.get_market_selector_dropdown())
        market_selector.select_by_visible_text(locale_name)

    def click_on_navbar_search_icon(self):
        """Performs a click on the nav bar search icon.
        """
        self.click_on_element(self._search_icon)

    def search_bar_is_opened(self):
        """Waits for the search bar to be present in the DOM as well as visible
        and throws an exception when it fails.

        Returns
        ------
        True, if the search bar is visible and present in DOM.
        False, if the search bar is not visible and the exception is thrown.

        Raises
        ------
        TimeoutException
            If the search bar is not visible and not present in DOM.
        """
        try:
            self.wait_visibility_of_element(self._search_bar)
            return True
        except TimeoutException:
            logger.error('Search bar on header is not visible')
            return False

    def click_on_navbar_menu_submenu_link(self, menu_item_name, url_to_check,
                                          level):
        """Finds the web elements for the given menu or submenu items names.
        If they're found, then it tries to perform a http request using the
        href attribute that belongs to menu/submenu item.

        If they're not found, then an exception will be raised and the scenario
        will fail.

        Parameters
        ----------
        menu_item_name : str, mandatory
        Name of the menu/submenu item.

        url_to_check : str, mandatory
        URL of the menu/submenu item.

        level: str, mandatory. Only two possible values: menu and submenu

        Returns
        ------
        The status code (200) after performing a http request using the href
        attribute that belongs to menu/submenu item.
        """
        locator = self._menu_nav_item
        if level == "submenu":
            locator = self._submenu_nav_item
        try:
            menu_items_list = self.get_elements_list(locator)
            menu_item = self.get_element_from_list_by_text(menu_items_list,
                                                           menu_item_name)
            if menu_item is None \
               or url_to_check != menu_item.get_attribute("href"):
                # To force an exception when navbar menu/submenu item was
                # not found or the URL is not the expected
                raise AttributeError
            return self.get_http_request(menu_item.get_attribute("href"))
        except AttributeError as ae:
            logger.error(
                f'The Navbar menu/submenu item: {menu_item_name} '
                f'was not found on page or the menu/submenu URL:{url_to_check}'
                f' is not the expected ')
            raise ae

from aloe import before, world, after
from selenium import webdriver
from ..pages.header import HeaderFeatures
from ..pages.homepage import HomePage
from ..pages.market_selector_modal import MarketSelectorModalFeatures
from ..pages.global_toast import GlobalToast
from selenium.webdriver.remote.remote_connection import LOGGER
import os
import logging

LOGGER.setLevel(logging.WARNING)


@before.all
def setup_suite():
    browser = os.environ.get('BROWSER', 'chrome')
    open_drivers(browser)
    prepare_pages(world.driver)


@after.all
def close_suite():
    close_drivers()


def open_drivers(browser):
    if browser == 'chrome':
        world.driver = get_chrome()
    elif browser == 'ff':
        world.driver = get_ff()
    else:
        world.driver = get_safari()
    world.driver.set_page_load_timeout(10)
    world.driver.maximize_window()


def get_chrome():
    return webdriver.Chrome('./chromedriver')


def get_ff():
    return webdriver.Firefox(executable_path='./geckodriver')


def get_safari():
    return webdriver.Safari(executable_path='/usr/bin/safaridriver')


def prepare_pages(driver):
    world.header_features = HeaderFeatures(driver)
    world.home_page = HomePage(driver)
    world.market_selector_modal = MarketSelectorModalFeatures(driver)
    world.global_toast = GlobalToast(driver)


def close_drivers():
    if world.driver:
        world.driver.quit()

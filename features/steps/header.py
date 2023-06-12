from aloe import step, world
from nose.tools import assert_equal, assert_in
from aloe.tools import guess_types


@step('I read the title of the page')
def when_i_get_the_homepage_title(step):
    world.page_title = world.header_features.get_page_title()


@step('I can see the text "([^“]*)"')
def then_i_can_see_the_text(step, title):
    assert_equal(title, world.page_title)


@step('I click on the market selector modal close icon')
def click_on_market_selector_close_icon(step):
    world.market_selector_modal.click_on_modal_close_button()


@step('I click on the header logo')
def click_on_header_logo(step):
    world.header_features.click_on_global_header_logo()


@step('The url opened is "([^“]*)"')
def the_url_opened_is(step, expected_url):
    assert_equal(expected_url, world.header_features.get_current_page_url())


@step('I select the locale "([^“]*)" on the market selector dropdown')
def select_locale_on_market_selector_dropdown(step, locale_name):
    world.header_features.select_locale_on_market_selector_dropdown(
        locale_name)


@step('Navbar menu links are valid')
def navbar_menu_links_are_valid(step):
    for menu_item in guess_types(step.hashes):
        # It fails and throws an exception for not finding menu or the url is
        # not the expected
        world.menu_item_request = \
            world.header_features.click_on_navbar_menu_submenu_link(
                menu_item_name=menu_item['menu_item_name'],
                url_to_check=menu_item['menu_url'],
                level="menu")
        assert_equal(200, world.menu_item_request.status_code)


@step('Navbar submenu links are valid')
def navbar_submenu_links_are_valid(step):
    for submenu_item in guess_types(step.hashes):
        # It fails and throws an exception for not finding menu or submenu or
        # the url is not the expected
        world.submenu_item_request = \
            world.header_features.click_on_navbar_menu_submenu_link(
                menu_item_name=submenu_item['submenu_item_name'],
                url_to_check=submenu_item['submenu_url'],
                level="submenu")
        assert_equal(200, world.submenu_item_request.status_code)


@step('I click on the navbar search icon')
def click_on_navbar_search_icon(step):
    world.header_features.click_on_navbar_search_icon()


@step('The search bar is opened')
def search_bar_is_opened(step):
    world.search_bar_opened = world.header_features.search_bar_is_opened()
    assert_equal(True, world.search_bar_opened,
                 'Search bar was not opened.')


@step('The search bar is closed')
def search_bar_is_closed(step):
    world.search_bar_closed = world.header_features.search_bar_is_opened()
    assert_equal(False, world.search_bar_closed,
                 'Search bar was not closed.')


@step('I go to the Newsletter form in a new tab')
def then_i_go_to_the_newsletter_progressive_form(step):
    world.request = world.header_features.get_http_request(
        world.header_features.get_element_attribute(
            world.subscribe_cta, "href"))
    assert_equal(200, world.request.status_code)
    assert_in('newsletter/signup/landing/?slug', world.request.url)
    assert_equal(
        '_blank', world.header_features.get_element_attribute(
            world.subscribe_cta, "target"))

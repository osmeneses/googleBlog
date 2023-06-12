from aloe import step, world
from nose.tools import assert_equal, assert_in, assert_true


@step('I can see the spotlight eyebrow text')
def spotlight_feature_text(step):
    assert_true(world.home_page.is_spotlight_eyebrow_present())


@step('I can click the spotlight article')
def can_click_spotlight_article(step):
    world.spotlight_text_request = world.home_page.click_spotlight_text()
    assert_equal(200, world.spotlight_text_request.status_code)
    world.spotlight_image_request = world.home_page.click_spotlight_image()
    assert_equal(200, world.spotlight_image_request.status_code)
    assert_equal(
        world.spotlight_text_request.url, world.spotlight_image_request.url)


@step('I can see a featured card title')
def then_i_can_see_a_featured_card_title(step):
    assert_true(world.home_page.featured_card_title_present())


@step('I can see a feature card editorial type')
def and_i_can_see_a_feature_card_editorial_type(step):
    assert_true(world.home_page.featured_card_editorial_type_present())


@step('I can click the featured card')
def and_i_can_click_the_featured_card(step):
    world.home_page.click_featured_card()


@step('I can see a default card title')
def then_i_can_see_a_default_card_title(step):
    assert_true(world.home_page.default_card_title_present())


@step('I can see a default card editorial type')
def and_i_can_see_a_default_card_editorial_type(step):
    assert_true(world.home_page.default_card_editorial_type_present())


@step('I can click the default card')
def and_i_can_click_the_default_card(step):
    world.home_page.click_default_card()
    world.current_url = world.home_page.get_current_page_url()
    world.request = world.home_page.get_http_request(world.current_url)
    assert_equal(200, world.request.status_code)


@step('I can click the open tool card link')
def i_can_click_open_link(step):
    assert_true(world.home_page.click_open_tool_card_link())


@step('I go to a new tab page')
def i_go_to_a_new_tab_page(step):
    assert_true(world.home_page.get_open_windows_number() == 2)
    world.home_page.close_browser_tab()


@step('The See All Tools button takes to the Tools Landing page')
def see_all_tools_button_take_to_tools_landing_page(step):
    world.home_page.click_see_all_tools_button()
    assert_in('/tools/', world.home_page.get_current_page_url())

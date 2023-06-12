from aloe import step, world
from nose.tools import assert_true


@step('I click the close cookie toast button')
def click_close_cookie_toast_button(step):
    world.global_toast.close_toast_cookie_toast()


@step('The global toast is not visible')
def global_toast_not_visible(step):
    assert_true(world.global_toast.validate_global_toast_closed())
    # Clearing localStorage as once closed it won't show again for EU locales
    world.global_toast.clear_toast_cookie_local_storage()

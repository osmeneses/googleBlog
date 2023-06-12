from aloe import step, world


@step('I navigate to the Think with Google home page')
def given_i_navigate_to_the_home_page(step):
    world.header_features.navigate('https://www.thinkwithgoogle.com/')


@step('I navigate to the Think with Google page for locale "([^“]*)"')
def navigate_to_locale_home_page(step, locale_code):
    if locale_code == 'en-us':
        homepage_url = 'https://www.thinkwithgoogle.com/'
    else:
        homepage_url = f'https://www.thinkwithgoogle.com/intl/{locale_code}/'
    world.header_features.navigate(homepage_url)


@step('I navigate to my home page')
def given_i_navigate_to_my_home_page(step):
    world.header_features.navigate(r'file:///Users/macbookpro/Documents/Omar/2023/Learning/Automation/javascript-basics/JavaScript_Basics/index.html')

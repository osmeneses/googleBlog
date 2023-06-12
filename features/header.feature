Feature: Global Header

  Scenario: Title says "Think with Google - Discover Marketing Research & Digital Trends"
    Given I navigate to the Think with Google home page
    When I read the title of the page
    Then I can see the text "Think with Google - Discover Marketing Research & Digital Trends"

  Scenario Outline: Click on header logo takes to locale home page
    Given I navigate to the Think with Google page for locale "<locale_code>"
    And I click on the market selector modal close icon
    When I click on the header logo
    Then The url opened is "<locale_homepage_url>"

    Examples:
      |locale_code  |locale_homepage_url                        |
      |en-us        |https://www.thinkwithgoogle.com/             |
      |de-de        |https://www.thinkwithgoogle.com/intl/de-de/  |
      |es-419       |https://www.thinkwithgoogle.com/intl/es-419/ |
      |en-apac      |https://www.thinkwithgoogle.com/intl/en-apac/|
      |zh-tw        |https://www.thinkwithgoogle.com/intl/zh-tw/  |

  Scenario Outline: Market selector goes to the selected locale
    Given I navigate to the Think with Google home page
    And I click on the market selector modal close icon
    When I select the locale "<locale_name>" on the market selector dropdown
    Then The url opened is "<locale_homepage_url>"
    And I read the title of the page
    And I can see the text "<locale_page_title>"

    Examples:
      |locale_name  |locale_homepage_url                        |locale_page_title                                               |
      |台灣          |https://www.thinkwithgoogle.com/intl/zh-tw/  |Think with Google 台灣                                          |
      |MENA         |https://www.thinkwithgoogle.com/intl/en-145/ |Think with Google - Discover Marketing Research & Digital Trends|
      |대한민국        |https://www.thinkwithgoogle.com/intl/ko-kr/  |Think with Google: Marketing Research & Digital Trends          |
      |Россия       |https://www.thinkwithgoogle.com/intl/ru-ru/  |Think with Google — маркетинговые исследования и digital-тренды|
      |ประเทศไทย    |https://www.thinkwithgoogle.com/intl/th-th/  |Think with Google: Marketing Research & Digital Trends          |
      |Brasil       |https://www.thinkwithgoogle.com/intl/pt-br/  |Think with Google Brasil                                        |

  Scenario: Navbar menu items go to page (en_us)
    Given I navigate to the Think with Google home page
    And I click on the market selector modal close icon
    Then Navbar menu links are valid
      |menu_item_name       |menu_url                                            |
      |Consumer Insights    |https://www.thinkwithgoogle.com/consumer-insights/    |
      |Marketing Strategies |https://www.thinkwithgoogle.com/marketing-strategies/ |
      |Future of Marketing  |https://www.thinkwithgoogle.com/future-of-marketing/  |
      |Tools                |https://www.thinkwithgoogle.com/tools/              |

  Scenario: Navbar submenu items go to page (en_us)
    Given I navigate to the Think with Google home page
    And I click on the market selector modal close icon
    Then Navbar submenu links are valid
      |submenu_item_name            |submenu_url                                                              |
      |Consumer Journey             |https://www.thinkwithgoogle.com/consumer-insights/consumer-journey/        |
      |Consumer Trends              |https://www.thinkwithgoogle.com/consumer-insights/consumer-trends/         |
      |App & Mobile                 |https://www.thinkwithgoogle.com/marketing-strategies/app-and-mobile/       |
      |Data & Measurement           |https://www.thinkwithgoogle.com/marketing-strategies/data-and-measurement/ |
      |Programmatic                 |https://www.thinkwithgoogle.com/marketing-strategies/programmatic/         |
      |Retail                       |https://www.thinkwithgoogle.com/collections/retail/                        |
      |Search                       |https://www.thinkwithgoogle.com/marketing-strategies/search/               |
      |YouTube                      |https://www.thinkwithgoogle.com/marketing-strategies/video/                |
      |Creativity                   |https://www.thinkwithgoogle.com/future-of-marketing/creativity/            |
      |Digital Transformation       |https://www.thinkwithgoogle.com/future-of-marketing/digital-transformation/|
      |Machine Learning             |https://www.thinkwithgoogle.com/future-of-marketing/emerging-technology/   |
      |Management & Culture         |https://www.thinkwithgoogle.com/future-of-marketing/management-and-culture/|
      |Privacy & Trust              |https://www.thinkwithgoogle.com/future-of-marketing/privacy-and-trust/     |

  Scenario: Magnifying glass opens and closes search bar
    Given I navigate to the Think with Google home page
    And I click on the market selector modal close icon
    When I click on the navbar search icon
    And The search bar is opened
    Then I click on the navbar search icon
    And The search bar is closed

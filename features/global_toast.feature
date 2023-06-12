Feature: Global Toast

    Scenario Outline: Cookie toast can be closed
        Given I navigate to the Think with Google page for locale "<locale_code>"
        And I click on the market selector modal close icon
        Then I click the close cookie toast button
        And The global toast is not visible

    Examples:
        |locale_code|
        |de-de      |
        |en-aunz    |
        |en-154     |
        |en-gb      |
        |es-es      |
        |fr-fr      |
        |en-ca      |
        |ko-kr      |
        |tr-tr      |

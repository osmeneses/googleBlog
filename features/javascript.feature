Feature: JavaScript Project

  Scenario: Title says "Javascript Basics"
    Given I navigate to my home page
    When I read the title of the page
    Then I can see the text "Javascript Basics"

  
Feature: Homepage

  Scenario: Spotlight article and clickable
    Given I navigate to the Think with Google home page
    And I click on the market selector modal close icon
    Then I can see the spotlight eyebrow text
    And I can click the spotlight article

  Scenario: Featured card present and clickable
    Given I navigate to the Think with Google page for locale "en-aunz"
    And I click on the market selector modal close icon
    Then I can see a featured card title
    And I can see a feature card editorial type
    And I can click the featured card

  Scenario: Default card present and clickable
    Given I navigate to the Think with Google home page
    And I click on the market selector modal close icon
    Then I can see a default card title
    And I can see a default card editorial type
    And I can click the default card

  Scenario: Open tool card link
    Given I navigate to the Think with Google page for locale "en-apac"
    And I click on the market selector modal close icon
    Then I can click the open tool card link
    And I go to a new tab page

  Scenario: See All Tools button takes to Tools Landing page
    Given I navigate to the Think with Google home page
    And I click on the market selector modal close icon
    Then The See All Tools button takes to the Tools Landing page

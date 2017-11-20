@userFeature
Feature: User

  @getuser
  Scenario: Get user information
    Given I have a username "qa.testing.dgs@gmail.com"
    And I have a token "7aa42a278db04c46a7fc424bf64acd31"
    When I GET  my request to success
    Then I receive status code 200 for the response
 
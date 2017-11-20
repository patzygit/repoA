@userFeature
Feature: User

  @getuser
  Scenario: Get user information
    Given I have a user authenticated
    And I have service for "/user.json"
    When I send GET user request to have user information
    Then I receive status code 200 for the response
 
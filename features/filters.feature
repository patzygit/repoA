@filtersFeature @smoke
Feature: Filters

  Background: User authenticated
    Given I have a new user authenticated

  @getAllFilters
  Scenario: Get all filters
    Given I have a service of "/filters.json"
    When I send "GET" filters request, the result is returned.
    Then I receive the status code "200" for the response

  @getFilterById
  Scenario: Get filter by id
    Given I have a service with the id "/filters/-5.json"
    When I send "GET" filter by id request to have the result
    Then I receive the status code "200" of the response

  @getItemOfOneFilter
  Scenario: Get item of one filter
    Given I have a service with id of the item "/filters/-1/items.json"
    When I send "GET" filter by the id of the item and get the result
    Then I receive the status code "200"

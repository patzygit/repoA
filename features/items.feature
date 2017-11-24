@itemsFeature
Feature: Items

  @getitem
Scenario: Get items
	Given I have a service for "/items.json"
	When I send GET items request to get all items information
	Then I receive status code 200 for the response
    #And response body should contain the same structure that dataAllItems.json


  @getitem
Scenario Outline: Get item by Id
	Given I have a service with id "/items/<Id>.json"
	When I send GET item request to get specified item information
	Then I receive status code 200 for the response
    And response body should be the same of "data/dataIdItems.json" with "data/Item_GETIdItems.json" for specific item

Examples:
|Id|
|10049816|

  @getitem
Scenario Outline: Get root parent for unchecked item
	Given I have a service with root id "/items/<Id>/RootItem.json"
	When I send GET item request to get root parent for unchecked item
	Then I receive status code 200 for the response
    And response body should be the same of "data/dataRootIdItems.json" with "data/Item_GETRootIdItems.json" for unchecked item

Examples:
|Id|
|10049816|

  @getitem
Scenario Outline: Get root parent for done item
	Given I have a service with item id "/items/<Id>/DoneRootItem.json"
	When I send GET item request to get an error for done item that does not exist
	Then I receive status code 200 for the response
    #And response body should contain item information of doneRoot item as dataDRootItems.json
Examples:
|Id|
|10049816|


  @additem
Scenario: Add item
	Given I have a service for "/items.json"
	And I have a pyloadBody:
	"""
	{
		"Content":"New Item - paty2"
	}
	"""
	When I send POST items request to add a new item
	Then I receive status code 200 for the response
      And I got response body of new item

  @deleteitem
Scenario Outline: Delete item
	Given I have a service for "/items/<Id>.json"
	When I send DELETE items request to delete an item
	Then I receive status code 200 for the response
	    And I receive Deleted parameter True
    #Deleted": true
Examples:
|Id|
|10049837|

  @updateitem
Scenario Outline: Update item
	Given I have a service for "/items/<Id>.json"
	And I have a updateBody:
	"""
	{
		"Content":"Item - updated paty6"
	}
	"""
 		# "Notes":"This is note to update"
	When I send PUT items request to update a new item
	Then I receive status code 200 for the response
      And I recieve <updatedParameter> parameter for item with <description>

Examples:
|Id|updatedParameter|description|
|10049818|Content   |Item - updated paty6|
#|10049599|Notes   |This is note to update|
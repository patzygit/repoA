@itemsFeature
Feature: Items

  @getitem
Scenario: Get items
	Given I have a service for "/items.json"
	When I send GET items request to get all items information
	Then I receive status code 200 for the response
    #And reponse body should contain the same structure that dataAllItems.json


  @getitem
Scenario Outline: Get item by Id
	Given I have a service with id "/items/<Id>.json"
	When I send GET item request to get specified item information
	Then I receive status code 200 for the response
    #And reponse body should contain item information of specified item as dataAllItems.json

Examples:
|Id|
|10048278|

  @getitem
Scenario Outline: Get root parent for unchecked item
	Given I have a service with root id "/items/<Id>/RootItem.json"
	When I send GET item request to get root parent for unchecked item
	Then I receive status code 200 for the response
    #And reponse body should contain item information of unchecked item as dataAllItems.json
Examples:
|Id|
|10028551|

  @getitem
Scenario Outline: Get root parent for done item
	Given I have a service with item id "/items/<Id>/DoneRootItem.json"
	When I send GET item request to get root parent for done item
	Then I receive status code 200 for the response
    #And reponse body should contain item information of doneRoot item as dataAllItems.json
Examples:
|Id|
|10048278|


  @additem
Scenario: Add item
	Given I have a service for "/items.json"
	When I send POST items request to add a new item
      And I have a pyloadBody
      """
      {
        "Content":"New Item - paty"
      }
      """
	Then I receive status code 200 for the response
      And I got response body of new item
      """
      {
          "Id": 10048278,
          "Content": "New Item - paty",
          "ItemType": 1,
          "Checked": false,
          "ProjectId": null,
          "ParentId": null,
          "Path": "",
          "Collapsed": false,
          "DateString": null,
          "DateStringPriority": 0,
          "DueDate": "",
          "Recurrence": null,
          "ItemOrder": null,
          "Priority": 4,
          "LastSyncedDateTime": "/Date(1511283587351)/",
          "Children": [],
          "DueDateTime": null,
          "CreatedDate": "/Date(1511283587337)/",
          "LastCheckedDate": null,
          "LastUpdatedDate": "/Date(1511283587337)/",
          "Deleted": false,
          "Notes": "",
          "InHistory": false,
          "SyncClientCreationId": null,
          "DueTimeSpecified": true,
          "OwnerId": 589936
      }
      """
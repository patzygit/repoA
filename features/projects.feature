@projectsFeature
Feature: Projects
As ToDo user
 I want to manage my projects
 Because Project holds a number of items. Every Item in the system belongs to a Project.
 If an Item doesn’t have a Project assigned to it, it only displayed in the Inbox.
 Projects can be in hierarchy containing other projects.

  @getprojects
Scenario: Get All Projects
 Given I am an authenticated user
 When I call the method GET_Project
 Then I receibe a status code 200
  And a list of all projects and subprojects should be displayed

Scenario: Create a new Project
 Given I am an authenticated user
  And I have a new proyect (AprobarLaMateria)
 When I call the method Create_New_Project
  And I indicate the project name and an Icon
 Then I receibe a status code 200
  And A new proyect should be created

 
Feature: Projects
  List, Retrieve, Update, Create Project and Project Forms

  Background:
    Given we authenticate using a valid key

  Scenario: List of Projects
    When we request a list of projects
    Then we get the list of projects with test project included

  Scenario: Retrieve Project Information
    When we request for the test project
    Then we get the test project back

  Scenario: Update Project Information
    When we change the test project name
    Then we get test project with new name

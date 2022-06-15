Feature: Projects
  List, Retrieve, Update, Create Project and Project Forms
  Background: we authenticate using a valid key

  Scenario: List of Projects
    When we request a list of projects
    Then we get the list of projects we defined back
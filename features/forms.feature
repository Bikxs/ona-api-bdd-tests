Feature: Forms
  List, Retrieve Published Forms.

  Background:
    Given we authenticate using a valid key

  Scenario: Get list of forms on test project
    When we request a list of test project forms
    Then we get a list of project forms
    And the test form id should be included in the list
  Scenario: Get Form Information
    When we request a infomation of test form
    Then we should get infomation about the test form
  Scenario: Set Form Information
    When we change information of test form
    Then we should get updated infomation about the test form

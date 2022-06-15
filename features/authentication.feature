Feature: Authentication
  Authentication and Status Codes

  Scenario: No authentication
    Given we are not authenticated
    When we request our list of projects
    Then we shall received a 200 status code
    And the project list will be empty

  Scenario: Valid Token Authentication
    Given we authenticate using a valid key
    When we request our list of projects
    Then we shall received a 200 status code
    And the project list will not be empty

  Scenario: Valid Basic Authentication
    Given we authenticate using a valid username/password
    When we request our list of projects
    Then we shall received a 200 status code
    And the project list will not be empty

  Scenario: Invalid Token Authentication
    Given we authenticate using an invalid key
    When we request our list of projects
    Then we shall received a 401 status code

  Scenario: Invalid Basic Authentication
    Given we authenticate using a bad username/password
    When we request our list of projects
    Then we shall received a 401 status code
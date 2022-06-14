Feature: Authentication

  Scenario: Valid Token Authentication
    Given we are not authenticated
    When we authenticate using a valid key
    Then we shall received a 200 status code

  Scenario: Valid Basic Authentication
    Given we are not authenticated
    When we authenticate using a valid username/password
    Then we shall received a 200 status code

  Scenario: Invalid Token Authentication
    Given we are not authenticated
    When we authenticate using an invalid key
    Then we shall received a 401 status code

  Scenario: Invalid Basic Authentication
    Given we are not authenticated
    When we authenticate using a bad username/password
    Then we shall received a 401 status code
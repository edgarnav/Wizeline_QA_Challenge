Feature: Login

  Scenario: Login with a valid user
    Given Prepare classes login
    Then Validate login page
    When Send user and password
    Then Press login button
    And Validate products page

  Scenario: Login with an invalid user
    Given Prepare classes login
    Then Validate login page
    When Send invalid user and password
    Then Press login button
    And Validate error message

  Scenario: Logout from the home page
    Given Prepare classes login
    Then Validate login page
    When Send user and password
    Then Press login button
    Then Validate products page
    When Click menu button
    Then Click logout option
    And Validate login page

Feature: Products list

  Scenario: Sort products by Price (low to high)
    Given Prepare classes products list
    Then Validate login page
    When Send user and password
    Then Press login button
    Then Validate products page
    When Sort by price low to high
    Then Validate price order

Feature: Purchase

  Scenario: Complete a purchase
    Given Prepare classes purchase
    Then Validate login page
    When Send user and password
    Then Press login button
    Then Validate products page
    When Add multiple products
    When Click shopping cart button
    Then Verify shopping cart page
    Then Verify added products
    When Click checkout button
    Then Validate information page
    When Send personal information
    Then Click continue button
    Then Validate overview page
    When Click finish button
    Then Verify complete page
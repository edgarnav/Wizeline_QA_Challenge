Feature: Shipping cart

  Scenario: Add multiple items to the shopping cart
    Given Prepare classes shopping cart
    Then Validate login page
    When Send user and password
    Then Press login button
    Then Validate products page
    When Add multiple products
    When Click shopping cart button
    Then Verify shopping cart page
    Then Verify added products

  Scenario: Add the specific product Sauce Labs Onesie to the shopping cart
    Given Prepare classes shopping cart
    Then Validate login page
    When Send user and password
    Then Press login button
    Then Validate products page
    When Add specific product to cart
    When Click shopping cart button
    Then Verify shopping cart page
    Then Verify added products

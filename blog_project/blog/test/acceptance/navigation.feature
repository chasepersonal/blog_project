Feature: Test navigation between pages
  Customer wants to go to the appropriate link

  Scenario: Welcome link can go to the Blog
    Given I am on the Welcome page
    When I click on the "Blog" link
    Then I am on the blog page
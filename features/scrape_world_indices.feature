# Created by Oem at 19/04/2020
Feature: To scrape the world indices from the yahoo finance page

  Scenario Outline: scrape a named index

  Given I am on the yahoo world indices page
  When I scrape the named index <index>
  Then I output the data to the std out

  Examples:
    |index   |
    |^DJI    |
    |^GSPC   |
    |^FTSE   |

  Scenario: scrape all indexes

  Given I am on the yahoo world indices page
  When I scrape all the named indices
  Then I output the data to the std out


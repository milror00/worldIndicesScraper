# Yahoo World Indices Scraper

This is a demo project that uses python - request and behave to scrape the world indices published by yahoo finance.

Requirements to run :

Python 3.7 above
behave==1.2.6
requests==2.23.0
lxml==4.5.0

Steps for installation:

1. Clone git repo
2. I use PyCharm Professional to I import the project which creates a virtual environment for the project
3. Install libraries :
  pip install behave
  pip install requests
  pip install lxml
  
4. Open the console at the root of project and run the command :

behave ./features

Feature 

There is a single feature file with 2 scenarios :

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


An extension to the project would be to add an data adapter to save the indices to a database.

Scheduling the running of the application

Rather than create my own schedulig code - I use jenkins to manage the periodic execution of the application

#TODO

Add a vagrant file that hosts jenkins and db which then can be used to run the application unmanned - say o collect data every 15 mins





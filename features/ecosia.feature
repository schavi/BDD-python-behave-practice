
Feature: Searching the web
    Users should be able to retrieve results from the internet based on keywords.
    They should be able to pick between general results, images only, videos only and news.

    Scenario: General search
        Given Opening ecosia.org
        When Entering 'python behave' into the search bar
        And Clicking the search button
        Then The behave documentation shows up in the results
    
    Scenario: Image search
        Given Opening ecosia.org
        When Entering 'kittycat' into the search bar
        And Clicking the search button
        And Clicking the images tab
        Then Images of 'kittycat's are shown
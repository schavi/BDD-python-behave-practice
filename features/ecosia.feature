
Feature: Searching the web
    Users should be able to retrieve results from the internet based on keywords.
    They should be able to pick between general results, images only, videos only and news.


    Scenario: General search
        Given ecosia.org is open in 'firefox'
        When the user enters 'python behave' into the search bar
        Then the behave documentation shows up in the results
    
    Scenario: Image search
        Given ecosia.org is open in 'firefox'
        When the user enters 'kittycat' into the search bar
        And the user clicks on the images tab
        Then images of 'kittycat's are shown
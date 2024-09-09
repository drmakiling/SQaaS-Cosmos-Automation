Feature: Behave with Cosmos

    #3414
    @test @regression @smoketest
    Scenario: test
        Given user is on "Dev"
        And the user is logged in as "STUDYBA1"
        Then create or select a case a study
        Then add a country with default settings
        When cancel the date of birth format modal

    #3419
    @test3419
    Scenario: COSMOS-3419
        Given user is on "Dev"
        And the user is logged in as "STUDYBA1"
        Then create or select a case a study
        Then add a country with default settings
        When open delete country modal




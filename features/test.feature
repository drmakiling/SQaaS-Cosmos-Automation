Feature: Behave with Cosmos

    #3414
    @test @regression @smoketest
    Scenario: test
        Given user is on "Dev"
        And the user is logged in as "USER1"
        Then create or select a case a study
        Then add a country with default settings
        When cancel the date of birth format modal






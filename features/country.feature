Feature: Behave with Cosmos

    #3414
    @test @country
    Scenario: User_views_a_draft_study and On_Countries_section When Clicks_on_Country_DOB_format_button Then Verify_system_displays_Country_DOB_format_modal
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        When cancel the date of birth format modal

    #3413
    @test @country @testrun
    Scenario:Verify_system_displays_Country_DOB_format_modal and Change_DOB_format_to_{RTSM} When Clicks_Country_DOB_format_modal_save_button Then Verify_updated_Country_DOB_format_saved
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        When verify the updated country dob format for "3413"

    #3412
    @test @country
    Scenario:Verify_system_displays_Country_DOB_format_modal and Change_DOB_format_to_{Custom} When Clicks_Country_DOB_format_modal_save_button Then Verify_updated_Country_DOB_format_saved
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        When verify the updated country dob format for "3412"

    #3410
    @test @country
    Scenario: User_views_a_draft_study and On_Countries_section When Clicks_on_Country_DOB_format_button Then Verify_system_displays_Country_DOB_format_modal
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        When verify the date of birth format modal

    #3419
    @test @country
    Scenario: User_views_a_draft_study and On_Countries_section When Click_Country_Delete_button Then Verify_system_displays_country_delete_confirmation_popup
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        When open delete country modal



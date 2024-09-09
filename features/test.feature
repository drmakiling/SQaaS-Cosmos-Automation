Feature: Behave with Cosmos

    #3414
    @test
    Scenario: {StudyBA}_User and User_views_a_draft_study and On_Countries_section When Clicks_on_Country_DOB_format_button Then Verify_system_displays_Country_DOB_format_modal
        Given user is on "Dev"
        And the user is logged in as "STUDYBA1"
        Then create or select a case a study
        Then add a country with default settings
        When cancel the date of birth format modal

    #3413
    @test
    Scenario:Verify_system_displays_Country_DOB_format_modal and Change_DOB_format_to_{RTSM} When Clicks_Country_DOB_format_modal_save_button Then Verify_updated_Country_DOB_format_saved
        Given user is on "Dev"
        And the user is logged in as "STUDYBA1"
        Then create or select a case a study
        Then add a country with default settings
        When verify the updated country dob format

    #3419
    @test3419
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_In_{StudyBA}_User and User_views_a_draft_study and On_Countries_section When Click_Country_Delete_button Then Verify_system_displays_country_delete_confirmation_popup
        Given user is on "Dev"
        And the user is logged in as "STUDYBA1"
        Then create or select a case a study
        Then add a country with default settings
        When open delete country modal



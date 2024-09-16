Feature: Behave with Cosmos

    #3414
    @country
    Scenario: User_views_a_draft_study and On_Countries_section When Clicks_on_Country_DOB_format_button Then Verify_system_displays_Country_DOB_format_modal
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        When cancel the date of birth format modal

    #3413
    @country @test
    Scenario:Verify_system_displays_Country_DOB_format_modal and Change_DOB_format_to_{RTSM} When Clicks_Country_DOB_format_modal_save_button Then Verify_updated_Country_DOB_format_saved
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        When verify the updated country dob format for "3413"

    #3412
    @country
    Scenario:Verify_system_displays_Country_DOB_format_modal and Change_DOB_format_to_{Custom} When Clicks_Country_DOB_format_modal_save_button Then Verify_updated_Country_DOB_format_saved
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        When verify the updated country dob format for "3412"

    #3410
    @country
    Scenario: User_views_a_draft_study and On_Countries_section When Clicks_on_Country_DOB_format_button Then Verify_system_displays_Country_DOB_format_modal
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        When verify the date of birth format modal

    #3419
    @country
    Scenario: User_views_a_draft_study and On_Countries_section When Click_Country_Delete_button Then Verify_system_displays_country_delete_confirmation_popup
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        When open delete country modal


    #3517
    @country
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_In_{StudyBA}_User and User_views_a_draft_study and On_Countries_section and [Not] On_{Edit}_Country_modal_with_edits When Click_Country_Cancel_button Then [Not] Verify_Country_Cancel_popup_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        And edit an existing countries record
        When click Cancel button
        Then verify Countries cancel popup is not displayed

    #3421
    @country
    Scenario: Given Verify_system_displays_country_delete_confirmation_popup When Click_Yes_button_on_delete_country_modal Then Verify_system_will_delete_the_country
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        Then add a country with default settings
        And add a country with default settings
        When open delete country modal
        Then verify country is deleted

    #3516
    @country
    Scenario: Given Verify_system_displays_country_delete_confirmation_popup When Click_Yes_button_on_delete_country_modal Then Verify_system_will_delete_the_country
        Given the user is logged in as "STUDYBA1"
        Then create or select a case a study
        And open add country modal
        When click Cancel button
        Then verify cancel popup not displayed

    #3488
    @country
    Scenario:Signed_In_{StudyBA}_User and  User_views_a_draft_study and On_Countries_section and On_{Add}_Country_modal_with_edits When Click_Country_Cancel_button Then Verify_Country_Cancel_popup_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        When On Cancel pop up is displayed for Country

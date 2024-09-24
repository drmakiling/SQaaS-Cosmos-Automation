Feature: General


    @15534
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_In_{StudyBA}_User and Draft_Study_{MyStudies} and On_General_feature and Config_alert_On When Click_MNOPTS_Edit_button Then Verify_MNOPTS_modal_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "General" feature nav menu option
        And config alert is "on"
        When Click "min number of patients" Edit button
        Then Verify min number of patients modal

    @15522
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_In_{StudyBA}_User and Draft_Study_{MyStudies} and On_General_feature and Config_alert_On When Click_SO_Edit_button Then Verify_SO_modal_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "General" feature nav menu option
        And config alert is "on"
        When Click "study overview" Edit button
        Then Verify study overview modal


    @15773
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_in_{StudyBA}_user and On_dashboard and Draft_Study_{MyStudies} and On_Study_Landing_Page and On_General_feature When Click_Comments_button Then Verify_Comments_pane_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "General" feature nav menu option
        And click on the button for comment side panel
        Then Verify comment side panel


    @4078
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_in_{StudyBA}_user and On_dashboard and Draft_Study_{MyStudies} and On_Study_Landing_Page and On_General_feature When Click_Comments_button Then Verify_Comments_pane_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "General" feature nav menu option
        And click on the button for comment side panel
        And add comment less than 2 characters
        Then verify comment of less than 2 characters is not added
        When add comment with 501 characters
        Then verify 501st character is not added in comment
        Then add comment with url 
        Then Verify comment side panel with comment


@groupedActivities
Feature: Grouped Activities

    @19337
    Scenario: Draft_Study_{MyStudies} and Config_Alert_Off When Click_Grouped_activities_feature Then Verify_Grouped_activities_feature_page
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Grouped activities" feature nav menu option
        When config alert is "off"
        Then Grouped Activities feature page is empty

    @19364
    Scenario: Draft_Study_{MyStudies} and [Not] Config_Alert_Off When Click_Grouped_activities_feature Then Verify_Grouped_activities_feature_page
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Grouped activities" feature nav menu option
        When config alert is "on"
        Then Grouped Activities feature page is empty

    @19368
    Scenario: Given Verify_Grouped_Activities_Cancel_popup_displayed When Click_Yes_cancel_button Then Verify_Grouped_Activities_modal_closed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Grouped activities" feature nav menu option
        When the Add Activity button is clicked
        And unsaved changes are made to the activity modal
        And Activity Modal Cancel button is clicked
        Then Verify Cancel modal
        And click the "Yes" button on the Cancel modal
        Then Verify Grouped activities feature page

    @19369
    Scenario: Draft_Study_{MyStudies} and Click_on_{GroupedActivities}_feature and On_{Add}_modal_with_{Unsavedchanges}_edits When Click_Cancel_button Then Verify_Grouped_Activities_Cancel_p...
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Grouped activities" feature nav menu option
        When the Add Activity button is clicked
        And unsaved changes are made to the activity modal
        And Activity Modal Cancel button is clicked
        Then Verify Cancel modal

    @19370
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_In_{StudyBA}_User and Draft_Study_{MyStudies} and Click_on_{GroupedActivities}_feature and On_{Add}_modal_with_{Unsavedchanges}_edits When Click_Cancel_button Then Verify_Grouped_Activities_Cancel_p...
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Grouped activities" feature nav menu option
        When the Add Activity button is clicked
        And unsaved changes are made to the activity modal
        And the Save button is clicked
        And the "Edit" button for the first record is clicked
        And unsaved changes are made to the activity modal
        And Activity Modal Cancel button is clicked
        Then Verify Cancel modal

    @19381
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_In_{StudyBA}_User and Draft_Study_{MyStudies} and Click_on_{GroupedActivities}_feature and On_{Add}_modal_with_{Unsavedchanges}_edits When Click_Cancel_button Then Verify_Grouped_Activities_Cancel_p...
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Grouped activities" feature nav menu option
        When the Add Activity button is clicked
        And unsaved changes are made to the activity modal
        And the Save button is clicked
        And the "Delete" button for the first record is clicked
        Then Verify delete Grouped Activities confirmation modal
        When click the "Yes" button for the GA Delete Confirmation modal
        Then Verify successfully "Deleted" message
        Then verify GA record is deleted

    @19383
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_in_{StudyBA}_user and Draft_Study_{MyStudies} and On_{Groupedactivities}_feature_with_data When Click_Grouped_activities_Delete_button Then Verify_GACT_Delete_confirmation_popup_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Grouped activities" feature nav menu option
        When the Add Activity button is clicked
        And unsaved changes are made to the activity modal
        And the Save button is clicked
        And the "Delete" button for the first record is clicked
        Then Verify delete Grouped Activities confirmation modal
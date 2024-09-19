Feature: Patient Details

    #3205
    @patientDetail
    Scenario: On_dashboard and Draft_Study_{PatientDetails} When User_makes_changes Then Verify_unsaved_indicator_appears
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Height" card
        And making unsaved changes on the Height modal
        Then Verify the unsaved indicator appears for the "Height" tab

    #3207
    @patientDetail @3207
    Scenario: Given Verify_unsaved_indicator_appears When User_changes_tabs Then Verify_unsaved_indicator_remains
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Height" card
        And making unsaved changes on the Height modal
        And click the "Weight" tab from the Patient Details modal
        Then Verify the unsaved indicator appears for the "Height" tab

    @patientDetail @3202
    Scenario: COSMOS-3205 Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_In_{StudyBA}_User and On_dashboard and Draft_Study_{PatientDetails} When User_makes_changes Then Verify_unsaved_indicator_appears
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Height" card
        And making unsaved changes on the Height modal
        And click the Patient Details Save button
        Then Verify the save indicator is not shown for the "Height" tab
    
    #2977
    @patientDetail
    Scenario: On_dashboard and Draft_Study_{MyStudies} and On_Study_Landing_Page When Click_Patient_Details_button Then Verify_Patient_Details_feature_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        When click "Patient details" feature nav menu option
        Then verify Date of birth card is displayed for 2977
    
    #11278
    @patientDetail
    Scenario: Click_Patient_Details_button Then Verify_Patient_Details_feature_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        When click "Patient details" feature nav menu option
        Then verify "Patient details" feature page is displayed
    
    #2991
    @patientDetail
    Scenario: Given Verify_Patient_Details_feature_displayed When Click_DOB_PD_Edit_Button Then Verify_PD_Date_of_Birth_modal_tab_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click Date of birth Edit button
        Then verify Date of birth modal tab displayed
    
    #2992
    @patientDetail
    Scenario: Given Verify_PD_Date_of_Birth_modal_tab_displayed When Click_View_Countries_link Then Verify_System_Opens_New_Browser_Tab
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        And click Date of birth Edit button
        When click View Countries link
        Then verify "Countries" feature page is displayed in a new browser tab
    
    #2983
    @patientDetail
    Scenario: On_dashboard and Draft_Study_{MyStudies} and On_Study_Landing_Page When Click_Patient_Details_button Then Verify_Patient_Details_feature_displayed
        Given the user is logged in as "TESTLEAD1"
        And create or select a case a study
        When click "Patient details" feature nav menu option
        Then verify Date of birth card is displayed for 2983
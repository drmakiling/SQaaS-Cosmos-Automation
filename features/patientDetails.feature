Feature: Patient Details

    #3205
    @patientDetail
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_In_{StudyBA}_User and On_dashboard and Draft_Study_{PatientDetails} When User_makes_changes Then Verify_unsaved_indicator_appears
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
    
    #2977
    @patientDetail
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_In_{StudyBA}_User and On_dashboard and Draft_Study_{MyStudies} and On_Study_Landing_Page When Click_Patient_Details_button Then Verify_Patient_Details_feature_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        When click "Patient details" feature nav menu option
        Then verify Date of birth card is displayed
    
    #11278
    @patientDetail
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_In_{StudyBA}_User and On_dashboard and Draft_Study_{MyStudies} and On_Study_Landing_Page When Click_Patient_Details_button Then Verify_Patient_Details_feature_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        When click "Patient details" feature nav menu option
        Then verify "Patient details" feature page is displayed
    
    #2991
    @patientDetail
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_In_{StudyBA}_User and On_dashboard and Draft_Study_{MyStudies} and On_Study_Landing_Page When Click_Patient_Details_button Then Verify_Patient_Details_feature_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click Date of birth Edit button
        Then verify Date_of_birth_modal_tab_displayed


    #2995
    @patientDetail @2995
    Scenario: Given Verify_PD_Date_of_Birth_modal_tab_displayed and Edit_Date_of_birth_form_{1} When Click_Save_date_of_birth_button Then Verify_PD_Date_of_Birth_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click Date of birth Edit button
        And Fill out Date of birth modal
        And Save button is clicked
        And close button is clicked
        Then Verify Date of birth data is saved
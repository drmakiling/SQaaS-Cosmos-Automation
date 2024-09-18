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
        Then verify "Patient details" feature page is displayed
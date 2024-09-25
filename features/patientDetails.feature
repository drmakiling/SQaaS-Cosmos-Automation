@patientDetail
Feature: Patient Details

    @2977
    Scenario: On_dashboard and Draft_Study_{MyStudies} and On_Study_Landing_Page When Click_Patient_Details_button Then Verify_Patient_Details_feature_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        When click "Patient details" feature nav menu option
        Then verify Date of birth card is displayed for 2977
    
    @11278
    Scenario: Click_Patient_Details_button Then Verify_Patient_Details_feature_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        When click "Patient details" feature nav menu option
        Then verify "Patient details" feature page is displayed
    
    @2991
    Scenario: Given Verify_Patient_Details_feature_displayed When Click_DOB_PD_Edit_Button Then Verify_PD_Date_of_Birth_modal_tab_displayed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When Date of birth card is displayed for 2991
        And click the Edit button for "Date of birth" card
        Then verify Date of birth modal tab is displayed

    @2992
    Scenario: Given Verify_PD_Date_of_Birth_modal_tab_displayed When Click_View_Countries_link Then Verify_System_Opens_New_Browser_Tab
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When Date of birth card is displayed for 2992
        And click the Edit button for "Date of birth" card
        And Date of birth modal tab is displayed
        And click View Countries link
        Then verify "Countries" feature page is displayed in a new browser tab

    @2983
     @regression @PDregres
    Scenario: On_dashboard and Draft_Study_{MyStudies} and On_Study_Landing_Page When Click_Patient_Details_button Then Verify_Patient_Details_feature_displayed
        Given the user is logged in as "TESTLEAD1"
        And create or select a case a study
        When click "Patient details" feature nav menu option
        Then verify Date of birth card is displayed for 2983
    
    @3691
     @regression @PDregres
    Scenario: On_dashboard and Draft_Study_{AllStudies} and On_Study_Landing_Page When Click_Patient_Details_button Then Verify_Patient_Details_feature_displayed
        Given the user is logged in as "STUDYBA2"
        And select a study in All Studies
        When click "Patient details" feature nav menu option
        Then verify Date of birth card is displayed for 3691
    
    @3692 @regression @PDregres
    Scenario: On_dashboard and Draft_Study_{AllStudies} and On_Study_Landing_Page When Click_Patient_Details_button Then Verify_Patient_Details_feature_displayed
        Given the user is logged in as "CONTENTMANAGER1"
        And select a study in All Studies
        When click "Patient details" feature nav menu option
        Then verify Date of birth card is displayed for 3692
    
    @3205
    Scenario: On_dashboard and Draft_Study_{PatientDetails} When User_makes_changes Then Verify_unsaved_indicator_appears
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Height" card
        And making unsaved changes on the Height modal
        Then verify the unsaved indicator appears for the "Height" tab

    @3207
    Scenario: Given Verify_unsaved_indicator_appears When User_changes_tabs Then Verify_unsaved_indicator_remains
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Height" card
        And making unsaved changes on the Height modal
        And click the "Weight" tab from the Patient Details modal
        Then verify the unsaved indicator appears for the "Height" tab

    @3202
    Scenario: Given Verify_unsaved_indicator_appears When User_saves_changes Then Verify_unsaved_indicator_removed
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Height" card
        And making unsaved changes on the Height modal
        And Save button is clicked
        Then verify the save indicator is not shown for the "Height" tab
    
    @2995
    Scenario: Given Verify_PD_Date_of_Birth_modal_tab_displayed and Edit_Date_of_birth_form_{1} When Click_Save_date_of_birth_button Then Verify_PD_Date_of_Birth_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Date of birth" card
        And fill out Date of birth modal
        And Save button is clicked
        And close button is clicked
        Then verify Date of birth data is saved

    @11310
    Scenario: Given Verify_PD_Gender_modal_tab_displayed and Edit_Gender_form_{1} When Click_PD_Gender_Save_button Then Verify_PD_Gender_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Gender" card
        And fill out "Gender" modal include in study no
        And Save button is clicked
        And close button is clicked
        Then verify Gender not included in study

    @11311
    Scenario: Given Verify_PD_Gender_modal_tab_displayed and Edit_Gender_form_{2} When Click_PD_Gender_Save_button Then Verify_PD_Gender_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Gender" card
        And fill out Gender modal  
        And Save button is clicked
        And close button is clicked
        Then verify Gender data is saved
    
    @11313
    Scenario: Given Verify_PD_Weight_modal_tab_displayed and Edit_Weight_form_{1} When Click_PD_Weight_Save_button Then Verify_PD_Weight_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Weight" card
        And fill out "Weight" modal include in study no
        And Save button is clicked
        And close button is clicked
        Then verify Weight not included in study
    
    @11314
    Scenario: Given Verify_PD_Weight_modal_tab_displayed and Edit_Weight_form_{2} When Click_PD_Weight_Save_button Then Verify_PD_Weight_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Weight" card
        And fill out Weight modal  
        And Save button is clicked
        And close button is clicked
        Then verify Weight data is saved
    
    @11318
    Scenario: Given Verify_PD_Height_modal_tab_displayed and Edit_Height_form_{1} When Click_PD_Height_Save_button Then Verify_PD_Height_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Height" card
        And fill out "Height" modal include in study no
        And Save button is clicked
        And close button is clicked
        Then verify Height not included in study

    @11319
    Scenario: Given Verify_PD_Height_modal_tab_displayed and Edit_Height_form_{2} When Click_PD_Height_Save_button Then Verify_PD_Height_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Height" card
        And fill out Height modal  
        And Save button is clicked
        And close button is clicked
        Then verify Height data is saved
    
    @11323
    Scenario: Given Verify_PD_Ethnicity_modal_tab_displayed and Edit_Ethnicity_form_{1} When Click_PD_Ethnicity_Save_button Then Verify_PD_Ethnicity_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Race" card
        And fill out "Race" modal include in study no
        And Save button is clicked
        And close button is clicked
        Then verify Race not included in study
    
    @11324
    Scenario: Given Verify_PD_Ethnicity_modal_tab_displayed and Edit_Ethnicity_form_{2} When Click_PD_Ethnicity_Save_button Then Verify_PD_Ethnicity_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Race" card
        And fill out Race modal  
        And Save button is clicked
        And close button is clicked
        Then verify Race data is saved

    @11310
    Scenario: Given Verify_PD_Gender_modal_tab_displayed and Edit_Gender_form_{1} When Click_PD_Gender_Save_button Then Verify_PD_Gender_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Gender" card
        And Fill out "Gender" modal include in study no
        And Save button is clicked
        And close button is clicked
        Then verify Gender not included in study

    @11311
    Scenario: Given Verify_PD_Gender_modal_tab_displayed and Edit_Gender_form_{2} When Click_PD_Gender_Save_button Then Verify_PD_Gender_modal_tab_saved_edits
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Patient details" feature nav menu option
        When click the Edit button for "Gender" card
        And Fill out Gender modal  
        And Save button is clicked
        And close button is clicked
        Then verify Gender data is saved


    @regression @PDregres
    Scenario: Patient Details regression flow
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        When click "Patient details" feature nav menu option
        Then verify Date of birth card is displayed for 2977
        When click the Edit button for "Height" card
        When making unsaved changes on the Height modal
        Then Verify the unsaved indicator appears for the "Height" tab
        When click the "Weight" tab from the Patient Details modal
        Then Verify the unsaved indicator appears for the "Height" tab
        When click the "Height" tab from the Patient Details modal
        When Save button is clicked
        Then Verify the save indicator is not shown for the "Height" tab
        When close button is clicked
        When click the Edit button for "Date of birth" card
        Then verify Date of birth modal tab is displayed
        When click View Countries link
        Then verify "Countries" feature page is displayed in a new browser tab
        When Fill out Date of birth modal
        When Save button is clicked
        When close button is clicked
        Then Verify Date of birth data is saved
        When click the Edit button for "Gender" card
        When Fill out "Gender" modal include in study no
        When Save button is clicked
        When click the "Weight" tab from the Patient Details modal
        When Fill out "Weight" modal include in study no
        When Save button is clicked
        When click the "Height" tab from the Patient Details modal
        When Fill out "Height" modal include in study no
        When Save button is clicked
        When click the "Race" tab from the Patient Details modal
        When Fill out "Race" modal include in study no
        When Save button is clicked
        When close button is clicked
        Then verify Gender not included in study
        Then verify Height not included in study
        Then verify Weight not included in study
        Then verify Race not included in study
        When click the Edit button for "Gender" card
        When Fill out Gender modal  
        When Save button is clicked
        When click the "Weight" tab from the Patient Details modal
        When fill out Weight modal  
        When Save button is clicked
        When click the "Height" tab from the Patient Details modal
        When fill out Height modal  
        When Save button is clicked
        When click the "Race" tab from the Patient Details modal
        When fill out Race modal  
        When Save button is clicked
        When close button is clicked
        Then verify Gender data is saved
        Then verify Weight data is saved
        Then verify Height data is saved
        Then verify Race data is saved
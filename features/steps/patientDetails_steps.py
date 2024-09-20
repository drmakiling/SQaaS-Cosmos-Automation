import re, time
from behave import *
from pages.Cosmos_PatientDetails import Cosmos_PatientDetails
from playwright.sync_api import expect

@when('Date of birth card is displayed for {case}')
@then('verify Date of birth card is displayed for {case}')
def verify_dob_card(context, case):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the verify_dob_card method to perform the actions
        cosmos_patient_details.verify_dob_card(case)

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('verify "Patient details" feature page is displayed')
def verify_patient_details_page(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the verify_dob_card method to perform the actions
        cosmos_patient_details.verify_dob_card("11278")
        # Call the verify_patient_details_page method to perform the actions
        cosmos_patient_details.verify_patient_details_page()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('Date of birth modal tab is displayed')
@then('verify Date of birth modal tab is displayed')
def verify_dob_modal_tab(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the verify_dob_modal_tab method to perform the actions
        cosmos_patient_details.verify_dob_modal_tab()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('click the Edit button for {card} card')
def click_Edit_button_for_card(context, card):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        patientDetails = Cosmos_PatientDetails(context.page)
        # Click the Edit button for the specified card
        patientDetails.clickEditbuttonForCard(card)

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('making unsaved changes on the Height modal')
def make_UnSaved_changes_to_Height_Modal(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        patientDetails = Cosmos_PatientDetails(context.page)
        #Select the Yes option for the Include in Study field
        patientDetails.selectIncludeInStudyOption("Height","Yes")
        #check if the save indicator is visible if not select the No radio button
        if(not(patientDetails.checkSavedIndicatorIsVisible("Height"))):
            patientDetails.selectIncludeInStudyOption("Height","No")       

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('Verify the unsaved indicator appears for the {tab} tab')
def verify_unsaved_indicator_appears(context,tab):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        patientDetails = Cosmos_PatientDetails(context.page)
        #Assert the saved indicator appears on the tab
        print(patientDetails.checkSavedIndicatorIsVisible(tab))
        assert patientDetails.checkSavedIndicatorIsVisible(tab)        

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('click View Countries link')
def click_view_countries_link(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the verify_dob_modal_tab method to perform the actions
        cosmos_patient_details.verify_dob_modal_tab()
        # Call the click_view_countries_link method to perform the actions
        cosmos_patient_details.click_view_countries_link(context)

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('verify "Countries" feature page is displayed in a new browser tab')
def verify_countries_page(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the verify_countries method to perform the actions
        cosmos_patient_details.verify_countries_page(context)
        
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('click the {tab} tab from the Patient Details modal')
def click_tab_in_patient_details_modal(context,tab):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        patientDetails = Cosmos_PatientDetails(context.page)
        # click the tab from the Patient Details modal
        patientDetails.clickTabFromPatientDetailsModal(tab)
    
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('click the Patient Details Save button')
def click_Patient_Details_Save_button(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        patientDetails = Cosmos_PatientDetails(context.page)
        # click the Save button
        patientDetails.clickPatientDetailsModalSaveButton()
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('Verify the save indicator is not shown for the {tab} tab')
def verify_saved_indicator_is_not_shown(context,tab):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        patientDetails = Cosmos_PatientDetails(context.page)
        #Assert the saved indicator appears on the tab
        time.sleep(5)
        print(patientDetails.checkSavedIndicatorIsVisible(tab))
        assert (not(patientDetails.checkSavedIndicatorIsVisible(tab)))        

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('Fill out Date of birth modal')
def fill_out_date_of_birth_modal(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        cosmos_patient_details.Fill_out_DOB_modal()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@when('Save button is clicked')
def click_save_button(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        cosmos_patient_details.click_save_button()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@when('close button is clicked')
def click_close_button(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        cosmos_patient_details.click_close_button()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open


@then('Verify Date of birth data is saved')
def verify_date_of_birth_saved(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        cosmos_patient_details.verify_date_of_birth_modal_saved()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@when('fill out {tab} modal include in study no')
def fill_out_modal_include_in_study_no(context, tab):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        cosmos_patient_details.selectIncludeInStudyOption(tab,"No")

    #check if the save indicator is visible if not select the No radio button
        if(not(cosmos_patient_details.checkSavedIndicatorIsVisible(tab))):
            cosmos_patient_details.selectIncludeInStudyOption(tab,"Yes")
            cosmos_patient_details.click_save_button()
            time.sleep(3)
            cosmos_patient_details.selectIncludeInStudyOption(tab,"No")

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@then('verify Gender not included in study')
def verify_gender_not_included_in_study(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        cosmos_patient_details.verify_gender_not_included_in_study()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@when('fill out Gender modal')
def fill_out_gender_modal(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        cosmos_patient_details.fill_out_gender_modal()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@then('verify Gender data is saved')
def Verify_gender_data_is_saved(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        cosmos_patient_details.verify_gender_data_is_saved()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@then('verify Weight not included in study')
def verify_weight_not_included_in_study(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the verify_weight_not_included_in_study method to perform the actions
        cosmos_patient_details.verify_weight_not_included_in_study()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@when('fill out Weight modal')
def fill_out_weight_modal(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the fill_out_weight_modal method to perform the actions
        cosmos_patient_details.fill_out_weight_modal()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@then('verify Weight data is saved')
def verify_weight_data_is_saved(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the verify_weight_data_is_saved method to perform the actions
        cosmos_patient_details.verify_weight_data_is_saved()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@then('verify Height not included in study')
def verify_height_not_included_in_study(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        cosmos_patient_details.verify_height_not_included_in_study()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@when('fill out Height modal')
def fill_out_height_modal(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the fill_out_height_modal method to perform the actions
        cosmos_patient_details.fill_out_height_modal()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open

@then('verify Height data is saved')
def verify_height_data_is_saved(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the verify_height_data_is_saved method to perform the actions
        cosmos_patient_details.verify_height_data_is_saved()

    except Exception as e:
        print(f"Test failed: {e}")
        time.sleep(99999)  # Pause to keep the browser open
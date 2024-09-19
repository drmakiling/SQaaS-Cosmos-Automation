import re, time
from behave import *
from pages.Cosmos_PatientDetails import Cosmos_PatientDetails
from playwright.sync_api import expect

@given('click "Patient details" feature nav menu option')
@when('click "Patient details" feature nav menu option')
def click_patient_details_nav_option(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the click_patient_details_nav_option method to perform the actions
        cosmos_patient_details.click_patient_details_nav_option()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('verify Date of birth card is displayed')
def verify_dob_card(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the verify_dob_card method to perform the actions
        cosmos_patient_details.verify_dob_card()

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
        cosmos_patient_details.verify_dob_card()
        # Call the verify_patient_details_page method to perform the actions
        cosmos_patient_details.verify_patient_details_page()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('click Date of birth Edit button')
def click_dob_edit_button(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the verify_dob_card method to perform the actions
        cosmos_patient_details.verify_dob_card()
        # Call the click_dob_edit_button method to perform the actions
        cosmos_patient_details.click_dob_edit_button()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('verify Date_of_birth_modal_tab_displayed')
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
        # Instantiate Cosmos_Country with the page object from the context
        patientDetails = Cosmos_PatientDetails(context.page)
        # Call the open_delete_country_modal method
        patientDetails.clickEditbuttonForCard(card)

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('making unsaved changes on the Height modal')
def make_UnSaved_changes_to_Height_Modal(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
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
        # Instantiate Cosmos_Country with the page object from the context
        patientDetails = Cosmos_PatientDetails(context.page)
        #Assert the saved indicator appears on Height tab
        print(patientDetails.checkSavedIndicatorIsVisible(tab))
        assert patientDetails.checkSavedIndicatorIsVisible(tab)        

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open
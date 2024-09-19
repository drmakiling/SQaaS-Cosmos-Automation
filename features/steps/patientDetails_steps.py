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
        
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

@then('verify "Patient details" feature page is displayed')
def verify_patient_details_page(context):
    try:
        # Instantiate Cosmos_PatientDetails with the page object from the context
        cosmos_patient_details = Cosmos_PatientDetails(context.page)
        # Call the click_patient_details_nav_option method to perform the actions
        cosmos_patient_details.verify_patient_details_page()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open
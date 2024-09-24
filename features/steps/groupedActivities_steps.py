import re, time
from behave import *
from pages.Cosmos_GroupedActivities import Cosmos_GroupedActivites
from playwright.sync_api import expect
import random

@then('Grouped Activities feature page is empty')
def verify_Grouped_Activities_is_Empty(context):
    try:
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        # Check if there are exisiting records, if so then delete all records
        if(patientGA.check_if_record_exists()):
            patientGA.delete_all_records()
        patientGA.verify_Grouped_Activities_Empty_State()
        
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('the Add Activity button is clicked')
def click_Add_Activity_button(context):
    try:
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        context.page.locator(patientGA.add_activity_button).click()
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('unsaved changes are made to the Add activity modal')
def enter_Unsaved_Changes_to_Activity_modal(context):
    try:
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        #Fill in the Add activity modal
        patientGA.input_SequenceID(str(time.time()))
        patientGA.input_Order_Sequence(str(random.randint(1,9999)))
        patientGA.select_Request_Code_Type("Questionnaire")
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('Add activity Modal Cancel button is clicked')
def click_Cancel_button(context):
    try:
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        context.page.locator(patientGA.Cancel_button).click()
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open 

@then('Verify Grouped activities feature page')
def verify_Grouped_Activities_Feature_Page(context):
    try:
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        expect(patientGA.page.locator(patientGA.featurePageTitle)).to_be_visible()
        expect(patientGA.page.locator(patientGA.add_activity_button)).to_be_visible()
        expect(patientGA.page.locator(patientGA.featureToggle)).to_be_visible()
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open 
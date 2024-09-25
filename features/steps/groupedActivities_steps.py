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

@when('unsaved changes are made to the activity modal')
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

@when('Activity Modal Cancel button is clicked')
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

@When('the Save button is clicked')
def click_Save_button(context):
    try: 
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        patientGA.click_Activity_Save_Button()
        time.sleep(2)
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open 

@When('the Save and add more button is clicked')
def click_Save_button(context):
    try: 
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        patientGA.click_Activity_Save_and_Add_More_Button()
        time.sleep(2)
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open 

@when('the {button} button for the first record is clicked')
def click_First_Record_Edit_button(context,button : str):
    try: 
        button = button.strip('"').capitalize()
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        if button == "Edit":
            patientGA.edit_the_first_record()
        else:
            patientGA.delete_the_first_record()
        
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open 

@Then('Verify the Grouped Activities record is deleted successfully')
def verify_GA_record_deleted(context):
    try: 
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        
        time.sleep(2)
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open 

@Then('Verify delete Grouped Activities confirmation modal')
def verify_GA_Delete_Confirm_Modal(context):
    try: 
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        expect(patientGA.page.locator(patientGA.delete_Confirmation_message)).to_be_visible()
        expect(patientGA.page.locator(patientGA.delete_Confirmation_message_No)).to_be_visible()
        expect(patientGA.page.locator(patientGA.delete_Confirmation_message_Yes)).to_be_visible()
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open 

@When('click the {button} button for the GA Delete Confirmation modal')
def click_Delete_Confirm_Modal_button(context, button : str):
    try: 
        button = button.strip('"').capitalize()
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        if(button == "Yes"):
            patientGA.page.locator(patientGA.delete_Confirmation_message_Yes).click()
            if (patientGA.page.locator(patientGA.recordCount).is_visible()):
                #save the current record count onto the context in order to be referenced later
                context.recordCount = patientGA.get_Record_Count()
        else:
            patientGA.page.locator(patientGA.delete_Confirmation_message_No).click()
        time.sleep(2)
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open 

@Then('verify GA record is deleted')
def ver_GA_Record_Deleted(context):
    try:
        # Instantiate Cosmos_GroupedActivities with the page object from the context
        patientGA = Cosmos_GroupedActivites(context.page)
        #context.recordCount needs to be instantiated first in another function; look at def click_Delete_Confirm_Modal_button function at top for reference
        recordCount = int(context.recordCount)
        print("This is the record count: " + str(recordCount))
        #check there is a updated record count, if so compare it with the old record count; return true if the updated record is less that old recordcount 
        if(recordCount >= 0 and patientGA.page.locator(patientGA.recordCount).is_visible()):
            compareCount = patientGA.get_Record_Count()
            if(recordCount <= compareCount):
                raise Exception("Record count has not decreased")
        #check if the old record count is greater than 0 and if the feature page is currently in an empty state
        elif(recordCount > 0 and patientGA.page.locator(patientGA.emptyStateMessage).is_visible()):
            assert True

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open 

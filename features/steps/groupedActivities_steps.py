import re, time
from behave import *
from pages.Cosmos_GroupedActivities import Cosmos_GroupedActivites
from playwright.sync_api import expect

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
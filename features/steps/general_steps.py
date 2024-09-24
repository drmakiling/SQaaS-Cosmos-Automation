import re, time
from behave import *
from pages.Cosmos_General import Cosmos_General
from playwright.sync_api import expect

@When("Click {card} Edit button")
def click_edit_for_card(context, card):
    try:
        # Instantiate Cosmos_General with the page object from the context
        generalPage =Cosmos_General(context.page)
        # Click the Edit button for the specified card
        generalPage.clickEditbuttonForCard(card)

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@Then("Verify min number of patients modal")
def Verify_min_number_patient_modal(context):
        # Instantiate Cosmos_General with the page object from the context
        generalPage =Cosmos_General(context.page)
        # Verify min number of patients modal 
        generalPage.verifyMinNumPatientModal()

@Then("Verify study overview modal")
def Verify_Study_Overview_modal(context):
        # Instantiate Cosmos_General with the page object from the context
        generalPage =Cosmos_General(context.page)
        # Verify study overview modal 
        generalPage.verifyStudyOverviewModal()

@When("And click on the button for comment side panel")
def click_button_for_comment_side_panel(context):
      # Instantiate Cosmos_General with the page object from the context
        generalPage =Cosmos_General(context.page)
        generalPage.clickCommentPanel_button()

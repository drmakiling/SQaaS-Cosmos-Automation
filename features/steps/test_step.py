import re, time
from behave import *
from pages.Cosmos_Main import Cosmos_Main
from pages.common_Login import Cosmos_Login_Page
from pages.SharedFunctions import sharedFunctions
import os
from dotenv import load_dotenv
from behave import given
from playwright.sync_api import Page, expect


@given('user is on "{env}"')
def navigate_to_cosmos(context, env):
    context.env = env
    context.page_object = Cosmos_Login_Page(context.page)
    context.page_object.navigate_to_environment(env)


@given('the user is logged in as "{User}"')
def verify_logged_in(context, User):
    try:
        # Initialize the page object and perform login
        context.page_object = Cosmos_Login_Page(context.page)

        # Ensure context.environment is being used
        print(f"Logging in to environment: {context.environment}")

        # Call login with the current environment
        context.page_object.login_to_page(User, context.environment)

        # Add assertions to verify successful login
        # Example assertion (modify the locator as needed):
        #assert context.page.locator("//element_or_text_to_check_after_login").is_visible()
    except Exception as e:
        print(f"Test failed: {e}")
        raise
        time.sleep(99999)  # Pause to keep the browser open

@given('create or select a case a study')
def create_case_study(context):
    try:
        # Instantiate Cosmos_Main with the page object from the context
        cosmos_main = Cosmos_Main(context.page)
        # Call the create_study method to perform the actions
        cosmos_main.create_study()

        # Add assertions or additional checks as needed

    except Exception as e:
        print(f"Test failed: {e}")
        raise
        time.sleep(99999)  # Pause to keep the browser open

@given('click {feature} feature nav menu option')
@when('click {feature} feature nav menu option')
def clickFeatureNavOption(context,feature):
    sharedFunction = sharedFunctions(context.page)
    sharedFunction.clickFeatureNavOption(feature)

@given('select a study in All Studies')
def select_study_all_studies(context):
    try:
        # Instantiate Cosmos_Main with the page object from the context
        cosmos_main = Cosmos_Main(context.page)
        # Call the select_study_all_studies method to perform the actions
        cosmos_main.select_study_all_studies()

        # Add assertions or additional checks as needed

    except Exception as e:
        print(f"Test failed: {e}")
        raise
        time.sleep(99999)  # Pause to keep the browser open

@given('config alert is {switch}')
@when('config alert is {switch}')
def config_alert_switch(context,switch : str):
    sharedFunction = sharedFunctions(context.page)
    sharedFunction.config_Alert_Switch(switch)

@then('Verify Cancel modal')
def verify_Cancel_Modal(context):
    try:
        sharedFunction = sharedFunctions(context.page)
        sharedFunction.ValidateSingleTabCancelModal()
    except Exception as e:
        print(f"Test failed: {e}")
        raise
        time.sleep(99999)  # Pause to keep the browser open

@then('click the {option} button on the Cancel modal')
def click_Yes_or_No_cancel_button(context,option : str):
    try:
        sharedFunction = sharedFunctions(context.page)
        sharedFunction.click_Yes_or_No_Cancel_Modal_button(option)
    except Exception as e:
        print(f"Test failed: {e}")
        raise
        time.sleep(99999)  # Pause to keep the browser open

@Then('Verify successfully {message} message')
def verify_Success_Message(context, message : str):
    try:
        message = message.lower().strip('"')
        sharedFunction = sharedFunctions(context.page)
        if message == "deleted":
            expect(sharedFunction.page.locator(sharedFunction.successDeleteMessage)).to_be_visible()
        elif message == "saved":
            expect(sharedFunction.page.locator(sharedFunction.successSavedMessage)).to_be_visible()
        else:
            raise Exception("Wrong success message entered in verify_Success_Message function")
        sharedFunction.successDeleteMessage
    except Exception as e:
        print(f"Test failed: {e}")
        raise
        time.sleep(99999)  # Pause to keep the browser open
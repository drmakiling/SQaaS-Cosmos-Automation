import re, time
from behave import *
from pages.Cosmos_Main import Cosmos_Main
from pages.common_Login import Cosmos_Login_Page
import os
from dotenv import load_dotenv
from behave import given


@given('user is on "{env}"')
def navigate_to_cosmos(context, env):
    context.env = env
    context.page_object = Cosmos_Login_Page(context.page)
    context.page_object.navigate_to_environment(env)



@given('the user is logged in as "{User}"')
def verify_logged_in(context, User):
    # Ensure the environment variables are loaded
    env_file_path = f'./environments/{context.env}/.env'  # Ensure you set `context.env` in a prior step
    load_dotenv(dotenv_path=env_file_path)

    # Initialize the page object and perform login
    context.page_object = Cosmos_Login_Page(context.page)
    context.page_object.login_to_page(User)

    # Add assertions to verify successful login
    # Example assertion (modify the locator as needed):
    #assert context.page.locator("//element_or_text_to_check_after_login").is_visible()


@then('create or select a case a study')
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



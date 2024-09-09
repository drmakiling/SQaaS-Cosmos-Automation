import re, time
from behave import *
from pages.Cosmos_Country import Cosmos_Country


@then('add a country with default settings')
def add_country_with_default_settings(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the add_country_simple method to perform the actions
        cosmos_country.add_country_simple()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('cancel the date of birth format modal')
def cancel_date_of_birth_format_modal(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the cancel_date_of_birth_format_modal method
        cosmos_country.cancel_date_of_birth_format_modal()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@When('verify the updated country dob format')
def verify_updated_country_dob_format(context):
    context.cosmos_country.configure_dob_format()

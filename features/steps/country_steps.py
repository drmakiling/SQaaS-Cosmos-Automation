import re, time
from behave import *
from pages.Cosmos_Country import Cosmos_Country
from playwright.sync_api import expect


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

@when('verify the date of birth format modal')
def verify_dob_format_modal(context):
    try:
        cosmos_country = Cosmos_Country(context.page)
        cosmos_country.add_country_simple()
        cosmos_country.verify_dob_format_modal()

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

@When('verify the updated country dob format for {case}')
def verify_updated_country_dob_format(context, case):
    # Initialize the page object and perform login
    cosmos_country = Cosmos_Country(context.page)

    cosmos_country.configure_dob_format(case)
@when('open delete country modal')
def open_delete_country_modal(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the open_delete_country_modal method
        cosmos_country.open_delete_country_modal()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('verify country is deleted')
def delete_country(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the delete_country method
        cosmos_country.delete_country()
    
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('edit an existing countries record')
def edit_existing_countries_record(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the edit_existing_countries_record method
        cosmos_country.edit_existing_countries_record(context)
    
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('click Cancel button')
def click_cancel_button(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the click_cancel_button method
        cosmos_country.click_cancel_button()
    
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('verify Countries cancel popup is not displayed')
def verify_countries_cancel_popup_not_displayed(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the verify_countries_cancel_popup_not_displayed method
        cosmos_country.verify_countries_cancel_popup_not_displayed(context)
    
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('open add country modal')
def open_add_country_modal(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the open_add_country_modal method
        cosmos_country.open_add_country_modal()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('verify cancel popup not displayed')
def verify_cancel_popup_not_displayed(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the verify_cancel_popup_not_displayed method
        cosmos_country.verify_cancel_popup_not_displayed()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@When('On Cancel pop up is displayed for Country')
def Cancel_Country_pop_up_displayed(context):
    try:
        cosmos_country = Cosmos_Country(context.page)
        cosmos_country.cancel_country_action()
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@When('edit country modal is opened')
def edit_country_modal_is_opened(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the cancel_country_action method
        cosmos_country.edit_country_modal_opened()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('add a country')
def add_country(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the add_country_simple method to perform the actions
        cosmos_country.add_country()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@when('yes is clicked')
def click_yes_cancel_button(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the click_cancel_button method
        cosmos_country.click_yes_cancel_button()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('countries feature page is displayed')
def countries_feature_page_displayed(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the verify_cancel_popup_not_displayed method
        cosmos_country.countries_feature_page_displayed()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

@then('verify cancel popup is displayed')
def verify_cancel_popup_displayed(context):
    try:
        # Instantiate Cosmos_Country with the page object from the context
        cosmos_country = Cosmos_Country(context.page)
        # Call the verify_cancel_popup_not_displayed method
        cosmos_country.cancel_country_popup_displayed()

    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

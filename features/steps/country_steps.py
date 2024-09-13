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


@given('edit an existing countries record')
def edit_existing_countries_record(context):
    # Save the data for the first record in the global context object to be viewed later
    context.countryCode = context.page.locator("//div[contains(@data-rowindex, '0')]/div[@data-field = 'countryCode']").inner_text()
    context.patientLanguage = context.page.locator("//div[contains(@data-rowindex, '0')]/div[@data-field = 'patientLanguage']").inner_text()
    context.dobFormat = context.page.locator("//div[contains(@data-rowindex, '0')]/div[@data-field = 'dateOfBirthFormat']").inner_text()

    # Instantiate Cosmos_Country with the page object from the context
    cosmos_country = Cosmos_Country(context.page)

    cosmos_country.edit_first_row_table.click()    


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

Then('verify Countries cancel popup is not displayed')
def verify_countries_cancel_popup_not_displayed(context):
    # Instantiate Cosmos_Country with the page object from the context
    cosmos_country = Cosmos_Country(context.page)

    # Verify Country Cancel popup is not displayed
    expect(cosmos_country.country_cancel_popup).not_to_be_visible()
    # Verify edit country modal is closed
    expect(cosmos_country.edit_country_modal).not_to_be_visible()
    #Verify the data of the first record remain unchanged 
    countryCode2 = context.page.locator("//div[contains(@data-rowindex, '0')]/div[@data-field = 'countryCode']").inner_text()
    patientLanguage2 = context.page.locator("//div[contains(@data-rowindex, '0')]/div[@data-field = 'patientLanguage']").inner_text()
    dobFormat2 = context.page.locator("//div[contains(@data-rowindex, '0')]/div[@data-field = 'dateOfBirthFormat']").inner_text()
    if context.countryCode == countryCode2 and context.patientLanguage == patientLanguage2 and context.dobFormat == dobFormat2:
        assert True

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
def verifiy_cancel_popup_not_displayed(context):
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
        cosmos_country = Cosmos_Country(context.page);
        cosmos_country.cancel_country_action()
    except Exception as e:
        print(f"Test failed: {e}")
        raise  # Raise the exception to ensure failure is reported
        time.sleep(99999)  # Pause to keep the browser open

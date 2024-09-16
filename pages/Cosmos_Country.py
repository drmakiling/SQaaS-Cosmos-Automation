import time

from playwright.sync_api import Page, expect
from utils.wait_helpers import wait_and_click_element, wait_for_element

class Cosmos_Country:
    def __init__(self, page: Page):
        self.page = page  # Ensure page is set
        self.edit_country_modal = "//div[@role='dialog']"
        self.countries_tab = "//p[contains(text(), 'Countries')]"
        self.add_country_button = "//button[contains(text(), 'Add country')]"
        self.country_code_field = "//div[@data-testid='countryCode']//input"
        self.languages_field = "//div[@data-testid='patientLanguage']//input"
        self.dob_format_rtsm = "//input[contains(@value, 'RTSM')]"
        self.dob_format_custom = "//div[@role='radiogroup']//input[contains(@value, 'custom')]"
        self.select_format_dropdown = "//div[@id='Select Format-select']"
        self.save_button = "(//button[contains(text(), 'Save')])[1]"
        self.cancel_button = "(//button[contains(text(), 'Cancel')])[1]"
        self.cancel_popup_text_1 = "//span[contains(text(), 'Would you like to cancel?')]"
        self.cancel_popup_text_2 = "//span[contains(text(), 'Any updates will not be saved')]"
        self.yes_button = "//button[contains(text(), 'Yes')]"
        self.no_button = "//button[contains(text(), 'No')]"
        self.country_cancel_popup = "(//div[@role='dialog'])[2]"
        self.first_row_table = "//div[contains(@data-rowindex, '0')]"
        self.edit_first_row_table = "//button[contains(@data-testid, 'action_icon_0')]"
        self.delete_first_row_table = "//button[contains(@data-testid, 'action_icon_1')]"
        self.delete_popup_text = "//span[contains(text(), 'Would you like to delete this country?')]"
        self.information_deleted_successfully = "//div[contains(text(), 'Information deleted successfully')]"
        self.records_in_the_list = "//p[contains(text(), 'records in the list')]"
        self.date_of_birth_format_button = "//p[contains(text(), 'Date of birth format')]"
        self.date_of_birth_format_title = "//span[contains(text(), 'Date of Birth format')]"
        self.date_of_birth_rtsm_description_text = "//p[contains(text(), 'All countries')]"
        self.date_of_birth_format_modal = "//div[@role='dialog']"
        self.date_of_birth_custom_format_button = "//div/h3[contains(text(), 'Custom')]"
        self.date_of_birth_rtsm_format_button = "//div/h3[contains(text(), 'RTSM')]"
        self.date_of_birth_save_button = "//button[contains(text(), 'Save')]"
        self.date_of_birth_cancel_button = "//button[contains(text(), 'Cancel')]"
        self.date_of_birth_custom_format_card = "//h3[text()='Custom format']"
        self.date_of_birth_custom_defined_by_RTSM_card = "//h3[text()='Defined by RTSM']"
        self.disabled_save_button = "//button[@disabled and text()='Save']"
        self.dob_table_format = "//div[@data-rowindex = '0']//div[@data-field='dateOfBirthFormat']"
        self.first_record_country_code = "//div[contains(@data-rowindex, '0')]/div[@data-field = 'countryCode']"
        self.first_record_patient_language = "//div[contains(@data-rowindex, '0')]/div[@data-field = 'patientLanguage']"
        self.first_record_dob_format = "//div[contains(@data-rowindex, '0')]/div[@data-field = 'dateOfBirthFormat']"

    def add_country_simple(self):
        self.page.locator(self.countries_tab).click()
        self.page.locator(self.add_country_button).click()
        self.page.locator(self.country_code_field).click()
        time.sleep(2)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        self.page.locator(self.languages_field).click()
        time.sleep(2)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.page.keyboard.press("Escape")

        # Check if RTSM radio button is disabled; if so, click Custom radio button and select from dropdown
        if self.page.locator(self.dob_format_rtsm).is_disabled():
            self.page.locator(self.dob_format_custom).click()
            self.page.locator(self.select_format_dropdown).click()
            time.sleep(2)
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")
        else:
            self.page.locator(self.dob_format_rtsm).click()

        self.page.locator(self.save_button).click()

    def cancel_date_of_birth_format_modal(self):
        # Click on the 'Date of Birth Format' button
        self.page.locator(self.date_of_birth_format_button).click()

        # Click on the 'Cancel' button
        self.page.locator(self.date_of_birth_cancel_button).click()

        # Verify that the modal is no longer visible
        expect(self.page.locator(self.date_of_birth_format_modal)).not_to_be_visible()
    
    def configure_dob_format(self, case: str):
        wait_and_click_element(self.page, self.date_of_birth_format_button)
        wait_and_click_element(self.page, self.date_of_birth_rtsm_format_button)

        if self.page.locator(self.save_button).is_disabled():
            if case == "3412":
                # First set of actions
                wait_and_click_element(self.page, self.date_of_birth_custom_format_button)
                wait_and_click_element(self.page, self.save_button)
                wait_and_click_element(self.page, self.date_of_birth_format_button)
                wait_and_click_element(self.page, self.date_of_birth_rtsm_format_button)
            elif case == "3413":
                # Second set of actions
                wait_and_click_element(self.page, self.date_of_birth_rtsm_format_button)
                wait_and_click_element(self.page, self.save_button)
                wait_and_click_element(self.page, self.date_of_birth_format_button)
                wait_and_click_element(self.page, self.date_of_birth_custom_format_button)

        wait_and_click_element(self.page, self.save_button)

    def open_delete_country_modal(self):
        # Click on the 'Delete' button
        self.page.locator(self.first_row_table).hover()
        self.page.locator(self.delete_first_row_table).click()

        # Verify delete country modal
        expect(self.page.locator(self.delete_popup_text)).to_contain_text("Would you like to delete this country?")
        expect(self.page.locator(self.yes_button)).to_contain_text("Yes")
        expect(self.page.locator(self.no_button)).to_contain_text("No")
    
    def delete_country(self):
        # Click on the 'Yes' button
        self.page.locator(self.yes_button).click()

        wait_for_element(self.page, self.edit_country_modal, 'hidden')

        # Get record count before deletion
        record_count_1 = int(self.page.locator(self.records_in_the_list).text_content()[0])

        # Delete country
        expect(self.page.locator(self.information_deleted_successfully)).to_contain_text("Information deleted successfully")

        wait_for_element(self.page, self.information_deleted_successfully, 'hidden')

        # Get record count after deletion
        record_count_2 = int(self.page.locator(self.records_in_the_list).text_content()[0])

        assert record_count_2 == record_count_1 - 1

    def verify_dob_format_modal(self):
        self.page.locator(self.date_of_birth_format_button).click()
        time.sleep(2)

        expect(self.page.locator(self.date_of_birth_format_modal)).to_be_visible()
        expect(self.page.locator(self.date_of_birth_rtsm_description_text)).to_be_visible()

    def edit_existing_countries_record(self, context):
        # Save the data for the first record in the global context object to be viewed later
        context.country_code = self.page.locator(self.first_record_country_code).inner_text()
        context.patient_language = self.page.locator(self.first_record_patient_language).inner_text()
        context.dob_format = self.page.locator(self.first_record_dob_format).inner_text()
        self.page.locator(self.first_row_table).hover()
        self.page.locator(self.edit_first_row_table).click()

    def click_cancel_button(self):
        self.page.locator(self.cancel_button).click()

    def verify_countries_cancel_popup_not_displayed(self, context):
        # Verify Country Cancel popup is not displayed
        expect(self.page.locator(self.country_cancel_popup)).not_to_be_visible()
        # Verify edit country modal is closed
        expect(self.page.locator(self.edit_country_modal)).not_to_be_visible()
        #Verify the data of the first record remain unchanged
        country_code2 = self.page.locator(self.first_record_country_code).inner_text()
        patient_language2 = self.page.locator(self.first_record_patient_language).inner_text()
        dob_format2 = self.page.locator(self.first_record_dob_format).inner_text()
        if context.country_code == country_code2 and context.patient_language == patient_language2 and context.dob_format == dob_format2:
            assert True

    def open_add_country_modal(self):
        # Click on the 'Add country' button
        self.page.locator(self.countries_tab).click()
        self.page.locator(self.add_country_button).click()

    def verify_cancel_popup_not_displayed(self):
        # Verify Country Cancel popup is not displayed
        expect(self.page.locator(self.country_cancel_popup)).not_to_be_visible()

        # Verify Add country modal is closed
        expect(self.page.locator(self.edit_country_modal)).not_to_be_visible()

    def cancel_country_action(self):
        # Cause cancel popup to display
        wait_and_click_element(self.page, self.countries_tab)
        wait_and_click_element(self.page, self.add_country_button)
        wait_and_click_element(self.page, self.country_code_field)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        wait_and_click_element(self.page, self.cancel_button)

        # Verify text 1. Would you like to cancel 2. Any updates will not be saved 3. Yes 4. No
        expect(self.page.locator(self.cancel_popup_text_1)).to_contain_text("Would you like to cancel?")
        expect(self.page.locator(self.cancel_popup_text_2)).to_contain_text("Any updates will not be saved")
        expect(self.page.locator(self.yes_button)).to_contain_text("Yes")
        expect(self.page.locator(self.no_button)).to_contain_text("No")

    def add_country(self):
        self.page.locator(self.countries_tab).click()
        self.page.locator(self.add_country_button).click()
        self.page.locator(self.country_code_field).click()
        time.sleep(2)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

    def edit_country_modal_opened(self):
        self.page.locator(self.first_row_table).hover()
        self.page.locator(self.edit_first_row_table).click()
        self.page.locator(self.languages_field).click()
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.page.keyboard.press("Escape")

    def cancel_country_popup_displayed(self):
        # Verify text 1. Would you like to cancel 2. Any updates will not be saved 3. Yes 4. No
        wait_for_element(self.page, self.cancel_popup_text_1)
        expect(self.page.locator(self.cancel_popup_text_1)).to_contain_text("Would you like to cancel?")
        wait_for_element(self.page, self.cancel_popup_text_2)
        expect(self.page.locator(self.cancel_popup_text_2)).to_contain_text("Any updates will not be saved")
        wait_for_element(self.page, self.yes_button)
        expect(self.page.locator(self.yes_button)).to_contain_text("Yes")
        wait_for_element(self.page, self.no_button)
        expect(self.page.locator(self.no_button)).to_contain_text("No")

    def click_yes_cancel_button(self):
        # click yes in cancel popup
        wait_for_element(self.page, self.yes_button)
        self.page.locator(self.yes_button).click()

    def countries_feature_page_displayed(self):
        # Verify modal is closed
        expect(self.page.locator(self.edit_country_modal)).not_to_be_visible()

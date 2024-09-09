import time

from playwright.sync_api import Page, expect

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
        self.wait_and_click_element(self.date_of_birth_format_button)
        self.wait_and_click_element(self.date_of_birth_rtsm_format_button)

        if self.page.locator(self.save_button).is_disabled():
            if case == "3412":
                # First set of actions
                self.wait_and_click_element(self.date_of_birth_custom_format_button)
                self.wait_and_click_element(self.save_button)
                self.wait_and_click_element(self.date_of_birth_format_button)
                self.wait_and_click_element(self.date_of_birth_rtsm_format_button)
            elif case == "3413":
                # Second set of actions
                self.wait_and_click_element(self.date_of_birth_rtsm_format_button)
                self.wait_and_click_element(self.save_button)
                self.wait_and_click_element(self.date_of_birth_format_button)
                self.wait_and_click_element(self.date_of_birth_custom_format_button)

        self.wait_and_click_element(self.save_button)



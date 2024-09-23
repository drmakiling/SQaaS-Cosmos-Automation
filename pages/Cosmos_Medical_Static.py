from utils.wait_helpers import wait_and_click_element, wait_for_element
import time


class MedicationStatusFeaturePage():
    def __init__(self, page):
        self.page = page
        self.medication_static_tab = "//p[contains(text(), 'Medication static')]"
        self.add_medication_status_button = "//button[contains(text(), 'Add medication status')]"
        self.patient_medication_status_field = "(//input[contains(@class, 'MuiSelect')])[1]/parent::*"

        # Activity card
        self.card_header = "//input[@name='ActivityCardSection-cardHeader']"
        self.card_sub_header = "//input[@name='ActivityCardSection-cardSubHeader']"
        self.dosage_header = "//input[@name='ActivityCardSection-dosageHeader']"
        self.dosage_sub_header = "//input[@name='ActivityCardSection-dosageSubHeader']"
        self.dosage_time_header = "//input[@name='ActivityCardSection-timeHeader']"
        self.dosage_time_sub_header = "//input[@name='ActivityCardSection-timeSubHeader']"
        self.save_button = "(//button[contains(text(), 'Save')])[1]"
        self.close_button = "//button[contains(text(), 'Close')]"

        # Medication card
        self.medication_modal_tab = "//button[@id='Medication-1']"
        self.button_text = "//input[@name='MedicationSection-buttonText']"
        self.nav_bar_title = "//input[@name='MedicationSection-navBarTitle']"
        self.category_header = "//input[@name='MedicationSection-categoryHeader']"
        self.header_field = "//input[@name='MedicationSection-header']"
        self.description_field = "//input[@name='MedicationSection-description']"
        self.medication_dosage_header = "//input[@name='MedicationSection-dosageHeader']"
        self.medication_dosage_sub_header = "//input[@name='MedicationSection-medicationDosageSubHeader']"
        self.medication_dosage_time_header = "//input[@name='MedicationSection-medicationTimeHeader']"
        self.medication_dosage_time_sub_header = "//input[@name='MedicationSection-timeSubHeader']"

        # Medication table
        self.medication_record_context_menu_last_record = "(//*[local-name()='svg' and @data-testid='MoreVertIcon']/*[local-name()='path'])[last()]"
        self.delete_button = "(//span[contains(text(), 'Delete')])[last()]"
        self.three_dot_button = "(//*[name()='svg' and @data-testid='MoreVertIcon'])[1]"
        self.delete_record_button = "(//span[contains(text(), 'Delete')])[1]"
        self.yes_delete_button = "//button[contains(text(),'Yes')]"

    def create_medication_status_activity_card_only(self):
        wait_and_click_element(self.page, self.medication_static_tab)
        wait_and_click_element(self.page, self.add_medication_status_button)
        wait_and_click_element(self.page, self.patient_medication_status_field)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        self.page.locator(self.card_header).fill(str(time.time()))
        self.page.locator(self.card_sub_header).fill(str(time.time()))

        self.page.locator(self.dosage_header).fill(str(time.time()))
        self.page.locator(self.dosage_sub_header).fill(str(time.time()))

        self.page.locator(self.dosage_time_header).fill(str(time.time()))
        self.page.locator(self.dosage_time_sub_header).fill(str(time.time()))

        wait_and_click_element(self.page, self.save_button)
        wait_and_click_element(self.page, self.close_button)

    def create_medication_status_minimum(self):
        wait_and_click_element(self.page, self.medication_static_tab)
        wait_and_click_element(self.page, self.add_medication_status_button)
        wait_and_click_element(self.page, self.patient_medication_status_field)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        wait_and_click_element(self.page, self.save_button)
        wait_and_click_element(self.page, self.close_button)

    def create_medication_status_both_cards(self):
        """Fill Out Activity card"""
        wait_and_click_element(self.page, self.medication_static_tab)
        wait_and_click_element(self.page, self.add_medication_status_button)
        wait_and_click_element(self.page, self.patient_medication_status_field)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        self.page.locator(self.card_header).fill(str(time.time()))
        self.page.locator(self.card_sub_header).fill(str(time.time()))

        self.page.locator(self.dosage_header).fill(str(time.time()))
        self.page.locator(self.dosage_sub_header).fill(str(time.time()))

        self.page.locator(self.dosage_time_header).fill(str(time.time()))
        self.page.locator(self.dosage_time_sub_header).fill(str(time.time()))

        wait_and_click_element(self.page, self.save_button)

        """Fill Out Medication Card"""
        wait_and_click_element(self.page, self.medication_modal_tab)

        self.page.locator(self.button_text).fill(str(time.time()))
        self.page.locator(self.nav_bar_title).fill(str(time.time()))
        self.page.locator(self.category_header).fill(str(time.time()))
        self.page.locator(self.header_field).fill(str(time.time()))
        self.page.locator(self.description_field).fill(str(time.time()))
        self.page.locator(self.medication_dosage_header).fill(str(time.time()))
        self.page.locator(self.medication_dosage_sub_header).fill(str(time.time()))
        self.page.locator(self.medication_dosage_time_header).fill(str(time.time()))
        self.page.locator(self.medication_dosage_time_sub_header).fill(str(time.time()))

        wait_and_click_element(self.page, self.save_button)
        wait_and_click_element(self.page, self.close_button)

    def delete_medication_record(self):
        wait_and_click_element(self.page, self.three_dot_button)
        wait_and_click_element(self.page, self.delete_record_button)
        wait_and_click_element(self.page, self.yes_delete_button)

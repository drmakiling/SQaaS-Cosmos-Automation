from playwright.sync_api import expect
from utils.wait_helpers import wait_and_click_element, wait_for_element

class HumanBioSampleFeaturePage():
    def __init__(self, page):
        self.page = page
        # Feature page locators
        self.human_bio_samples_tab = "//li//p[contains(text(),'Human bio samples')]"
        self.no_bio_samples_alert_message = '//div[contains(text(),"There are no human bio samples yet. Entries will be added automatically once record(s) in the ")]'
        self.no_kit_sample_information_alert_message = '//div[contains(text(),"Enable Labcorp system OR HBS data hub system in ")]'
        self.integrations_message_link = '//div[contains(text(),"There are no human bio samples yet. Entries will be added automatically once record(s) in the ")]//button[contains(text(),"Integrations")]'
        self.visits_message_link = '//button[contains(text(),"Visits")]'
        self.kit_sample_information_edit_button = '//div/span[contains(text(),"Kit/sample information")]/following::button[contains(text(),"Edit")]'
        self.first_bio_sample_record_row = '//div[@data-rowindex="0"]'
        self.bio_sample_record_edit_button = '//button[@data-testid="action_icon_0"]//span[@class="MuiBox-root css-10usvc8"]'
        self.bio_sample_record_delete_button = '//button[@data-testid="action_icon_1"]//span[@class="MuiBox-root css-10usvc8"]'
        # Edit kit/sample information modal
        self.bardcode_length_input_field = '//input[@name="KitSampleInformationSection-barcodeLength"]'
        self.save_button = '//button[contains(text(),"Save")]'
        # Edit human bio sample modal
        self.sample_type_all_radio_button = '//input[@name= "sampleType-field1" and @value = "All"]'
        self.sample_type_select_radio_button = '//input[@value="Select sample type"]'
        self.analysis_all_radio_button = '//input[@name= "analysisInformation-field1" and @value="All"]'
        self.analysis_select_radio_button = '//input[@value="Select analyte/analysis"]'
        self.process_sample_all_radio_button = '//input[@name= "processSampleType-field1" and @value = "All"]'
        self.process_sample_select_radio_button = '//input[@value="Select process sample type"]'

    def editKitSampleInformationModal(self, length: int):
        wait_and_click_element(self.page, self.human_bio_samples_tab)
        wait_and_click_element(self.page, self.kit_sample_information_edit_button)
        wait_for_element(self.page, self.bardcode_length_input_field)  # Ensure the field is visible
        self.page.fill(self.bardcode_length_input_field, str(length))
        wait_and_click_element(self.page, self.save_button)

    def checkNoBioSamplesMessage(self):
        wait_and_click_element(self.page, self.human_bio_samples_tab)
        expect(self.page.locator(self.no_bio_samples_alert_message)).to_be_visible()
        expect(self.page.locator(self.no_kit_sample_information_alert_message)).to_be_visible()

import time

from playwright.sync_api import Page, expect
from utils.wait_helpers import wait_and_click_element, wait_for_element


class Cosmos_GroupedActivites:
    def __init__(self, page: Page):
        self.page = page  # Ensure page is set
        self.featurePageTitle = "//h6[text()='Grouped activities']"
        self.firstRecord = "//div[@data-testid='datagrid-table']//div[@role='row' and contains(@class, 'MuiDataGrid-row')][1]"
        self.firstRecordDeleteButton = "//button[@data-testid='action_icon_1'][1]"
        self.featureToggle = "//h6[text()='Grouped activities']/following-sibling::div//input[@type = 'checkbox']"

        #Feature page empty state message
        self.emptyStateMessage = "//p[text()='There are no records yet.']"

        # Feature Toggle
        self.Grouped_Activities_feature_toggle = "//h6[text()='Grouped activities']/following-sibling::div//input[@type='checkbox']"

        # Add activity
        self.add_activity_button = "//button[text()='Add activity']"

        #Delete confirmation modal
        self.delete_Confirmation_message = "//div[@role='dialog']//span[text()='Would you like to delete this grouped activity?']"
        self.delete_Confirmation_message_Yes = "//div[@role='dialog']//button[text()='Yes']"
        self.delete_Confirmation_message_No = "//div[@role='dialog']//button[text()='No']"

        #Add acivity modal
        self.sequenceID = "//input[@name='sequenceIdName']"
        self.orderInSequenece = "//input[@name='orderInSequence']"

        self.Save_button = "//button[text() = 'Save']"
        self.Save_and_add_more_button = "//button[text() = 'Save and add more']"
        self.Cancel_button = "//button[contains(text(), 'Cancel')]"

    def check_if_record_exists(self) -> bool:
        return self.page.locator(self.firstRecord).is_visible()
    
    def delete_the_first_record(self):
        self.page.locator(self.firstRecord).hover()
        time.sleep(1)
        self.page.locator(self.delete_the_first_record).click()

    def delete_all_records(self): 
        while (self.page.locator(self.firstRecord).is_visible()):
            self.page.locator(self.firstRecord).hover()
            time.sleep(1)
            self.page.locator(self.delete_the_first_record).click()
            self.page.locator(self.delete_Confirmation_message_Yes).click()
            time.sleep(2)

    def verify_Grouped_Activities_Empty_State(self):
        expect(self.page.locator(self.emptyStateMessage)).to_be_visible()
        expect(self.page.locator(self.Grouped_Activities_feature_toggle)).to_be_visible()
        expect(self.page.locator(self.featurePageTitle)).to_be_visible()
        expect(self.page.locator(self.add_activity_button)).to_be_visible()

    def select_Request_Code_Type(self, type : str):
        type = type.strip('"').capitalize()
        self.page.locator("//h6[text()='Request code type']/following-sibling::div//input[@value = '"+ type + "']")

    def input_SequenceID(self, name : str):
        name = name.strip('"')
        self.page.locator(self.sequenceID).fill(name)

    def input_Order_Sequence(self, num : str):
        self.page.locator(self.orderInSequenece).fill(num)

        
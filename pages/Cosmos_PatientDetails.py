import time

from playwright.sync_api import Page, expect
from utils.wait_helpers import wait_and_click_element, wait_for_element

class Cosmos_PatientDetails:
    def __init__(self, page: Page):
        self.page = page  # Ensure page is set
        self.Patient_Details_feature = "//p[contains(text(), 'Patient details')]"
        #Jason was wrong, don't worry its fixed now
        self.DOB_card_Visible_for_GST_value = " //div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for GST')]//parent::div/following-sibling::div/p"
import time

from playwright.sync_api import Page, expect
from utils.wait_helpers import wait_and_click_element, wait_for_element

class Cosmos_PatientDetails:
    def __init__(self, page: Page):
        self.page = page  # Ensure page is set
        self.Patient_Details_feature = "//p[contains(text(), 'Patient details')]"
        #Jason was wrong, don't worry its fixed now
        self.DOB_card_Visible_for_GST_value = " //div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for GST')]//parent::div/following-sibling::div/p"
        self.Height_card_edit = "//div[@data-testid='height-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        self.Height_Include_in_study_Yes_Radio_button = "//input[@name ='HeightSection-includedInStudy' and  @value='Yes']"
        self.Height_Include_in_study_No_Radio_button = "//input[@name ='HeightSection-includedInStudy' and  @value='No']"
        self.Height_Save_Indicator = "//button[@id = 'Height-3']/*[name()='svg' and @data-testid = 'CircleIcon']"

    def checkTabSavedIndicator(self, tab : str) -> bool:
        return self.page.locator("//button[@id = " + tab + "]/*[name()='svg' and @data-testid = 'CircleIcon']").is_visible()
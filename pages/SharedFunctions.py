from utils.wait_helpers import wait_and_click_element, wait_for_element
from playwright.sync_api import Page, expect
import time
from typing import List

class sharedFunctions():
    def __init__(self, page : Page):
        self.page = page
        #Single tab cancel modal
        self.cancel_popup_text_1 = "//span[contains(text(), 'Would you like to cancel?')]"
        self.cancel_popup_text_2 = "//span[contains(text(), 'Any updates will not be saved')]"
        self.yes_button = "//button[contains(text(), 'Yes')]"
        self.no_button = "//button[contains(text(), 'No')]"
        self.cancel_pop_text_2_Multi_tab = "//p[contains(text(), 'Any updates will not be saved for:')]"
        #Login
        self.sso_button = "//button[contains(text(),'Sign in with AstraZeneca SSO')]"
        self.email_input = "//input[@type='email']"
        self.submit_button = "//input[@type='submit']"
        self.password_input = "//input[@type='password']"
        #Study config alert toggle
        self.config_on = "//div[@data-testid='config-alert-toggle']//span[contains(@class,'Mui-checked')]"
        self.config_off = "//div[@data-testid='config-alert-toggle']//span[contains(@class,'MuiSwitch-root')]"

    def ValidateSingleTabCancelModal(self):
        # Use wait_for_element for elements that are not clicked
        wait_for_element(self.page, self.cancel_popup_text_1)
        wait_for_element(self.page, self.cancel_popup_text_2)
        wait_for_element(self.page, self.yes_button)
        wait_for_element(self.page, self.no_button)

    def login_cosmos(self, email, password):
        # Click the SSO button, fill out email, password, and submit
        wait_and_click_element(self.page, self.sso_button)
        self.page.locator(self.email_input).fill(email)
        wait_and_click_element(self.page, self.submit_button)
        self.page.locator(self.password_input).fill(password)
        wait_and_click_element(self.page, self.submit_button)

    def click_Yes_or_No_Cancel_Modal_button(self,option : str):
        option = option.strip('"').strip().capitalize()
        self.page.locator("//button[contains(text(), '" + option + "')]").click()

    def config_Alert_Switch(self, switch : str):
        switch = switch.lower().strip('"').strip()
        if(switch == 'on'):
            if(not(self.page.locator(self.config_on).is_visible())):
                self.page.locator(self.config_off).click()
        elif(switch == 'off'):
            if(self.page.locator(self.config_on).is_visible()):
                self.page.locator(self.config_off).click()
        time.sleep(2)

    def clickFeatureNavOption(self,feature : str):
        self.page.locator("//p[contains(text(), " + feature + ")]").click()

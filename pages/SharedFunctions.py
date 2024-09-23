from utils.wait_helpers import wait_and_click_element, wait_for_element
from typing import List

class sharedFunctions():
    def __init__(self, page):
        self.page = page
        self.cancel_popup_text_1 = "//span[contains(text(), 'Would you like to cancel?')]"
        self.cancel_popup_text_2 = "//span[contains(text(), 'Any updates will not be saved')]"
        self.yes_button = "//button[contains(text(), 'Yes')]"
        self.no_button = "//button[contains(text(), 'No')]"
        self.cancel_pop_text_2_Multi_tab = "//p[contains(text(), 'Any updates will not be saved for:')]"
        self.sso_button = "//button[contains(text(),'Sign in with AstraZeneca SSO')]"
        self.email_input = "//input[@type='email']"
        self.submit_button = "//input[@type='submit']"
        self.password_input = "//input[@type='password']"

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


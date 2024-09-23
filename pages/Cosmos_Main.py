from behave import *
from playwright.sync_api import Page, expect
import re
import time

from utils.wait_helpers import wait_and_click_element, wait_for_element


class Cosmos_Main:
    def __init__(self, page):
        self.browser = "https://the-internet.herokuapp.com/"
        self.page = page

        self.create_new_study = "//button[@data-testid='btn-create-new-study']"
        self.create_new_form = "//h3[@data-testid='card-create-from-blank']"
        self.form_time = "//input[@id=':r4:']"
        self.form_create = "//button[text()='Create']"
        self.email_search = "(//input[@aria-label='Search for name or email'])[1]"
        self.tab_click = "((//div[@id='simple-tabpanel-0'])[1]//span)[4]"
        self.assign_team = "//button[contains(text(), 'Assign team')]"
        self.existing_form = "((//h6[text()='My Studies']//ancestor::*[last()-7]//following-sibling::div)[2]//div[@data-testid='study-card'])[1]"
        self.existing_form_all_studies = "((//h6[text()='All Studies']//ancestor::*[last()-7]//following-sibling::div)[2]//div[@data-testid='study-card'])[1]"
        self.create_new_study_button = "//button[contains(@data-testid, 'btn-create-new-study')]"
        self.create_from_blank_card = "//h3[contains(@data-testid, 'card-create-from-blank')]"
        self.study_name_field = "//input[@id=':r4:']"
        self.create_button = "//button[contains(text(), 'Create')]"
        self.assign_user_field = "(//input[contains(@aria-label, 'Search for name or email')])[1]"
        self.assign_user_option = "((//div[@id='simple-tabpanel-0'])[1]//span)[4]"
        self.assign_team_button = "//button[contains(text(), 'Assign team')]"
        self.implementation_lead_textbox = "//p[contains(text(), 'Implementation Lead')]/following-sibling::div//input[contains(@aria-label, 'Search for name or email')]"
        self.imple_lead1_option = "//p[contains(text(), 'Implementation Lead')]/following-sibling::div//span[contains(text(),'COSMOS IMPLE LEAD1')]"
        self.ecoa_textbox = "//p[contains(text(), 'eCOA')]/following-sibling::div//input[contains(@aria-label, 'Search for name or email')]"
        self.ecoa_ba1_option = "//p[contains(text(), 'eCOA')]/following-sibling::div//span[contains(text(),'BA1')]"

    def create_study(self):
        # Click on the 'Create New Study' button
        time.sleep(6)


        # Check if the existing form exists
        if self.page.locator(self.existing_form).is_visible():
            # If the existing form is found, click on it
            wait_and_click_element(self.page, self.existing_form)
        # else:
        #     wait_and_click_element(self.page, self.create_new_study)
        #     # If the existing form doesn't exist, proceed with the rest of the function
        #     # Click on the 'Create from Blank' form
        #     wait_and_click_element(self.page, self.create_new_form)
        #
        #     # Fill in the form with the current time
        #     wait_for_element(self.page, self.form_time).fill(str(time.time()))
        #
        #     # Click the 'Create' button
        #     wait_and_click_element(self.page, self.form_create)
        #
        #     # Search for an email and click the tab
        #     for _ in range(3):  # Repeat 3 times
        #         wait_for_element(self.page, self.email_search).click()
        #         self.page.locator(self.email_search).fill("cos")
        #         wait_and_click_element(self.page, self.tab_click)
        #
        #     # Assign the team
        #     wait_and_click_element(self.page, self.assign_team)
    
    def select_study_all_studies(self):
        time.sleep(6)

        # Check if the existing form exists
        if self.page.locator(self.existing_form_all_studies).is_visible():
            # If the existing form is found, click on it
            wait_and_click_element(self.page, self.existing_form_all_studies)

    def create_study_from_blank(self):
        wait_and_click_element(self.page, self.create_new_study_button)
        wait_and_click_element(self.page, self.create_from_blank_card)

        # Fill in the study name
        wait_for_element(self.page, self.study_name_field)  # Ensure the field is visible
        self.page.fill(self.study_name_field, f"test {str(time.time())}")

        wait_and_click_element(self.page, self.create_button)

        wait_and_click_element(self.page, self.assign_user_field)
        self.page.fill(self.assign_user_field, "cos")
        wait_and_click_element(self.page, self.assign_user_option)

        wait_and_click_element(self.page, self.implementation_lead_textbox)
        self.page.fill(self.assign_user_field, "cos")  # Reuse the assign_user_field
        wait_and_click_element(self.page, self.imple_lead1_option)

        wait_and_click_element(self.page, self.ecoa_textbox)
        self.page.fill(self.assign_user_field, "cos")  # Reuse the assign_user_field
        wait_and_click_element(self.page, self.ecoa_ba1_option)

        wait_and_click_element(self.page, self.assign_team_button)
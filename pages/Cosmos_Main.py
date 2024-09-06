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

    def create_study(self):
        # Click on the 'Create New Study' button
        time.sleep(6)
        wait_and_click_element(self.page, self.create_new_study)
        #self.page.locator(self.sign_in_button).click()
        # Click on the 'Create from Blank' form
        wait_and_click_element(self.page, self.create_new_form)

        # Fill in the form with the current time
        wait_for_element(self.page, self.form_time).fill(str(time.time()))

        # Click the 'Create' button
        wait_and_click_element(self.page, self.form_create)

        # Search for an email and click the tab
        for _ in range(3):  # Repeat 3 times
            wait_for_element(self.page, self.email_search).click()
            self.page.locator(self.email_search).fill("cos")
            wait_and_click_element(self.page, self.tab_click)

        # Assign the team
        wait_and_click_element(self.page, self.assign_team)

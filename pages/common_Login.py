import time

from behave import *
from playwright.sync_api import Page, expect
import re, os
from dotenv import load_dotenv
from utils import wait_helpers
from utils.wait_helpers import wait_for_element, wait_and_click_element


class Cosmos_Login_Page:
    def __init__(self, page):
        self.browser_link = "https://the-internet.herokuapp.com/basic_auth"
        self.page = page

        self.sign_in_button = "//button[contains(text(),'Sign in with AstraZeneca SSO')]"
        self.email_input = "//input[@type='email']"
        self.submit_button = "//input[@type='submit']"
        self.password_input = "//input[@type='password']"

    def navigate_to_environment(self, env: str):
        # Set the environment
        self.env = env

        # Construct the path to the .env file based on the environment parameter
        env_file_path = f'./environments/{env}/.env'

        # Load environment variables from the .env file
        load_dotenv(dotenv_path=env_file_path)

        # Retrieve the release URL from the environment variables
        release_url = os.getenv('RELEASE_URL')

        # Navigate to the release URL
        self.page.goto(release_url)

    def login_to_page(self, user_account):
        # Load environment variables
        account = os.getenv(user_account + "_ACCOUNT")
        password = os.getenv(user_account + "_PASSWORD")
        self.page.wait_for_load_state("networkidle")

        # Wait for and click the 'Sign in with AstraZeneca SSO' button
        wait_and_click_element(self.page, self.sign_in_button)

        # Wait for and fill in the email input field
        wait_for_element(self.page, self.email_input).fill(account)

        # Wait for and click the submit button
        wait_and_click_element(self.page, self.submit_button)

        # Wait for and fill in the password input field
        wait_for_element(self.page, self.password_input).fill(password)

        # Wait for and click the submit button again
        wait_and_click_element(self.page, self.submit_button)

        # Wait for and click the submit button again
        #wait_and_click_element(self.submit_button).click()

    def verify_login_is_successful(self):
        expect(self.page.locator(self.login_header)).to_be_visible()
        expect(self.page.locator(self.login_success_message)).to_be_visible()

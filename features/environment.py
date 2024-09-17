from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright, Page, expect
import time, json, base64, os
from datetime import datetime

@fixture
def playwright(context):
    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)


def before_all(context):
    use_fixture(playwright, context)
    context.environment = "Dev"

def before_scenario(context, scenario):
    context.playwright_context = context.browser.new_context(viewport={'width': 1920, 'height': 1080})
    context.page = context.playwright_context.new_page()


# Directory where screenshots will be saved
SCREENSHOT_DIR = os.path.join(os.getcwd(), "reports", "screenshots")


# Make sure the directory exists
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)


def after_step(self, context, step):
    if step.status == 'failed':
        # Your logic for capturing screenshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{timestamp}_{step.name}.png"
        screenshot_path = os.path.join('screenshots', screenshot_name)

        context.page.screenshot(path=screenshot_path)
        self.log_screenshot(screenshot_path)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        print("Test failed, keeping the browser open for debugging.")
        time.sleep(2)
    else:
        context.page.close()  # Or whatever cleanup you have for closing the browser



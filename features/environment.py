from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
from utils.utilities import capture_screenshot, clean_old_screenshot_folders, TIMESTAMP, SCREENSHOT_DIR, delete_old_reports
import time

@fixture
def playwright(context):
    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)

def before_all(context):
    use_fixture(playwright, context)
    context.environment = "Dev"
    context.screenshot_folder = SCREENSHOT_DIR
    clean_old_screenshot_folders() # Cleans old screenshots
    delete_old_reports('reports')

def before_scenario(context, scenario):
    context.playwright_context = context.browser.new_context(viewport={'width': 1920, 'height': 1080})
    context.page = context.playwright_context.new_page()

def after_scenario(context, scenario):
    if scenario.status == "failed":
        print(f"Test failed: {scenario}")
        time.sleep(2)
    else:
        context.page.close()

def after_step(context, step):
    # Capture screenshot on failure
    capture_screenshot(context, step)  # This will handle the screenshot capture in failures

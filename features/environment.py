from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright, Page, expect
import json, base64
from datetime import datetime

@fixture
def playwright(context):
    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)


def before_all(context):
    use_fixture(playwright, context)


def before_scenario(context, scenario):
    context.playwright_context = context.browser.new_context(viewport={'width': 1920, 'height': 1080})
    context.page = context.playwright_context.new_page()


def after_scenario(context, scenario):
    context.page.close()


import time

from playwright.sync_api import Page, expect
from utils.wait_helpers import wait_and_click_element, wait_for_element


class Cosmos_GroupedActivites:
    def __init__(self, page: Page):
        self.page = page  # Ensure page is set
        self.firstRecord = "//div[@data-testid='datagrid-table']//div[@role='cell'][1]"
        self.firstRecordDeleteButton = "//button[@data-testid='action_icon_1']"

    def check_if_record_exists(self) -> bool:
        return self.page.locator(self.firstRecord).is_visible()
    
    def delete_the_first_record(self):
        self.page.locator(self.firstRecord).hover()
        time.sleep(1)
        self.page.locator(self.delete_the_first_record).click()
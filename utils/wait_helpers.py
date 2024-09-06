
from playwright.sync_api import Page

def wait_for_element(page: Page, selector: str, state='visible', timeout=30000):
    """Wait for an element to be in a specific state with a custom timeout."""
    element = page.locator(selector)

    # Check if the element is already in the desired state
    if state == 'visible' and element.is_visible():
        return element

    element.wait_for(state=state, timeout=timeout)
    return element

def wait_and_click_element(page: Page, selector: str, state='visible', timeout=30000):
    """Wait for an element to be in a specific state and then click it."""
    element = wait_for_element(page, selector, state, timeout)
    element.click()
    return element

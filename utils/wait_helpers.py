
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


def wait_and_scroll_to_element(page, locator):
    """
    Scrolls to the specified element if it is off-screen.

    Args:
    - page: The Playwright page object.
    - locator: The locator for the element to scroll to.
    """
    # Wait for the element to be present in the DOM
    element = page.locator(locator)

    # Scroll the element into view
    element.scroll_into_view_if_needed()

    # Optionally, you can also wait for the element to become visible
    wait_for_element(page, locator)

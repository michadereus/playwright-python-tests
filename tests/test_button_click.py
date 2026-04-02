import re, time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_button_click(page):
    page.goto("https://demoqa.com/buttons")
    time.sleep(1)
    
    page.get_by_role("button", name="Click Me", exact=True).click()
    time.sleep(1)
    
    expect(page.locator("#dynamicClickMessage")).to_have_text("You have done a dynamic click")
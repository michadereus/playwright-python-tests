import re, time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_textbox_submission(page):
    page.goto("https://demoqa.com/text-box")
    
    time.sleep(1)
    
    page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="Full Name").fill("John Wick")
    page.get_by_role("textbox", name="Full Name").press("Tab")
    page.get_by_role("textbox", name="name@example.com").fill("jwick@gmail.com")
    page.get_by_role("button", name="Submit").click()
    
    time.sleep(1)
    
    assert "John Wick" in page.text_content("body")
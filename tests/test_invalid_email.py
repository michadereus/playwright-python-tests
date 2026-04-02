import re, time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_invalid_email(page):
    page.goto("https://demoqa.com/text-box")
    time.sleep(1)
    page.fill("#userEmail", "invalid-email")
    page.click("#submit")    
    
    assert "@" not in page.input_value("#userEmail")
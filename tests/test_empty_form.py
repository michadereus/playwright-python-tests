import re, time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_empty_form(page):
    page.goto("https://demoqa.com/text-box")
    time.sleep(1)
    
    page.click("#submit")
    
    assert page.url == "https://demoqa.com/text-box"
import re, time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_element_visible(page):
    page.goto("https://demoqa.com/")
    time.sleep(1)
    
    assert page.get_by_text("Elements").is_visible()
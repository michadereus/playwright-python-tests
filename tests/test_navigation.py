import re, time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_navigation(page):
    page.goto("https://demoqa.com/")
    time.sleep(1)
    page.get_by_role("link", name="Elements").click()
    
    assert "elements" in page.url
import re, time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_homepage_load(page):
    page.goto("https://demoqa.com/")
    time.sleep(1)
    assert "demosite" in page.title()
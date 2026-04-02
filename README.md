# Playwright Automation Tests (Python)

This project demonstrates automated UI testing using Playwright and Python.

## Overview

This repository contains UI automation tests designed to validate common user interactions and application behavior. The tests focus on core QA concepts such as navigation, form handling, and UI validation.

## Test Coverage

- Homepage load (smoke test)
- Navigation between pages
- Form input and submission
- Button interaction and dynamic UI updates
- Element visibility verification
- Negative test case for invalid input

## Tech Stack

- Playwright
- Python
- PyTest

## How to Run

pip install -r requirements.txt  
playwright install  
pytest

## Repository Structure

playwright-python-tests/
│
├── tests/
│   ├── test_homepage.py
│   ├── test_navigation.py
│   ├── test_textbox_submission.py
│   ├── test_button_click.py
│   ├── test_element_visible.py
│   ├── test_empty_form.py
│   └── test_invalid_email.py
│
├── requirements.txt
└─  README.md

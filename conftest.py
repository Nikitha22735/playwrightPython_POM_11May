from playwright.sync_api import sync_playwright, expect
import pytest

# @pytest.fixture()
# def page():
#     with sync_playwright as p:
#         browser = p.chromium.launch()
#         context = browser.new_context()
#         page = context.new_page()
        # yield page

@pytest.fixture()
def navigateAmazon(page):
     page.goto("https://www.amazon.in/")

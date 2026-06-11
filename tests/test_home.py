# 1. titlecheck, url
# 2. adds , menu, search

from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.home
def test_titleCheck(page):
    page.goto("https://www.amazon.in/")
    # page.wait_for_selector("input#twotabsearchtextbox", timeout=50000)
    page.get_by_role("searchbox", name="Search Amazon.in").wait_for(state="visible", timeout=50000)
    expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
    
# validate UI elements
# def test_validateUIElements()
@pytest.mark.home
def test_validate_UI_elements(page):
    page.goto("https://www.amazon.in/")
    expect(page.get_by_label("Open All Categories Menu")).to_be_visible()
    expect( page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()
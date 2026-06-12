# 1. titlecheck, url
# 2. adds , menu, search

from playwright.sync_api import sync_playwright, expect
import pytest
from pages.home import homePage

@pytest.mark.home
def test_titleCheck(page,navigateAmazon):
    homePageObj = homePage(page)
    homePageObj.waitingForSearchBoxToBeVisible()
    homePageObj.verifyTitle()
    

@pytest.mark.home
def test_validate_UI_elements(page,navigateAmazon):
    homePageObj = homePage(page)
    homePageObj.validateThevisibityOfMenu()
    homePageObj.validateVisibilityOfSeachBox()
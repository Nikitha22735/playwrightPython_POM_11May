from playwright.sync_api import sync_playwright, expect

from pages.home import homePage
from pages.login import loginPage

def cookiesgeneartion():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context =  browser.new_context()
        page = context.new_page()
        page.goto("https://www.amazon.in/")
        page.wait_for_timeout(5000)
        homePageObj = homePage(page)
        loginPageObj = loginPage(page)

        homePageObj.clickOnAccountsndList()   
        loginPageObj.enterEmailValue("trainingplaywright@gmail.com")
        loginPageObj.clickOnContinueBtn()
        loginPageObj.enterPw("Welcome@04")
        loginPageObj.clickOnContinueBtn()   
        page.wait_for_timeout(5000)
        context.storage_state(path="cookies.json")


def test_navigation():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context =  browser.new_context(storage_state="cookies.json")
        page = context.new_page()
        page.goto("https://www.amazon.in/")
        page.wait_for_timeout(5000)
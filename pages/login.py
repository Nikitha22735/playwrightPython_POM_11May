import allure
from playwright.sync_api import sync_playwright, expect

class loginPage:
    def __init__(self,page):
        self.emailTextBox = page.locator("input#ap_email_login")
        self.continueBtn = page.locator('[type="submit"]')
        self.pwTextBox = page.locator("#ap_password")

    @allure.step("enterEmailValue")
    def enterEmailValue(self, email):
        self.emailTextBox.fill(email)

    @allure.step("clickOnContinueBtn")
    def clickOnContinueBtn(self):
        self.continueBtn.click()

    @allure.step("enterPw")
    def enterPw(self,pw):
        self.pwTextBox.fill(pw)
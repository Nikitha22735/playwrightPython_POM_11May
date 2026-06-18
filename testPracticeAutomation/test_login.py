import allure
import pytest
from playwright.sync_api import expect
from pagesPracticeAutomation.login_page import LoginPage


@pytest.mark.usefixtures("page")
class TestPracticeAutomationLogin:
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.login_page = LoginPage(page)
        self.login_page.navigate_to_login_page()
    
    def test_positive_login_with_valid_credentials(self):
        with allure.step("Verify initial UI elements are displayed"):
            self.login_page.verify_username_field_visible()
            self.login_page.verify_password_field_visible()
            self.login_page.verify_submit_button_visible()
        
        with allure.step("Enter valid credentials and submit"):
            self.login_page.perform_login("student", "Password123")
        
        with allure.step("Verify successful login - URL validation"):
            self.login_page.verify_login_success_url()
        
        with allure.step("Verify successful login - Success message validation"):
            self.login_page.verify_login_success_text()
        
        with allure.step("Verify logout button is visible on success page"):
            self.login_page.verify_logout_button_visible()

    def test_negative_login_with_invalid_username(self):
        with allure.step("Verify initial UI elements are displayed"):
            self.login_page.verify_username_field_visible()
            self.login_page.verify_password_field_visible()
            self.login_page.verify_submit_button_visible()
        
        with allure.step("Enter invalid username and valid password"):
            self.login_page.perform_login("incorrectUser", "Password123")
        
        with allure.step("Verify user remains on login page (no redirect)"):
            self.login_page.verify_user_on_login_page()
        
        with allure.step("Verify error message for invalid username"):
            self.login_page.verify_error_message("Your username is invalid!")

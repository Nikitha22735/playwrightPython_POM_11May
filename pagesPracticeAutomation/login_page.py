import allure
from playwright.sync_api import expect
import re


class LoginPage:
    """Page Object Model for Practice Test Automation Login Page"""
    
    def __init__(self, page):
        """
        Initialize LoginPage with page object
        
        Args:
            page: Playwright page object
        """
        self.page = page
        self.base_url = "https://practicetestautomation.com/practice-test-login/"
        
        # Locators
        self.username_field = page.locator("input#username")
        self.password_field = page.locator("input#password")
        self.submit_button = page.locator("button#submit")
        self.error_message = page.locator("//div[@class='post-title' or contains(text(), 'invalid')]")
        self.logout_button = page.locator("a.wp-nav-menu-link")
    
    @allure.step("Navigate to Login Page")
    def navigate_to_login_page(self):
        """Navigate to the practice login page"""
        self.page.goto(self.base_url)
        self.page.wait_for_load_state("networkidle")
    
    @allure.step("Enter Username: {username}")
    def enter_username(self, username):
        """
        Enter username in the username field
        
        Args:
            username: Username to enter
        """
        self.username_field.fill(username)
    
    @allure.step("Enter Password: {password}")
    def enter_password(self, password):
        """
        Enter password in the password field
        
        Args:
            password: Password to enter
        """
        self.password_field.fill(password)
    
    @allure.step("Click Submit Button")
    def click_submit_button(self):
        """Click the Submit button"""
        self.submit_button.click()
    
    @allure.step("Verify Login Success - URL Check")
    def verify_login_success_url(self):
        """Verify successful login by checking URL"""
        self.page.wait_for_url("**/logged-in-successfully/", timeout=5000)
        expect(self.page).to_have_url(re.compile(r".*logged-in-successfully.*"))
    
    @allure.step("Verify Login Success - Text Verification")
    def verify_login_success_text(self):
        """Verify successful login by checking success message text"""
        # Wait for success message
        success_text = self.page.locator("text=/Congratulations|successfully logged in/i")
        expect(success_text).to_be_visible()
    
    @allure.step("Verify Logout Button Visible")
    def verify_logout_button_visible(self):
        """Verify logout button is displayed after successful login"""
        logout_btn = self.page.locator("text=Log out")
        expect(logout_btn).to_be_visible()
    
    @allure.step("Verify Error Message: {expected_error}")
    def verify_error_message(self, expected_error):
        """
        Verify error message is displayed with expected text
        
        Args:
            expected_error: Expected error message text
        """
        error_msg = self.page.locator("#error")
        expect(error_msg).to_be_visible()
        expect(error_msg).to_contain_text(expected_error)
    
    @allure.step("Verify User Remains on Login Page")
    def verify_user_on_login_page(self):
        """Verify user is still on the login page (no redirect)"""
        expect(self.page).to_have_url(self.base_url)
    
    @allure.step("Verify Username Field is Visible")
    def verify_username_field_visible(self):
        """Verify username field is displayed"""
        expect(self.username_field).to_be_visible()
    
    @allure.step("Verify Password Field is Visible")
    def verify_password_field_visible(self):
        """Verify password field is displayed"""
        expect(self.password_field).to_be_visible()
    
    @allure.step("Verify Submit Button is Visible")
    def verify_submit_button_visible(self):
        """Verify submit button is displayed"""
        expect(self.submit_button).to_be_visible()
    
    @allure.step("Perform Login")
    def perform_login(self, username, password):
        """
        Perform complete login action
        
        Args:
            username: Username to enter
            password: Password to enter
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit_button()

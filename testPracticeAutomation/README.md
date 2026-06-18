# Practice Test Automation - Login Page Automation

## Overview
This is a Playwright-based Python automation framework for testing the Practice Test Automation login page using the Page Object Model (POM) design pattern.

**Website**: https://practicetestautomation.com/practice-test-login/

## Project Structure

```
playwrightPom_11May/
├── pagesPracticeAutomation/          # Page Object Models for Practice Automation
│   ├── __init__.py
│   └── login_page.py                 # Login Page Object
├── testPracticeAutomation/           # Test Cases for Practice Automation
│   ├── __init__.py
│   └── test_login.py                 # Login Test Cases
├── pages/                            # Other Page Objects (Amazon example)
├── tests/                            # Other Test Cases (Amazon example)
├── conftest.py                       # Pytest configuration and fixtures
├── pytest.ini                        # Pytest settings
├── requirements.txt                  # Python dependencies
└── manualtestcase.txt               # Manual test case documentation
```

## Test Credentials
- **Username**: `student`
- **Password**: `Password123`

## Test Cases Implemented

### TC_LOGIN_001 - Positive Login Test with Valid Credentials
**File**: [testPracticeAutomation/test_login.py](testPracticeAutomation/test_login.py)

**Description**: Verifies that a user can successfully login with valid credentials

**Steps**:
1. Navigate to the login page
2. Verify UI elements are displayed (username field, password field, submit button)
3. Enter valid credentials (username: student, password: Password123)
4. Click Submit button
5. Verify redirect to success page (URL contains "logged-in-successfully")
6. Verify success message is displayed
7. Verify logout button is visible on success page

**Status**: ✅ PASSED

### TC_LOGIN_002 - Negative Test with Invalid Username
**File**: [testPracticeAutomation/test_login.py](testPracticeAutomation/test_login.py)

**Description**: Verifies that a user cannot login with an invalid username and receives appropriate error message

**Steps**:
1. Navigate to the login page
2. Verify UI elements are displayed
3. Enter invalid username (incorrectUser) with valid password
4. Click Submit button
5. Verify user remains on login page (no redirect)
6. Verify error message "Your username is invalid!" is displayed

**Status**: ✅ PASSED

## Page Object Model - LoginPage

**File**: [pagesPracticeAutomation/login_page.py](pagesPracticeAutomation/login_page.py)

### Available Methods

#### Navigation
- `navigate_to_login_page()` - Navigate to the practice login page

#### User Actions
- `enter_username(username)` - Enter username in the username field
- `enter_password(password)` - Enter password in the password field
- `click_submit_button()` - Click the Submit button
- `perform_login(username, password)` - Perform complete login action (all 3 steps combined)

#### Verifications
- `verify_login_success_url()` - Verify URL redirect to success page
- `verify_login_success_text()` - Verify success message is displayed
- `verify_logout_button_visible()` - Verify logout button is visible
- `verify_error_message(expected_error)` - Verify error message text
- `verify_user_on_login_page()` - Verify user remains on login page
- `verify_username_field_visible()` - Verify username field is visible
- `verify_password_field_visible()` - Verify password field is visible
- `verify_submit_button_visible()` - Verify submit button is visible

## Running the Tests

### Prerequisites
```bash
pip install -r requirements.txt
```

### Run All Login Tests
```bash
pytest testPracticeAutomation/test_login.py -v
```

### Run Specific Test
```bash
# Positive Login Test
pytest testPracticeAutomation/test_login.py::TestPracticeAutomationLogin::test_positive_login_with_valid_credentials -v

# Negative Login Test
pytest testPracticeAutomation/test_login.py::TestPracticeAutomationLogin::test_negative_login_with_invalid_username -v
```

### Run with HTML Report
```bash
pytest testPracticeAutomation/test_login.py -v --html=report.html --self-contained-html
```

### Run with Allure Report
```bash
pytest testPracticeAutomation/test_login.py -v --alluredir=allure-results
allure serve allure-results
```

## Framework Features

### 1. Page Object Model (POM)
- Clean separation of test logic and page locators
- Reusable methods for common actions
- Easy maintenance and scalability

### 2. Allure Reporting
- Detailed test steps with @allure.step decorator
- Test title and description metadata
- Severity levels for test prioritization
- Comprehensive HTML reports

### 3. Playwright Features
- Fast and reliable browser automation
- Support for multiple browsers (Chromium, Firefox, WebKit)
- Built-in waits and synchronization
- Cross-platform support (Windows, Mac, Linux)

### 4. Pytest Integration
- Fixture-based setup and teardown
- Parameterization support
- Detailed failure reporting
- Easy test discovery and execution

## Locators Used

| Element | Locator | Type |
|---------|---------|------|
| Username Field | `input#username` | CSS Selector |
| Password Field | `input#password` | CSS Selector |
| Submit Button | `button#submit` | CSS Selector |
| Error Message | `#error` | CSS Selector |
| Logout Button | `text=Log out` | Text Selector |
| Success Message | `text=/Congratulations\|successfully logged in/i` | Regex Text |

## Dependencies

- **pytest** - Testing framework
- **pytest-playwright** - Pytest plugin for Playwright
- **playwright** - Browser automation library
- **allure-pytest** - Allure reporting integration
- **python-dotenv** - Environment variable management

See `requirements.txt` for complete list and versions.

## Future Test Cases

The framework is designed to support additional test cases:
- TC_LOGIN_003: Negative Password Test
- TC_LOGIN_004: Empty Username Test
- TC_LOGIN_005: Empty Password Test
- TC_LOGIN_006: Both Fields Empty Test
- TC_LOGIN_007: Case Sensitivity Test
- TC_LOGIN_008: SQL Injection Prevention Test
- TC_LOGIN_009: XSS Prevention Test
- TC_LOGIN_010: Page Load and UI Elements Test

See `manualtestcase.txt` for detailed manual test case documentation.

## Best Practices Implemented

✅ Page Object Model for code reusability
✅ Explicit waits for synchronization
✅ Meaningful method and variable names
✅ Docstrings for all methods
✅ Allure annotations for better reporting
✅ Proper assertion methods using expect()
✅ Separation of concerns (pages vs tests)
✅ Clear test step documentation
✅ Comprehensive test data management

## Notes

- Tests run headless by default (use `--headed` flag to see browser)
- Tests are independent and can run in any order
- Each test automatically cleans up after execution
- Tests use the pytest-playwright fixture for page management

---

**Author**: QA Automation Team  
**Date Created**: 2026-06-18  
**Last Updated**: 2026-06-18

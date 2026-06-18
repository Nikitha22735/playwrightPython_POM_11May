import allure
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
     outcome = yield
     report= outcome.get_result()

     if report.failed:
          page = item.funcargs.get("page")
          allure.attach(page.screenshot(), name="Failed page ss", attachment_type=allure.attachment_type.PNG)

          
     




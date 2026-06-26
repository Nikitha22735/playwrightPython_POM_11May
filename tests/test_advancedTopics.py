from playwright.sync_api import sync_playwright, expect

def dimesions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context =  browser.new_context(viewport={"width":600,"height":900})
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(5000)

def mobile():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context =  browser.new_context(**p.devices["iPhone XR"])
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(5000)


def geoLocationChange():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context =  browser.new_context(geolocation={"latitude":36.7783, "longitude":-119.4179}, permissions=["geolocation"])

        page = context.new_page()
        page.goto("https://browserleaks.com/geo")
        page.wait_for_timeout(15000)

def interNet():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context =  browser.new_context()
        page = context.new_page()
        context.set_offline(True)
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(5000)

def frames():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context =  browser.new_context()
        page = context.new_page()
        page.goto("https://demo.guru99.com/test/guru99home/")
        page.frame_locator('//iframe[contains(@src,"youtube")]').get_by_label("Play video").click()
        page.wait_for_timeout(5000)
        
##pip install pillow
from PIL import Image, ImageChops
def visualRegression():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context =  browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        # page.get_by_text("START").screenshot(path="ss2.png")
        # page.screenshot(full_page=True, path="ss1.png")
        img1 = Image.open("ss1.png")
        img2 = Image.open("ss2.png")
        diff = ImageChops.difference(img1, img2)
        print(diff.getbbox())
        assert diff.getbbox() is None

        expect(page).to_have_screenshot("ss1.png")


visualRegression()


# imh1 = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 2), (0, 0, 0, 0),(0, 0, 0, 0)]
# imh2 = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 3), (0, 0, 0, 0),(0, 0, 0, 0)]


# diff = [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, -1)]
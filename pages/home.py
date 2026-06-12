from playwright.sync_api import sync_playwright, expect

class homePage:

    def __init__(self,page):
        self.page = page
        self.searchBox = page.locator("input#twotabsearchtextbox")
        self.menuIcon = page.get_by_label("Open All Categories Menu")
        self.accountsndList = page.locator("//span[contains(text(),'Account & Lists')]")


    def waitingForSearchBoxToBeVisible(self):
        self.searchBox.wait_for(state="visible", timeout=50000)


    def validateVisibilityOfSeachBox(self):
         expect(self.searchBox).to_be_visible()

    def verifyTitle(self):
        expect(self.page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")


    def validateThevisibityOfMenu(self):
        expect(self.menuIcon).to_be_visible()

    def clickOnAccountsndList(self):
        self.accountsndList.click()
    

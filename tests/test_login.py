import pytest

from pages.home import homePage
from pages.login import loginPage

@pytest.mark.login
@pytest.mark.amazon
def test_positiveLogin(page,navigateAmazon):
    homePageObj = homePage(page)
    loginPageObj = loginPage(page)

    homePageObj.clickOnAccountsndList()   
    loginPageObj.enterEmailValue("trainingplaywright@gmail.com")
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw("Welcome@04")
    loginPageObj.clickOnContinueBtn()
    homePageObj.validateVisibilityOfSeachBox()
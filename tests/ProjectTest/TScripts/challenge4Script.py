from playwright.sync_api import sync_playwright
import sys
sys.path.append(sys.path[0] + "/..")

from ProjectTest.ElementLocator.commonLocators import *
from ProjectTest.ElementLocator.coreReusabilityLib import *
from ProjectTest.ElementLocator.dashBoardPage import *
from ProjectTest.TestCapabilities.testCap import testCapabilities


select = elementSelector()

capability = testCapabilities()


def set_test_status(page, status, remark):
    page.evaluate("_ => {}",
                  "PlayW Status: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")

class Challange4Test:
    '''
    Class and method Declaration for the action functionality for Challenge 4 Task.

    Initiate browser and call the required URL for the Action


    Exception handling is Not implemented and Logger class is not Implemented.
    Reporting Modules is also not Implemented
    '''
    def __init__(self, playwright) -> None:
        #self.browser = playwright.chromium.launch(headless=True)
        self.browser = playwright.chromium.launch(headless=False)
        #self.browser = playwright.chromium.connect(capability.Chrome())
        page = self.browser.new_page()
        self.page = page
    def launchWebUI(self):
        self.page.goto(select.challange4Url())
        title = self.page.title()
        print(title)

    def loginUsername(self, data):
        self.page.locator(select.loginUName()).fill(data)

    def loginPassword(self, data):
        self.page.locator(select.loginPwd()).fill(data)

    def clickLoginSubmitChal4(self):
        self.page.locator(select.signInBtn()).click()

    def captureScreenPostLoginChall4(self):
        self.page.screenshot(path="../ScreenProof/postloginChallenge4Screen.png", full_page=True)
        #self.page.locator(select.loginSuccessMsg()).

    def clickLogoutSubmit(self):
        self.page.locator(select.signOutBtn()).click()
        #self.page.locator(select.signOutBtn()).ispresent()

    def clickSignOutBtnChal4(self):
        self.page.locator(select.dashBoardSignOutBtn()).click()

    def clickdropDownBtnChal4(self):
        self.page.locator(select.dashBoardDropDownClick()).click()

    def getDashboardMsgCha4(self):
        text = self.page.locator(select.dashBoardPage()).inner_text()
        return text

    def getLoginUserNameChal4(self):
        text = self.page.locator(select.dashBoardUserData()).inner_text()
        return text


    def getSuccessStatus(self):
        return set_test_status(self.page, "passed", "Success")

    def getFailedStatus(self):
        return set_test_status(self.page, "failed", "Test failed")

    def closeBrowser(self):
        self.browser.close()